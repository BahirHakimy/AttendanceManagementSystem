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

    def __str__(self) -> str:
        split_department = self.department.split(' ')
        short_department = split_department[0][0] + split_department[1][0]
        class_name = short_department + "-"  + self.class_start_date + "-" + self.gender
        return class_name


class Subject(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.title