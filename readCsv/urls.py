from django.urls import path
from . import views
from .models import Student
urlpatterns = [

    path('', views.home, name='home'),
] 
