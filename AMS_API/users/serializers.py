from random import random, choice
import string
from math import floor
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Teacher

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data["first_name"] = validated_data['username']
        a = ''.join(str(x) for x in [floor(random() * 10) for i in range(0, floor(random() * 3 + 2))])
        b = ''.join(choice(string.ascii_letters))
        validated_data['username'] = validated_data['username']+a+b
        return super().create(validated_data)



class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['user', 'name', 'father_name', 'birth', 'gender', 'classes']
    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teacher
        fields = ['user', 'name', 'father_name', 'birth', 'gender', 'degree']


