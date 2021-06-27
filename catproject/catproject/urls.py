"""catproject URL Configuration

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
from cathome.views import base
from scheduleapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name="home"),
    path('schedule/', schedule_home, name="schedule"),
    path('new_schedule/', new_schedule, name = "new"),
    path('create_schedule/', create_schedule, name = "create"),
    path('edit/<str:id>', edit_schedule, name = "edit"),
    path('update/<str:id>', update_schedule, name = 'update'),
]
