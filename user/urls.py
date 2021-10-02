from django.urls import path, include
from . import views

app_name = 'restapi'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register_view,name='register'),
]