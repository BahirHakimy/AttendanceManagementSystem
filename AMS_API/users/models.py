from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from subject_class.models import Classes

# Create your models here.

GENDER_CHOISES = (("M", "M"), ("F", "F"))
DEEGREES = (("Master", "Master"), ("Bachelor", "Bachelor"))

def validate_age(value):
    if len(str(value)) > 2:
        raise ValidationError("age must be maximum 2 digits")


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOISES)
    age = models.IntegerField(validators=[validate_age], null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    REQUIRED_FIELDS = ["email"]

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOISES)
    birth = models.DateField()
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length= 20)
    father_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOISES)
    birth = models.DateField()
    degree = models.CharField(max_length=20, choices=DEEGREES)
