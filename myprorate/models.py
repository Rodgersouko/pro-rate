from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
#***
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200)
    photo = ImageField(manual_crop='1280x720', blank=True, null=True)
    
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name="posts")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
