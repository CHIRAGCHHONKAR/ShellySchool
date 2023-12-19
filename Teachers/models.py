from django.db import models

class teacher(models.Model):
    teacher_image=models.FileField(upload_to='teachers',default=None,null=True)
    teacher_name=models.CharField(max_length=100)
    teacher_designation=models.CharField(max_length=200)
    teacher_facebook=models.URLField(null=True,blank=True)
    teacher_linkedin=models.URLField(null=True,blank=True)
    teacher_instagram=models.URLField(null=True,blank=True)
    
    def __str__(self):
        return self.teacher_name
# Create your models here.
 
