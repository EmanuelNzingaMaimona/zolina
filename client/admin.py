from django.contrib import admin
from .models import Message, Donor

class DonorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'group', 'province', 'municipe', 'district', 'email']
    
    
# Register your models here.
admin.site.register(Message)
admin.site.register(Donor, DonorAdmin)