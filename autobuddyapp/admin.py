from django.contrib import admin
from .models import Make, Model, Car
# Register your models here.
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Car)