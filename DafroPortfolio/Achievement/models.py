from django.db import models

# Create your models here.
class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    refrence = models.CharField(max_length=1000)
    authority = models.CharField(max_length=100)
    licenseNumber = models.CharField(max_length=100)

