from enum import unique
from django.db import models
from users.models import GENDER_CHOISES

# Create your models here.

class Classes(models.Model):
    name = models.CharField(max_length=20, unique=True)
    floor = models.IntegerField()
    semester = models.IntegerField()
    department = models.CharField(max_length=25)
    room_no = models.IntegerField()
    class_start_date = models.DateField()
    gender = models.CharField(GENDER_CHOISES, max_length='1', blank=True)


class Subject(models.Model):
    title = models.CharField(max_length=35)
