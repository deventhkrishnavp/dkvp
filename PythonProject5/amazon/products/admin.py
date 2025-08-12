from django.contrib import admin
from.models import Items


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','price','image')
admin.site.register(Items,ItemAdmin)