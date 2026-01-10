from django.db import models
from employees.models import Employee


class Training(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    training_name = models.CharField(max_length=100)
    description=models.TextField(default="none")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
         choices=[
            ('ONGOING', 'Ongoing'),
            ('COMPLETED', 'Completed'),
        ]
    
    )

    def __str__(self):
        return f"{self.employee.name} - {self.training_name}"
