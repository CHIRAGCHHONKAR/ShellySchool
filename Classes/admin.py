from django.contrib import admin
from Classes.models import classes

class adminclass(admin.ModelAdmin):
    list_display=['classtitle','classtime','classteacherimage','classteachername','classprice','classimage']


admin.site.register(classes,adminclass)
# Register your models here.
