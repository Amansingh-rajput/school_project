from django.contrib import admin
from .models import *
# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','Address']

admin.site.register(School)
admin.site.register(Standard)

