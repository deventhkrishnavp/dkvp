from django.db import models

class Student(models.Model):
    sid=models.CharField(max_length=34)
    sname=models.CharField(max_length=34)
    scontact=models.IntegerField(max_length=23)







