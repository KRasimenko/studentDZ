from django.urls import path
from . import views

app_name = 'taskmanager_reg'

urlpatterns = [
    path('', views.choose_role, name='choose_role'),
    path('register/', views.register, name='register'),
]