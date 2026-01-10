from django.urls import path
from .views import create_attendance,get_all_attendance,attendance_detail

urlpatterns = [
    path('',get_all_attendance),
    path('create/',create_attendance),
    path('<int:id>/',attendance_detail),
]
