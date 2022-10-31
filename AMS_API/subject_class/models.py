from random import choices
from django.db import models

# Create your models here.
GENDER_CHOISES = (("M", "M"), ("F", "F"), ("B", "Both"))
CRIDET_CHOISES = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"))
WEEK_DAYS = (
    ("5", "Saturday"),
    ("6", "Sunday"),
    ("0", "Monday"),
    ("1", "Tuesday"),
    ("2", "Wednesday"),
    ("3", "Thursday"),
)


class Classes(models.Model):
    name = models.CharField(max_length=20, unique=True)
    floor = models.IntegerField()
    semester = models.IntegerField()
    department = models.CharField(max_length=25)
    room_no = models.IntegerField()
    class_start_date = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOISES)

    def __str__(self) -> str:
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.title


class SubjectClassTeacherInfo(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.classes.name + "-" + self.subject.title + "$" + self.teacher.user.get_full_name()


class Attendance(models.Model):
    student = models.ForeignKey("users.Student", on_delete=models.CASCADE)
    subject_class_teacher_info = models.ForeignKey(
        SubjectClassTeacherInfo, on_delete=models.CASCADE
    )
    isPresent = models.BooleanField()
    date = models.DateField()
    cridet = models.IntegerField(choices=CRIDET_CHOISES)

    def __str__(self) -> str:
        return super().__str__()


class TimeTable(models.Model):
    subject_class_teacher_info = models.ForeignKey(
        SubjectClassTeacherInfo, on_delete=models.CASCADE
    )
    day_of_week = models.CharField(max_length=1, choices=WEEK_DAYS)
    cridet = models.IntegerField(choices=CRIDET_CHOISES)
