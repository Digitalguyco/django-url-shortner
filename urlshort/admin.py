from django.contrib import admin
from .models import Url

# Register your models here.

# UrlAdmin to Manage list Displays
class UrlAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'link','user'] # Would Display uuid, link and and the user(username of the user)

# Register  Url Model
admin.site.register(Url, UrlAdmin)