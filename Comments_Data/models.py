from django.db import models



class comment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    website=models.URLField()
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
# Create your models here.
