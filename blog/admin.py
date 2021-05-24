from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post, Category


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post, SomeModelAdmin)
admin.site.register(Category)