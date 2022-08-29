from django.contrib import admin
from customer.models import Customer, BankAccount


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']


admin.site.register(Customer)
admin.site.register(BankAccount)
