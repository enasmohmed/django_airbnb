from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post, Category


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class CategoryAdmin(TofAdmin):
    list_display = ('id', 'name')
    inlines = (TranslationTabularInline, )


admin.site.register(Post, SomeModelAdmin)

admin.site.register(Category, CategoryAdmin)