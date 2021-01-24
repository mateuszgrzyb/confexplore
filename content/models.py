from django.db import models

# Create your models here.
from users.models import NormalUser





class City(models.Model):
    name = models.CharField(max_length=50, default='Warszawa')

class Type(models.Model):
    name = models.CharField(max_length=100, default='Ogólna')

class Event(models.Model):
    #    class Schedule(models.Model):
    #        event = models.ForeignKey('Event', on_delete=models.CASCADE)
    #        date = models.DateTimeField()

    name = models.CharField(max_length=100, default='konferencja')
    info = models.TextField(blank=True)
    localization = models.ForeignKey('City', on_delete=models.CASCADE, default="Warszawa")
    type = models.ForeignKey('Type', on_delete=models.CASCADE, default="Ogólna")
    date = models.CharField(max_length=30, default='1 stycznia')

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    owner = models.ManyToManyField(NormalUser, blank=True, related_name='tickets')
