from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Property(models.Model):
    owner = models.ForeignKey(User, related_name="property_owner", on_delete=models.CASCADE)
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

    def check_availability(self):
        all_reservations = self.book_property.all()
        now = timezone.now().date()

        for reservation in all_reservations:
            if now > reservation.date_to:
                return 'Availability'

            elif now > reservation.date_from and now < reservation.date_to :
                reserved_to = reservation.date_to
                return f'Now Reservation {reserved_to}'

        else:
            return 'Availability'

    def get_avg_rating(self):
        all_reviews = self.review_property.all()
        all_rating = 0

        if len(all_reviews) > 0 :
            for review in all_reviews:
                all_rating += review.rate
            return round(all_rating/len(all_reviews),2)
        else:
            return '-'
    

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
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ])



    def __str__(self):
        return str(self.property)


COUNT = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
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


    def now_reservation(self):
        now = timezone.now().date()
        return now > self.date_from and now < self.date_to

    now_reservation.boolean = True


OPTIONS_CHOICES = (
    ("World Class", " World Class"),
    ("sweetened", " sweetened"),
)


class PropertyRoomFacilities(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30)
    image = models.ImageField(upload_to='property_room_fac_images/')
    description = models.TextField(max_length=10000)
    option_service = models.CharField(max_length=20, choices=OPTIONS_CHOICES)
    service_hours_date_from = models.TimeField(default=timezone.now)
    service_hours_date_to = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name