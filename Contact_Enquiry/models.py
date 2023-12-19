from django.db import models


class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    
    
# Create your models here.
