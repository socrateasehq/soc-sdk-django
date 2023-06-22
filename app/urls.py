"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', views.index, name='home'),

    # About Us
    path('about-us', views.about_us, name='about_us'),

    # Pricing
    path('pricing', views.pricing, name='pricing'),

    # To go to Socratease home page, go to /assessments/cms/home
    re_path('assessments/*', views.socratease, name='assessments')


    ]
