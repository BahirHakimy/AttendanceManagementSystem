import string, random
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes, parser_classes

from .models import Student, Teacher
from .serializers import (
    StudentCreateSerializer,
    StudentDetailSerializer,
    StudentSerializer,
    TeacherCreateSerializer,
    TeacherDetailSerializer,
    TeacherSerializer,
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


@api_view(["POST"])
@permission_classes([AllowAny])
def getUser(request):
    User = get_user_model()
    try:
        user_id = request.data["id"]
        try:
            user = User.objects.get(id=user_id)
            user_type = user.get_user_type()
            serializer = None
            if user_type["role"] == "admin":
                serializer = UserSerializer(user, many=False)
            elif user_type["role"] == "teacher":
                serializer = TeacherSerializer(
                    user.teacher, many=False, context={"request": request}
                )
            elif user_type["role"] == "student":
                serializer = StudentSerializer(
                    user.student, many=False, context={"request": request}
                )
            else:
                return Response(
                    "User with the given id doesn't has a role",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            data = serializer.data.copy()
            data.update({"role": user_type["role"]})
            return Response(
                data,
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            return Response(
                {"detail": f"User with id={user_id} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
    except KeyError:
        return Response(
            {"detail": "You should include the [id] of user in your request"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({"students": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([AllowAny])
def addStudent(request):

    username, password = generateUsernameAndPassword(request.data)
    request.data._mutable = True
    request.data.update({"username": username, "password": password})

    userSerializer = UserCreateSerializer(data=request.data, many=False)
    if not userSerializer.is_valid():
        return standardizedErrors(userSerializer)
    user = userSerializer.save()

    request.data.update({"user": user.id})
    request.data._mutable = False

    studentSerializer = StudentCreateSerializer(data=request.data, many=False)
    if not studentSerializer.is_valid():
        user.delete()
        return standardizedErrors(studentSerializer)
    student = studentSerializer.save()

    data = StudentDetailSerializer(
        student, many=False, context={"request": request}
    ).data.copy()
    data["user"]["password"] = request.data["password"]

    return Response(data, status=status.HTTP_201_CREATED)
    # return Response({}, status=status.HTTP_201_CREATED)


@api_view(["PATCH", "PUT"])
@parser_classes([MultiPartParser, FormParser])
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
                {"detail": f"Student with id={id} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
    except KeyError:
        return Response(
            {"detail": "You should include the [id] of student you want to update"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteStudent(request, pk):
    if not pk:
        return Response(
            {"detail": "You should include the [id] of student you want to update"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        student = Student.objects.get(id=pk)
        student.user.delete()
        return Response(
            {"detail": f"Student with id={pk} deleted successfully"},
            status=status.HTTP_202_ACCEPTED,
        )
    except Student.DoesNotExist:
        return Response(
            {"detail": f"Student with id={pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def searchStudent(request):
    User = get_user_model()
    SEARCH_COLUMNS = ["username", "first_name", "last_name", "father_name"]
    try:
        search = request.data["search"]
        search_by = request.data["searchBy"]
        if not SEARCH_COLUMNS.__contains__(search_by):
            return Response(
                {"detail": f"[searchBy] should be one of {str(SEARCH_COLUMNS)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users = None
        students = None
        if search_by == "father_name":
            students = Student.objects.filter(father_name__iexact=search)
        elif search_by == "username":
            users = User.objects.filter(username__iexact=search)
        elif search_by == "first_name":
            users = User.objects.filter(first_name__iexact=search)
        else:
            users = User.objects.filter(last_name__iexact=search)

        if students and len(students) > 0:
            serializer = StudentSerializer(students, many=True)
            return Response({"students": serializer.data}, status=status.HTTP_200_OK)
        elif users and len(users) > 0:
            data = []
            for user in users:
                if hasattr(user, "student"):
                    serializer = StudentSerializer(user.student, many=False)
                    data.append(serializer.data)
            return Response({"student": data}, status=status.HTTP_200_OK)
        else:
            return Response({"student": []}, status=status.HTTP_200_OK)

    except KeyError:
        return Response(
            {
                "detail": "You should include the [search] and [searchBy] in your request body"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def getTeachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response({"teachers": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def addTeacher(request):
    username, password = generateUsernameAndPassword(request.data)
    request.data._mutable = True
    request.data.update({"username": username, "password": password})
    userSerializer = UserCreateSerializer(data=request.data)
    if not userSerializer.is_valid():
        return standardizedErrors(userSerializer)

    user = userSerializer.save()
    request.data.update({"user": user.id})
    request.data._mutable = False
    teacherSerializer = TeacherCreateSerializer(
        data=request.data,
        many=False,
    )
    if not teacherSerializer.is_valid():
        user.delete()
        return standardizedErrors(teacherSerializer)
    teacher = teacherSerializer.save()
    data = TeacherDetailSerializer(
        teacher, many=False, context={"request": request}
    ).data.copy()
    data["user"]["password"] = request.data["password"]
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(["PATCH", "PUT"])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([AllowAny])
def updateTeacher(request):
    try:
        teacher_id = request.data["id"]
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            userSerializer = UserSerializer(
                teacher.user, data=request.data, partial=True
            )
            if not userSerializer.is_valid():
                return standardizedErrors(userSerializer)
            teacherSerializer = TeacherCreateSerializer(
                teacher, data=request.data, partial=True
            )
            if not teacherSerializer.is_valid():
                return standardizedErrors(teacherSerializer)
            userSerializer.save()
            teacherSerializer.save()
            data = TeacherSerializer(teacher, many=False).data
            return Response(data, status=status.HTTP_202_ACCEPTED)
        except Teacher.DoesNotExist:
            return Response(
                {"detail": f"Teacher with id={teacher_id} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
    except KeyError:
        return Response(
            {"detail": "You should include the [id] of teacher you want to update"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteTeacher(request, pk):
    if not pk:
        return Response(
            {"detail": "You should include the [id] of teacher you want to update"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        teacher = Teacher.objects.get(id=pk)
        teacher.user.delete()
        return Response(
            {"detail": f"Teacher with id={pk} deleted successfully"},
            status=status.HTTP_202_ACCEPTED,
        )
    except Teacher.DoesNotExist:
        return Response(
            {"detail": f"Teacher with id={pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
