from rest_framework import serializers
from users.serializers import TeacherSerializer, StudentSerializer
from users.models import Student
from .models import Attendance, Classes, Subject, SubjectClassTeacherInfo, TimeTable

class ClassesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10, read_only=True)
    class Meta: 
        model = Classes
        fields = ['id', 'name', 'floor', 'semester', 'department', 'room_no', 'class_start_date', 'gender']
        read_only_fields = ('name',)

    def create(self, validated_data):
        split_department = validated_data["department"].split(' ')
        short_department = split_department[0][0].upper() + split_department[1][0].upper()
        date_arr = str(validated_data['class_start_date']).split('-')
        date = date_arr[0]
        validated_data["name"] = short_department + "-"  + date + "-" + validated_data["gender"]
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.floor = validated_data.get('floor') or instance.floor
        instance.semester = validated_data.get('semester') or instance.semester
        instance.department = validated_data.get('department') or instance.department
        instance.room_no = validated_data.get('room_no') or instance.room_no
        instance.class_start_date = validated_data.get('class_start_date') or instance.class_start_date
        instance.gender = validated_data.get('gender') or instance.gender
        split_department = instance.department.split(' ')
        short_department = split_department[0][0].upper() + split_department[1][0].upper()
        date_arr = str(instance.class_start_date).split('-')
        date = date_arr[0]
        instance.name = short_department + "-"  + date + "-" + instance.gender
        return super().update(instance, validated_data)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']
        read_only_fields = ['id']

class ClassBelongsSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    def get_students(self, classes):
        queryset = Student.objects.filter(parent_class=classes.id)
        serializer = StudentSerializer(queryset, many=True)
        return serializer.data
    
    class Meta:
        model = Classes
        fields = ['id', 'name', 'floor', 'semester', 'department', 'room_no', 'class_start_date', 'gender', 'students']
        read_only_fields = ['id', 'students']


class InfoSerializer(serializers.ModelSerializer):   
    # classes = ClassesSerializer()
    # subject = SubjectSerializer()
    # teacher = TeacherSerializer()

    class Meta:
        model = SubjectClassTeacherInfo
        fields = ['id', 'classes', 'subject', 'teacher']
        read_only_fields = ['id']


class TimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeTable
        fields = ['id', 'subject_class_teacher_info', 'day_of_week', 'cridet']

class GetAttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'subject_class_teacher_info', 'isPresent', 'date', 'cridet']


class PostAttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'subject_class_teacher_info', 'isPresent', 'date', 'cridet']

