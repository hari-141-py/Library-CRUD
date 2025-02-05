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
from books import views

app_name = "books"

urlpatterns = [
    path('book_view',views.book_view,name='book_view'),
    path('add_book',views.add_book,name='add_book'),
    path('edit_book/<int:i>',views.edit_book,name='edit_book'),
    path('delete_book/<int:d>',views.delete_book,name='delete_book'),
    path('search_book',views.search_book,name='search_book')
]
