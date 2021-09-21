from django.contrib import admin
from .models import student

class studentAdmin(admin.ModelAdmin):
    list_display = ('name','subject','mark','subject')
admin.site.register(student)
