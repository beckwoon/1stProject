from django.contrib import admin

# Register your models here.

from .models import *

class DataAdmin(admin.ModelAdmin):
    list_display = ['a_rdate', 'car_id', 'car_num1', 'car_num2', 'car_num3', 'car_type', 'cus_name','text']
    list_filter = ['a_rdate', 'car_type', 'cus_name']
    search_fields = ['a_rdate', 'car_num1', 'car_num2', 'car_num3', 'car_type', 'cus_name', 'text']
    ordering = ['-a_rdate']

admin.site.register(Data, DataAdmin)


class MassAdmin(admin.ModelAdmin):
    list_display = ['cus', 'car', 'num', 'fdate', 'spot', 'created', 'updated', 'author']
    list_filter = ['fdate', 'cus', 'car']
    search_fields = ['fdate', 'cus', 'car', 'text']
    ordering = ['-fdate', '-updated']

admin.site.register(MassBoard, MassAdmin)


class CarTypeMgtAdmin(admin.ModelAdmin):
    list_display = ['num', 'cartype', 'maxprice']
    list_filter = ['cartype']
    search_fields = ['cartype']
    ordering = ['num']

admin.site.register(CarTypeMgt, CarTypeMgtAdmin)