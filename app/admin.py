from django.contrib import admin
from .models import LineModel,LineSettingsModel
# Register your models here.

admin.site.register(LineModel)
admin.site.register(LineSettingsModel)