from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'restapi'

urlpatterns = [
    path('', views.restapi, name='restapi'),
    path('student_list/',views.student_list,name='student_list'),
    path('student_detail/<int:pk>',views.student_detail,name='student_detail')
]