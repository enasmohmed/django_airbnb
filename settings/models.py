from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings_logo/')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=300)
    facebook_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)
    linkedin_link = models.URLField(max_length=200)

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse("Settings_detail", kwargs={"pk": self.pk})


class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Services(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=30)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
