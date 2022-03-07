from django.contrib import admin
from .models.human_model import Human
from .models.car_model import Car
# Customizing admin panel
admin.site.site_header = "Django Signals Study"
admin.site.site_title = "Django Signals Study"

admin.site.register(Human)
admin.site.register(Car)