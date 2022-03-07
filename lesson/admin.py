from django.contrib import admin
from .models.human_model import Human
from .models.car_model import Car
from .models.history_model import DeletedHumansHistory
# Customizing admin panel
admin.site.site_header = "Django Signals Study"
admin.site.site_title = "Django Signals Study"

admin.site.register(Human)
admin.site.register(Car)

# History model(s)
admin.site.register(DeletedHumansHistory)
