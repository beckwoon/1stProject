from django.contrib import admin

# Register your models here.
from .models import *
from monitoring.models import Data

class RecoveryAdmin(admin.ModelAdmin):
    list_display = ['car_num', 'car_date', 'rq_ex','rp_num', 'price_ex', 'rq_price', 'outstanding1', 'outstanding2', 'created']
    list_filter = ['created', 'rq_ex', 'price_ex', 'outstanding1', 'outstanding2']
    search_fields = ['car_num', 'text']
    ordering = ['-car_date']

admin.site.register(Recovery, RecoveryAdmin)
