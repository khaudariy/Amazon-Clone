from django.contrib import admin

# Register your models here.
from .models import Settings,Delivery




admin.site.register(Settings)
admin.site.register(Delivery)