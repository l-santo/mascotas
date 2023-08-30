
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.about, name="about"),
    path('category/<int:categoryId>/', views.category, name="category")
]
