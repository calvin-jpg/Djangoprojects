"""cmis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from customer.views import CustomerCreateView, CustomerDetailView,CustomerDeleteView, get_customer_list, CustomerListView,CustomerUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('customer/list', get_customer_list, name='customer-list'),
    path('customer/list', CustomerListView.as_view(), name='customer-list'),
    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer/detail/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/update/<int:pk>', CustomerUpdateView.as_view(), name='customer_update'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)