from django.db import models
from department.models import Department 
from users.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    hire_date=models.DateField()
    department=models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )

    def __str__(self):
        return  self.name