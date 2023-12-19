from django.contrib import admin
from Teachers.models import teacher

class teacher_admin(admin.ModelAdmin):
    list_display=['teacher_name','teacher_designation','teacher_linkedin','teacher_instagram','teacher_facebook','teacher_image']
    
admin.site.register(teacher,teacher_admin)    
# Register your models here.
