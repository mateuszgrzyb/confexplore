from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    class RoleName(models.TextChoices):
        NORMAL_USER = 'U', _('User')
        VOLUNTEER = 'V', _('Volunteer')
        ORGANIZER = 'O', _('Organizer')
        ADMINISTRATOR = 'A', _('Administrator')

    django_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.TextField()
    role_name = models.TextField(
        choices=RoleName.choices,
        default=RoleName.NORMAL_USER
    )

    def get_role(self):
        if self.role_name == 'U':
            return self.normaluser_role
        elif self.role_name == 'V':
            return self.volunteer_role
        elif self.role_name == 'O':
            return self.organizer_role
        elif self.role_name == 'A':
            return self.administrator_role
        else:
            raise Exception("ERROR - function profile.get_role() not working")


class Role(models.Model):
    profile = models.OneToOneField(
        Profile,
        related_name='%(class)s_role',
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


# @receiver(post_save, sender=User)
# def create_profile_hook(sender, instance: User, created, **kwargs) -> None:
#     if created:
#         profile = Profile.objects.create(django_user=instance, name=instance.username)
#         NormalUser.objects.create(profile=profile)


class NonAdmin(Role):
    blocked = models.BooleanField(default=False)

    class Meta:
        abstract = True


class NormalUser(NonAdmin):
    pass


class Organizer(NonAdmin):
    pass


class Volunteer(NonAdmin):
    pass


class Administrator(Role):
    pass
