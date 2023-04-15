from atexit import register
from django.contrib import admin

from Home_Page.models import Chart_Data

# Register your models here.
admin.site.register(Chart_Data)


