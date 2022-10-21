from django.db import models

# Create your models here.
GENDER_CHOISES = (("M", "M"), ("F", "F"), ("B", "Both"))

class Classes(models.Model):
    name = models.CharField(max_length=20, unique=True)
    floor = models.IntegerField()
    semester = models.IntegerField()
    department = models.CharField(max_length=25)
    room_no = models.IntegerField()
    class_start_date = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOISES)


class Subject(models.Model):
    title = models.CharField(max_length=35)