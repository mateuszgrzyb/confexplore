from django.db import models

# Create your models here.
from users.models import NormalUser
from users.models import Organizer


class City(models.Model):
    name = models.CharField(max_length=50, default='Warszawa')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, default='Ogólna')

    def __str__(self):
        return self.name


class Event(models.Model):
    #    class Schedule(models.Model):
    #        event = models.ForeignKey('Event', on_delete=models.CASCADE)
    #        date = models.DateTimeField()

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='konferencja')
    info = models.TextField(blank=True)
    localization = models.ForeignKey('City', on_delete=models.CASCADE, default="Warszawa")
    type = models.ForeignKey('Type', on_delete=models.CASCADE, default="Ogólna")
    date = models.CharField(max_length=30, default='1 stycznia')
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='images/', default='default.jpg')
    schedule = models.FileField(upload_to='schedule/', default='default.pdf')
    accepted = models.BooleanField(default=False)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    owner = models.ManyToManyField(NormalUser, blank=True, related_name='tickets')
