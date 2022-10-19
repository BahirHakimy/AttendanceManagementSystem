from random import choices
from django.db import models
from django.contrib.auth.models import User

from subject_class.models import Classes

# Create your models here.

GENDER_CHOISES = (("M", "M"), ("F", "F"))
DEEGREES = (("Master", "Master", "Bachelor", "Bachelor"))

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOISES)
    birth = models.DateField()
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(max_length= 20)
    father_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOISES)
    birth = models.DateField()
    degree = models.CharField(max_length=20, choices=DEEGREES)
