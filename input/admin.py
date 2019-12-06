from django.contrib import admin

# Register your models here.

from .models import Files

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'text', 'created', 'updated', 'author']
    list_filter = ['created']
    search_fields = ['file', 'created', 'text']
    ordering = ['-updated', '-created']

admin.site.register(Files, FileAdmin)
