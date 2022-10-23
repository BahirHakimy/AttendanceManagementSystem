from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from .serializers import StudentSerializer, UserSerializer

# Create your views here.

# The add Student should return 
{
    "data": {
        "class": {
            "name": "String",
            "floor": "int",
            "semester": "int",
            "department": "String",
            "room_no": "int"
        },
        "user": {
            "username": "String",
            "email": "unique -email",
            "first_name": "alpha String",
            "father_name": "alpha String",
            "gender": "M or F",
            "birth": "DD-MM-YYYY",
            "phone": "unique-phone",
            "password": "String"
        }
    }
}
# for above data the every student should be in class
# so add the class data or view first


@api_view(["POST"])
def addStudent(request):
    data = (request.data)
    data.update({'username': data['name']})
    serializerUser = UserSerializer(data=data)
    serializerStudent = StudentSerializer(data=data)
    if serializerUser.is_valid() and serializerStudent.is_valid() or serializerStudent.errors.keys().__len__() == 1 and serializerStudent.errors.keys().__contains__('user'):
        password = serializerUser.validated_data.get('password')
        serializerUser.validated_data['password']=make_password(password)
        instance = serializerUser.save()
        user = instance.id
        data.update({'user': user})
        serializerStudent1 = StudentSerializer(data=data)
        if serializerStudent1.is_valid():
            serializerStudent1.save()
            return Response(serializerStudent1.data, status = status.HTTP_201_CREATED)
        else:
            return Response({"error": serializerStudent1.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": serializerStudent.errors}, status=status.HTTP_400_BAD_REQUEST)
