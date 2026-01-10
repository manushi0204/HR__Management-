from django.urls import path
from .views import create_department, get_all_departments, department_detail

urlpatterns = [
    path('', get_all_departments),
    path('create/', create_department),
    path('<int:id>/', department_detail),
]
