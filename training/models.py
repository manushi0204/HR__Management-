from django.db import models
from employees.models import Employee


class Training(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    training_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.training_name
