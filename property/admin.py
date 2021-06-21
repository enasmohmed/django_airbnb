from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from property.models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook, PropertyRoomFacilities


class PropertyInline(admin.TabularInline):
    model = PropertyImages
    fields = ['image']


class PropertyAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'price', 'avaregereview', 'check_availability']
    inlines = [PropertyInline]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyRoomFacilities)


class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'now_reservation']


admin.site.register(PropertyBook, PropertyBookAdmin)