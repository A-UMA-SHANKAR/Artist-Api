# artist_app/models.py

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    identityNumber = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


# The absolute path to get the url then reverse into 'student_edit' with keyword arguments (kwargs) primary key
    def get_absolute_url(self):
        return reverse('student_edit', kwargs={'pk': self.pk})



class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('Other', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=LINK_TYPES)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work = models.ManyToManyField(Work)

# Signal to create an Artist object after each User registration
@receiver(post_save, sender=User)
def create_artist_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'artist'):
        Artist.objects.create(user=instance, name=instance.username)

# Signal to save the Artist object after each User update
@receiver(post_save, sender=User)
def save_artist_profile(sender, instance, **kwargs):
    if hasattr(instance, 'artist'):
        instance.artist.save()
