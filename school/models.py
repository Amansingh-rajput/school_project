from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Standard(models.Model):
    standard_name= models.CharField(max_length=100)
  