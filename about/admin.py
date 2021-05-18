from django.contrib import admin

# Register your models here.
from about.models import About, FAQ

admin.site.register(About)
admin.site.register(FAQ)