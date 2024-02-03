from django.db import models
from motors.constants import TYPE_OF_CARS
from django import datetime

class Manufacturer(models.Model):
    name = models.CharField(max_length=155)
    country_code = models.CharField(max_length=5)
    created = models.DateTimeField()


class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer')
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_OF_CARS)
    year = models.IntegerField(default=datetime.datetime.today().year)

    class Meta:
        ordering = ['year']
        unique_together = ("year", "type")
        verbose_name_plural = "cars"

    def type_to_string(self):
        """Convert the type field to its string representation
        (the boneheaded way).
        """
        if self.type == 1:
            return "Audi Q5"
        elif self.type == 2:
            return "Audi Q8"
        elif self.type == 3:
            return "Audi RS7"
        elif self.type == 4:
            return "Truck"
        else:
            return "Audi Q5"

    def __str__(self):
        return f' {self.name} {self.year}'

class Advert(models.Model):
    title = models.CharField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    url = models.URLField()
    car = models.ForeignKey('Car', related_name='adverts')