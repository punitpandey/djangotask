from django.contrib import admin

# Register your models here.
from .models import teacher,schedule
admin.site.register(teacher)
admin.site.register(schedule)