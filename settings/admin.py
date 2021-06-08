from django.contrib import admin

# Register your models here.
from settings.models import Settings, NewsLetter, Services

admin.site.register(Settings)
admin.site.register(NewsLetter)
admin.site.register(Services)