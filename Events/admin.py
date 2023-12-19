from django.contrib import admin
from Events.models import Event

class Event_admin(admin.ModelAdmin):
    list_display=['datetime','Eventprice','eventname','teacherimage','teachername','address']
    
admin.site.register(Event,Event_admin)    
# Register your models here.
