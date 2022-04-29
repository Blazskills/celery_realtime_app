from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(TacState)
class TacStateAdmin(admin.ModelAdmin):
    list_display = ['id', 'church_state',
                    'superintendent_name', 'phone', 'created']
    
    
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'church_assembly_location',
                    'pastor_incharge', 'phone', 'tacstatename', 'created']