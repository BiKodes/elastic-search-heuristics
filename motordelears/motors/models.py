from django.db import models
from motors.constants import TYPE_OF_CARS

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_OF_CARS)