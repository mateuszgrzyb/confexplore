from django.db import models

# Create your models here.
from users.models import User


class Event(models.Model):
    class Schedule(models.Model):
        event = models.ForeignKey('Event', on_delete=models.CASCADE)
        date = models.DateTimeField()

    name = models.TextField()
    info = models.TextField(blank=True)


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    owner = models.ManyToManyField(User, blank=True, related_name='tickets')
