from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Teacher, Teacher

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=55, required=False)
    password = serializers.CharField(min_length=8, max_length=55, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "gender",
            "first_name",
            "last_name",
            "phone",
            "age",
        ]

    #      user = {"email":"ahmad@abc.com","gender","M","first_name":"ahmad","last_name":"ahmadi","phone":"0789898989","age":"20"}
    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            gender=validated_data["gender"],
            phone=validated_data["phone"],
            age=validated_data["age"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    fullname = serializers.ReadOnlyField(source="get_full_name")
    gender = serializers.ReadOnlyField(source="get_gender_display")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "gender",
            "phone",
            "age",
            "first_name",
            "last_name",
            "fullname",
        ]


class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)
    profile_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Student
        fields = ["user", "father_name", "parent_class", "profile_pic"]


class StudentCreateSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Student
        fields = ["user", "father_name", "parent_class", "profile_pic"]


class StudentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    profile_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Student
        fields = ["user", "father_name", "parent_class", "profile_pic"]


class TeacherSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)
    degree = serializers.ReadOnlyField(source="get_degree_display")
    profile_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Teacher
        fields = ["user", "degree", "profile_pic"]


class TeacherCreateSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Teacher
        fields = ["user", "degree", "profile_pic"]


class TeacherDetailSerializer(serializers.ModelSerializer):
    degree = serializers.ReadOnlyField(source="get_degree_display")
    user = UserSerializer(many=False)
    profile_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Teacher
        fields = ["user", "degree", "profile_pic"]
