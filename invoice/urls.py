"""invoice URL Configuration

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
from invoiceapp.views import dashboard,add_collection,manage_bills,add_bills
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard,name='dashboard'),
    path('collection/<pk>',add_collection,name='add_collection'),
    path('manage-bills',manage_bills,name='manage_bills'),
    path('add-bills',add_bills,name='add_bills'),
]
