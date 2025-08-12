from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Invoice, InvoiceItem

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)


from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

admin.site.register(Product)
