from django.db import models

class student(models.Model):
    name = models.CharField(max_length=300)
    mark = models.IntegerField()
    subject =models.CharField(max_length=200)


class employee(models.Model):
    name = models.CharField(max_length=300)
    salary = models.IntegerField()
    company =models.CharField(max_length=200)
