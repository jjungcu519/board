from django.urls import path
from . import views #.의 의미는 현재 나의 위치

urlpatterns = [
    path('', views.index),
]