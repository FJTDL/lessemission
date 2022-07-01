from django.contrib import admin
from .models import CarbonScore, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CarbonScore)