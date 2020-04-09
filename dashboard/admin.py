from django.contrib import admin
from .models import control
from isplcAPI.models import devices
# Register your models here.

admin.site.register(control)
admin.site.register(devices)
