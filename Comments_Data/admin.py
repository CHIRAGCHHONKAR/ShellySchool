from django.contrib import admin
from Comments_Data.models import comment

class comment_admin(admin.ModelAdmin):
    list_display=['name','email','website','message','date']
    
admin.site.register(comment,comment_admin)    
# Register your models here.
