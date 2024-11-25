"""
URL configuration for Library_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from users import views

app_name = "users"

urlpatterns = [
    path('',views.home,name='home'),
    path('user_login',views.user_login,name='user_login'),
    path('user_register',views.user_register,name='user_register'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('view_users',views.view_users,name='view_users'),
    path('edit_user/<int:i>',views.edit_user,name='edit_user'),
    path('delete_user/<int:d>',views.delete_user,name='delete_user'),
    path('user_logout',views.user_logout,name='user_logout'),
]
