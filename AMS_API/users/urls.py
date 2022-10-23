from django.urls import path, include
from . import views

urlpatterns = [
    path("get-students/", views.getStudents),
    path("add-student/", views.addStudent),
    path("update-student/", views.updateStudent),
    path("delete-student/<int:pk>", views.deleteStudent),
    path("add-teacher/", views.addStudent),
]
