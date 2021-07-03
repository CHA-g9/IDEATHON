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
# from cathome.views import *
from scheduleapp.views import *
from shoppingapp.views import *
from accountapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', base, name="home"),
    path('schedule/', schedule_home, name="schedule"),
    path('new_schedule/', new_schedule, name = "new"),
    path('create_schedule/', create_schedule, name = "create"),
    path('edit/<str:id>', edit_schedule, name = "edit"),
    path('update/<str:id>', update_schedule, name = 'update'),
    path('detail_schedules/<event_date>', show_schedule, name = "detail"),
    path('delete/<str:id>', delete, name = "delete"),

    path('shopping/', shop, name = 'shopping'),

    path('account_book/', account_book, name = "account_book"),

    path('', start1, name="start1"),
    path('start1/', start1, name="start1"),
    path('start2/', start2, name="start2"),
    path('login/', login, name="login"),
    path('signin/', signin, name="signin"),
    path('start1/signin/', signin, name="signin"),
    path('CAT_HOME/', CAT_HOME, name="CAT_HOME"),
]
