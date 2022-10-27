from django.contrib import admin

from .models import Attendance, Classes, Subject, SubjectClassTeacherInfo, TimeTable

# Register your models here.

admin.site.register(Classes)
admin.site.register(Subject)
admin.site.register(SubjectClassTeacherInfo)
admin.site.register(Attendance)
admin.site.register(TimeTable)
