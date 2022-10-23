from functools import partial
import string, random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Student, Teacher, CustomUser
from .serializers import (
    StudentCreateSerializer,
    StudentDetailSerializer,
    StudentSerializer,
    UserCreateSerializer,
    UserSerializer,
)

# Create your views here.
def generateUsernameAndPassword(data):
    try:
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = (
            first_name[:3]
            + last_name[:3]
            + "".join(random.choice(string.digits) for i in range(2))
            + random.choice(string.punctuation)
        )
        password = (
            "".join(random.choice(string.ascii_lowercase) for i in range(3))
            + "".join(random.choice(string.ascii_uppercase) for i in range(3))
            + random.choice(string.digits)
            + random.choice(string.punctuation)
        )
        return [username, password]
    except:
        return ["", ""]


def standardizedErrors(serializer):
    standerdizedErrors = {}
    for error in serializer.errors:
        if error == "username" or error == "password":
            pass
        else:
            standerdizedErrors[error] = serializer.errors[error][0].__str__()
    return Response({"errors": standerdizedErrors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({"students": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def addStudent(request):
    username, password = generateUsernameAndPassword(request.data)
    request.data.update({"username": username, "password": password})
    userSerializer = UserCreateSerializer(data=request.data)
    if not userSerializer.is_valid():
        return standardizedErrors(userSerializer)

    user = userSerializer.save()
    request.data.update({"user": user.id})
    studentSerializer = StudentCreateSerializer(data=request.data, many=False)
    if not studentSerializer.is_valid():
        user.delete()
        return standardizedErrors(studentSerializer)
    student = studentSerializer.save()
    data = StudentDetailSerializer(student, many=False).data.copy()
    data["user"]["password"] = request.data["password"]
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(["PATCH", "PUT"])
@permission_classes([AllowAny])
def updateStudent(request):
    try:
        student_id = request.data["id"]
        try:
            student = Student.objects.get(id=student_id)
            userSerializer = UserSerializer(
                student.user, data=request.data, partial=True
            )
            if not userSerializer.is_valid():
                return standardizedErrors(userSerializer)
            studentSerializer = StudentCreateSerializer(
                student, data=request.data, partial=True
            )
            if not studentSerializer.is_valid():
                return standardizedErrors(studentSerializer)
            userSerializer.save()
            studentSerializer.save()
            data = StudentSerializer(student, many=False).data
            return Response(data, status=status.HTTP_202_ACCEPTED)
        except Student.DoesNotExist:
            return Response(
                {"message": f"Student with id={id} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
    except KeyError:
        return Response(
            {"message": "You should include the [id] of student you want to update"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteStudent(request, pk):
    if not pk:
        return Response(
            {"message": "You should include the [id] of student you want to update"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        student = Student.objects.get(id=pk)
        student.user.delete()
        return Response(
            {"message": f"Student with id={pk} deleted successfully"},
            status=status.HTTP_202_ACCEPTED,
        )
    except Student.DoesNotExist:
        return Response(
            {"message": f"Student with id={pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def searchStudent(request):
    SEARCH_COLUMNS = ["username", "first_name", "last_name", "father_name"]
    try:
        search = request.data["search"]
        search_by = request.data["searchBy"]
        if not SEARCH_COLUMNS.__contains__(search_by):
            return Response(
                {"message": f"[searchBy] should be one of {str(SEARCH_COLUMNS)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    except KeyError:
        return Response(
            {
                "message": "You should include the [search] and [searchBy] in your request body"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
