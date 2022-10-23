from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from subject_class.models import Classes

# Create your models here.

GENDER_CHOISES = (("M", "Male"), ("F", "Female"))
DEEGREES = (("BCH", "Bachelor"), ("MST", "Master"), ("PHD", "Doctorate"))


def validate_age(value):
    if len(str(value)) > 2 or len(str(value)) < 1:
        raise ValidationError("age must be between 18 to 99")


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOISES)
    age = models.IntegerField(validators=[validate_age], null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username

    def get_user_type(self):
        if self.is_staff:
            return {"role": "admin"}
        elif hasattr(self, "teacher"):
            return {"role": "teacher", "object": self.teacher}
        elif hasattr(self, "student"):
            return {"role": "student", "object": self.student}
        else:
            return {"role": "undefined"}


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=55)
    parent_class = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    degree = models.CharField(max_length=3, choices=DEEGREES)
