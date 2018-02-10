from django.db import models

# Create your models here.
# Django will create a primarykey by default behind the scenes
class Projects(models.Model) :
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    role = models.CharField(max_length=1000)
    projectLogo = models.CharField(max_length=1000)
    refrence = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)
    
    
