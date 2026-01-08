from django.db import models
from employees.models import Employee

class Leave(models.Model):
    employee=models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    staus=models.CharField(max_length=20,default="pending")

    def __str__(self):
        return f"{self.employee.name}-{self.status}"

# Create your models here.
