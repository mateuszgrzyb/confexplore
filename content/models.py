from django.db import models


# Create your models here.
from users.models import User


class Event(models.Model):
    class Information(models.Model):
        pass

    class Schedule(models.Model):
        pass

    info = models.OneToOneField(Information, on_delete=models.CASCADE)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    owner = models.ManyToManyField(User, blank=True, related_name='tickets')
