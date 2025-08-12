from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=678)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=678)