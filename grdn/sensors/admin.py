from django.contrib import admin

from . import models


@admin.register(models.Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "unit"]


@admin.register(models.Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ["sensor", "value", "created_at"]
