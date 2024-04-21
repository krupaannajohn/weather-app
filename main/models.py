from django.db import models

# Create your models here.

class Weather(models.Model):
    city=models.CharField(max_length=100)
    country_code=models.CharField(max_length=3)
    coordinate = models.CharField(max_length=10)
    temp = models.CharField(max_length=10)
    pressure = models.CharField(max_length=10)
    humidity=models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
