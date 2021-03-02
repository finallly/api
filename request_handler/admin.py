from django.contrib import admin
from .models import ServiceModel, LogModel, StatisticsModel

admin.site.register(ServiceModel)
admin.site.register(LogModel)
admin.site.register(StatisticsModel)
