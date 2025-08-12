from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Optional: Your custom manager to filter only top packages
class PackageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_top=True)


class Package(models.Model):
    img = models.ImageField(upload_to='pic/')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=22)
    desc = models.TextField(max_length=100)
    price = models.PositiveIntegerField()
    destination = models.CharField(max_length=18)
    is_top = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    expiry_date = models.DateField(null=True, blank=True)

    # Use your custom manager
    objects = PackageManager()

    def __str__(self):
        return self.name


class Booking(models.Model):
    cus_name = models.CharField(max_length=13)
    cus_phn = models.BigIntegerField()
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.cus_name}-{self.cus_phn}"

