from django.urls import path, include
from . import views

urlpatterns = [
    path('add-student/', views.addStudent),
    path('add-teacher/', views.addStudent),
]