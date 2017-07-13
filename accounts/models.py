from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address1 = models.CharField(max_length=255, default='', blank=True)
    address2 = models.CharField(max_length=255, default='',blank=True)
    postcode = models.CharField(max_length=7, default='',blank=True)
    phone = models.CharField(max_length=10, default='',blank=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='',blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class KidProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    parent = models.ForeignKey(User, related_name='kids')
    name = models.CharField(max_length=255, default='', blank=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='',blank=True)

    def __str__ (self):
        return self.name