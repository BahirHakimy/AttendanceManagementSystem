from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Teacher

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['user', 'email', 'password']

    def create(self, validated_data):
        return super().create(validated_data)

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['user', 'name', 'father_name', 'birth', 'gender', 'classes']
    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teacher
        fields = ['user', 'name', 'father_name', 'birth', 'gender', 'degree']


