"""lzq_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from view import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('classes/', views.classes),
    url('edit_class/', views.edit_class),
    url('add_class/', views.add_class),
    url('del_class/', views.del_class),
    url('student/', views.student),
    url('add_sts/', views.add_student),
    url('del_sts/', views.del_student),
    url('teachers/', views.teachers),
]
