from django.shortcuts import render
from http.client import HTTPResponse
from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from customer.models import Customer


# Create your views here.
def get_customer_list(request):
    customer = Customer.objects.all()
    return HTTPResponse(request, {'customer': customer})


class CustomerListView(ListView):
    queryset = Customer.objects.all()
    template_name = 'customer/customer_list.html'
    context_object_name = 'customer'



class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer/customer_create.html'
    #context_object_name = 'customer'
    fields = ['first_name', 'middle_name', 'last_name', 'age']
    success_url = '/customer/list'



class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_details.html'
    # context_object_name = 'cst'
    #context_object_name = 'customer'
    fields = ['first_name', 'middle_name', 'last_name', 'age']
    success_url = '/customer/list'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer/customer_update.html'
    #context_object_name = 'customer'
    fields = ['first_name', 'middle_name', 'last_name', 'age']
    success_url = '/customer/list'


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    # fields = ['first_name, middle_name, last_name, age']
    success_url = '/customer/list'
