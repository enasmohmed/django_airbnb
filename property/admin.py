from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from tof.admin import TofAdmin, TranslationTabularInline

from property.models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook, \
    PropertyRoomFacilities


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'price', 'get_avg_rating', 'check_availability']


class CategoryAdmin(TofAdmin):
    # list_display = ('name')
    inlines = (TranslationTabularInline, )


admin.site.register(Property, SomeModelAdmin)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PropertyReview)
admin.site.register(PropertyRoomFacilities)


class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'now_reservation']
    

admin.site.register(PropertyBook, PropertyBookAdmin)