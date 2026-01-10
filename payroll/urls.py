from django.urls import path
from .views import (
    compensation_create_update,
    get_compensation,
    delete_compensation,
    create_payroll,
    get_all_payrolls,
    payroll_detail
)

urlpatterns = [
    # Compensation
    path('compensation/<int:employee_id>/', get_compensation),
    path('compensation/<int:employee_id>/create-update/', compensation_create_update),
    path('compensation/<int:employee_id>/delete/', delete_compensation),

    # Payroll
    path('', get_all_payrolls),
    path('create/', create_payroll),
    path('<int:id>/', payroll_detail),
]
