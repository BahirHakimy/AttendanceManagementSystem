from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
GENDERS = (("M", "Male"), ("FM", "Female"))
DEGREES = (("BC", "Bachelor"), ("MS", "Master"), ("PHD", "Doctorate"))
DEPARTMENTS = (
    ("IT", "InformationTechnology"),
    ("SE", "SoftwareEngineering"),
    ("IS", "InformationSystems"),
)
SEMESTERS = (
    ("1st", "First"),
    ("2nd", "Second"),
    ("3rd", "Third"),
    ("4th", "Forth"),
    ("5th", "Fifth"),
    ("6th", "Sixth"),
    ("7th", "Seventh"),
    ("8th", "Eighth"),
)


def validate_age(value):
    if len(str(value)) > 2:
        raise ValidationError("age must be maximum 2 digits")


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=GENDERS)
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


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    degree = models.CharField(max_length=3, choices=DEGREES)

    def __str__(self) -> str:
        return self.user.get_full_name()


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_class = models.ForeignKey("Class", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.get_full_name()


class Class(models.Model):
    department = models.CharField(max_length=2, choices=DEPARTMENTS)
    semester = models.CharField(max_length=3, choices=SEMESTERS)
    room_no = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"{self.semester} Semester {self.department}"


class Subject(models.Model):
    title = models.CharField(max_length=55)
    classes = models.ManyToManyField(Class)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.title

    def get_classes_for_teacher(self, teacher):
        return Subject.objects.filter(title=self.title, teachers__id=teacher.id)[
            0
        ].classes.all()


class AttendanceForm(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    parent_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    is_locked = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.subject} {self.parent_class}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    form = models.ForeignKey(AttendanceForm, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.student} {self.date} {self.is_present}"
