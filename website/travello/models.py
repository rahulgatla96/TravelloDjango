from os import name
from django.db import models
from numpy import imag

# Create your models here.

class Destination(models.Model) :
     
    name = models.CharField(max_length=100) # type: ignore
    img = models.ImageField(upload_to='pics') # type: ignore
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False) # type: ignore
