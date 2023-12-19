from django.db import models
from django.utils import timezone

class Event(models.Model):
    datetime=models.CharField(max_length=50)
    Eventprice=models.CharField(max_length=50)
    eventname=models.CharField(max_length=100)
    teacherimage=models.FileField(upload_to='Events',default=None,null=True)
    teachername=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
# Create your models here.
