from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from property.models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'price', 'get_avg_rating', 'check_availability']


admin.site.register(Property, SomeModelAdmin)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)


class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'now_reservation']
    

admin.site.register(PropertyBook, PropertyBookAdmin)