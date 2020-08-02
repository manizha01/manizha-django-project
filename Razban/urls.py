"""Razban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# we need to import views
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # function for home page
    #'' if it is blank go to home page
path('', views.home, name = 'home'),

path('registration/<int:client_id>/', views.client_detail, name = 'client_detail'),

path('about/' , views.about, name = 'about')
]
