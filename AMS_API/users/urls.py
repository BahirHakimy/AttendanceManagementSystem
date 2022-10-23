from django.urls import path, include
from . import views

urlpatterns = [
    path("get-user/", views.getUser),
    path("get-students/", views.getStudents),
    path("add-student/", views.addStudent),
    path("update-student/", views.updateStudent),
    path("search-student/", views.searchStudent),
    path("delete-student/<int:pk>", views.deleteStudent),
    path("get-teachers/", views.getTeachers),
    path("add-teacher/", views.addTeacher),
    path("update-teacher/", views.updateTeacher),
    path("delete-teacher/<int:pk>", views.addTeacher),
]
