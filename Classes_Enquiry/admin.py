from django.contrib import admin
from Classes_Enquiry.models import ClassesEnquiry
class ClassesEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'Classes', 'message')


admin.site.register(ClassesEnquiry, ClassesEnquiryAdmin)
# Register your models here.
