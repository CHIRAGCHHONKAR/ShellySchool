from django.contrib import admin
from Contact_Enquiry.models import contact


class contactdata(admin.ModelAdmin):
    list_display=['name','email','message','date']
    
    
admin.site.register(contact,contactdata)
# Register your models here.
