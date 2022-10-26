from django.urls import path, include
from . import views

urlpatterns = [
    path('add-subject/', views.subject),
    path('add-subject/<int:id>', views.subject)
]
