from django.contrib import admin

# Register your models here.
from property.models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook

admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)