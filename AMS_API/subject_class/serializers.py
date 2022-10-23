from rest_framework import serializers

from .models import Classes

class ClassesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Classes
        fields = ['floor', 'semester', 'department', 'room_no', 'class_start_date', 'gender']

    def create(self, validated_data):
        split_department = validated_data["department"].split(' ')
        short_department = split_department[0][0] + split_department[1][0]
        validated_data["name"] = short_department + "-"  + validated_data["class_start_date"] + "-" + validated_data["gender"]
        return super().create(validated_data)

