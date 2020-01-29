from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import gettext_lazy as _


from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    mobile = models.CharField(verbose_name=_('Mobile Number'), max_length=150,
                              unique=True, blank=True, null=True)
    address = models.TextField(verbose_name=_("Address"),blank=True, null=True)
    dob = models.DateField(verbose_name=_("Date of Birth"),null=True, blank=True)
    city = models.CharField(verbose_name=_("City"), max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name=_("Country"), max_length=50, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

# class Profile(models.Model):
#     user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, unique=True)
    

#     def __str__(self):
#         return self.user.username

#     # @property
#     # def user_email(self):
#     #     return self.user.

# @receiver(post_save, sender=AbstractUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=AbstractUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()