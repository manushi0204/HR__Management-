from django.db import models
from employees.models import Employee

class Compensation(models.Model):
    employee=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE
    )
    basic_salary=models.FloatField()
    hra=models.FloatField()
    allowance=models.FloatField()
    deduction=models.FloatField()
    bonus=models.FloatField(default=0)

    def __str__(self):
        return self.employee.name


# Create your models here.
class Payroll(models.Model):
    employee=models.ForeignKey(
        Employee,on_delete=models.CASCADE
    )

    month=models.CharField(max_length=20)
    year=models.IntegerField()
    net_salary=models.FloatField()
    generated_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.employee.name} - {self.month}/{self.year}"

