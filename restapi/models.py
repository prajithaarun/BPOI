from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    mark = models.IntegerField()
    college = models.CharField(max_length=200)
