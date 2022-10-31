from django.urls import path, include
from . import views

urlpatterns = [
    path('subject/', views.subject),
    path('subject/<int:id>', views.subject),
    path('class/', views.classe),
    path('class/<int:id>', views.classe),
    path('', views.subject_class_info),
    path('<int:id>', views.subject_class_info),
    path('time-table', views.time_table),
    path('time-table/<int:id>', views.time_table),
    path('attendance/<int:cla>/<int:sub>', views.attendance)
]
