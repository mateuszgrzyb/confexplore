from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    django_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        abstract = True


@receiver(post_save, sender=DjangoUser)
def create_profile_hook(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)


class User(Profile):
    blocked = models.BooleanField(default=False)


class Organizer(User):
    pass


class Volunteer(User):
    pass


class Administrator(Profile):
    pass
