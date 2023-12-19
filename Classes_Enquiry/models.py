from django.db import models

class ClassesEnquiry(models.Model):
    CLASS_CHOICES = (
        ('Hospitality, Leisure & Sports Courses', 'Hospitality, Leisure & Sports Courses'),
        ('Environmental Studies & Earth Sciences', 'Environmental Studies & Earth Sciences'),
        ('Natural Sciences & Mathematics Courses', 'Natural Sciences & Mathematics Courses'),
        ('Basic English Speaking and Grammar', 'Basic English Speaking and Grammar'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    Classes = models.CharField(choices=CLASS_CHOICES, max_length=100, null=True,)
    message = models.TextField()


# Create your models here.
