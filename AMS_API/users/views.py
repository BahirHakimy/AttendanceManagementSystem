import json
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from AMS_API.users.serializers import StudentSerializer, UserSerializer

# Create your views here.

@api_view(["POST"])
def add (request):
    data = (request.data)
    data.update({'username': data['name']})
    print(data)
    serializerUser = UserSerializer(data=data)
    serializerStudent = StudentSerializer(data=data)
    if serializerUser.is_valid() and serializerStudent.is_valid():
        serializerUser.save()
        user = User.objects.get(username=serializerUser.data['username'])
        data.update({'user': user.id})
        if serializerStudent.is_valid():
            serializerStudent.save()
            return Response('', status = status.HTTP_201_CREATED)
        else:
            return Response('')
