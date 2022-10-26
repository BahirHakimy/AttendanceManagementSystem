from rest_framework import serializers
from users.serializers import StudentSerializer
from users.models import Student
from .models import Classes, Subject

class ClassesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Classes
        fields = ['id', 'floor', 'semester', 'department', 'room_no', 'class_start_date', 'gender']

    def create(self, validated_data):
        split_department = validated_data["department"].split(' ')
        short_department = split_department[0][0] + split_department[1][0]
        date = str(validated_data['date']).split('-')[0]
        validated_data["name"] = short_department + "-"  + date + "-" + validated_data["gender"]
        return super().create(validated_data)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title']

class ClassBelongsSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    def get_students(self, classes):
        queryset = Student.objects.filter(parent_class=classes.id)
        serializer = StudentSerializer(queryset, many=True)
        return serializer.data
    
    class Meta:
        model = Classes
        fields = ['id', 'floor', 'semester', 'department', 'room_no', 'class_start_date', 'gender', 'students']
        read_only_fields = ['id', 'students']

