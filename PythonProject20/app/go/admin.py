from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Package, Booking

admin.site.register(Package)
admin.site.register(Booking)
