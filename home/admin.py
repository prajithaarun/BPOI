from django.contrib import admin
from .models import student
from .models import employee

class studentAdmin(admin.ModelAdmin):
    list_display = ('name','mark','subject')
admin.site.register(student)

class employeeAdmin(admin.ModelAdmin):
    list_display = ('name','salary','company')
admin.site.register(employee)

