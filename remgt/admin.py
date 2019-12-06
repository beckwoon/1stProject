from django.contrib import admin

# Register your models here.
from .models import *

class ReMgtAdmin(admin.ModelAdmin):
    list_display = ['car_num', 'car_model', 'car_date', 'prespot', 'cancel','created']
    list_filter = ['created', 'cancel', 'car_date']
    search_fields = ['car_num']
    ordering = ['created']

admin.site.register(ReManagement, ReMgtAdmin)
