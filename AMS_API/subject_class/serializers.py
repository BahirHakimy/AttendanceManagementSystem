
from rest_framework import serializers
from users.serializers import StudentSerializer
from users.models import Student
from .models import Classes, Subject

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
        print(instance.department, 'sldjfl', validated_data)
        print(validated_data.get('name') or instance.department)
        # split_department = validated_data["department"].split(' ')
        # short_department = split_department[0][0].upper() + split_department[1][0].upper()
        # date_arr = str(validated_data['class_start_date']).split('-')
        # date = date_arr[0]
        # validated_data["name"] = short_department + "-"  + date + "-" + validated_data["gender"]
        return super().update(instance, validated_data)

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

