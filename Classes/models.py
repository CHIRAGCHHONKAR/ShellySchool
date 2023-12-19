from django.db import models

class classes(models.Model):
    classimage=models.FileField(upload_to='classes/class',default=None,null=True)
    classtitle=models.CharField(max_length=1000)
    classtime=models.CharField(max_length=500)
    classteacherimage=models.FileField(upload_to='classes/teacher',default=None,null=True)
    classteachername=models.CharField(max_length=50)
    classprice=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.classtitle

# Create your models here.
