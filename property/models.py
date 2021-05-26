from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)
       super(Property, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={"slug": self.slug})
    

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return str(self.property)


class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PropertyReview(models.Model):
    author = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.property)


COUNT = (
    (1 , 1),
    (2 , 2),
    (3 , 3),
    (4 , 4),
)


class PropertyBook(models.Model):
    user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.IntegerField(choices=COUNT)
    children = models.IntegerField(choices=COUNT)

    def __str__(self):
        return str(self.property)
