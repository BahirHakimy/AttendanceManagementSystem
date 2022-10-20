from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    CustomUser,
    Student,
    Teacher,
    Subject,
    Class,
    AttendanceForm,
    Attendance,
    TimeTable,
    DailyTimeTable,
    TimeTableObject,
)


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "phone", "age")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(AttendanceForm)
admin.site.register(Attendance)
admin.site.register(TimeTable)
admin.site.register(DailyTimeTable)
admin.site.register(TimeTableObject)
admin.site.unregister(Group)
