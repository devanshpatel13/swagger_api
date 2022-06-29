from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    std = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subj = models.CharField(max_length=100)
    phone = models.IntegerField()
