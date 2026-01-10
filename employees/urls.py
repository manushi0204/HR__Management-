from django.urls import path
from .views import create_employee,get_all_employees,get_employee_by_id

urlpatterns = [
    path('create/', create_employee),
    path('', get_all_employees),
    path('<int:id>/', get_employee_by_id),
]
