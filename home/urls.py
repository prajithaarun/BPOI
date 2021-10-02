from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'home'


urlpatterns = [
    path('',views.home,name='home'),
    path('insert/',views.insert, name='insert'),
    path('display/',views.display,name='display'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:pk>', views.update, name='update'),
]