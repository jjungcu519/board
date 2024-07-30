from django.urls import path
from . import views #.의 의미는 현재 나의 위치

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
]