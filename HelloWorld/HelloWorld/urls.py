"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import include, re_path
from . import views,testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/',views.index),
    re_path('index1/',views.index1),
    re_path(r'db/add$',testdb.add),
    re_path(r'db/get',testdb.get_all),
    re_path(r'db/update$',testdb.update),
    re_path(r'db/delete$',testdb.delete),
]
