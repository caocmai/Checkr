from django.contrib import admin

from home.models import NasaImage, Rating

# Register your models here.

admin.site.register(NasaImage)
admin.site.register(Rating)