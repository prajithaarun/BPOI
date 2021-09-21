from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hr,name='hr'),
    path('delete/',views.delete, name='delete')
]

