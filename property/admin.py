from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from property.models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Property, SomeModelAdmin)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)