
from datetime import datetime
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.


class Customer(models.Model):
    # id = models.AutoField()
    first_name = models.CharField(max_length=15, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    registration_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['first_name']  # ascending order
        # ordering = [-'first_name'] descending order
        verbose_name = 'Register Customer'
        # verbose_name_plural = 'Customer'

    def __str__(self):
        # f helps to format your string into any format
        return f"{self.pk} {self.first_name} {self.last_name}"

    def get_year_of_birth(self):
        year = datetime.today().year
        yob = int(year) - int(self.age)
        return yob


class BankAccount(models.Model):
    # account_name = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, unique=True)
    account_number = models.PositiveIntegerField(max_length=10)

    def __str__(self):
        return self.account_number
