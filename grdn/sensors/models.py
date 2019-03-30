from django.db import models
from django.utils.translation import gettext as _


class Sensor(models.Model):
    UNIT_LUX = "lux"
    UNIT_DEGREES_CELSIUS = "°C"
    UNIT_CHOICES = [
        (UNIT_LUX, _(UNIT_LUX)),
        (UNIT_DEGREES_CELSIUS, _(UNIT_DEGREES_CELSIUS)),
    ]

    name = models.CharField(_("name"), max_length=30)
    slug = models.SlugField(_("slug"), max_length=30, unique=True)
    unit = models.CharField(
        _("unit of data"), max_length=10, blank=True, choices=UNIT_CHOICES
    )
    description = models.TextField(_("description"), blank=True)

    class Meta:
        verbose_name = _("sensor")
        verbose_name_plural = _("sensors")

    def __str__(self):
        return self.name


class Observation(models.Model):
    sensor = models.ForeignKey(
        Sensor, verbose_name=_("sensor"), on_delete=models.CASCADE
    )
    value = models.FloatField(_("value"))
    timestamp = models.DateTimeField(
        _("timestamp"),
        blank=True,
        null=True,
        help_text=_("When is observation measured. It is NULL, if sensor has no RTC."),
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("When is observations stored in database."),
    )

    class Meta:
        verbose_name = _("observation")
        verbose_name_plural = _("observations")

    def __str__(self):
        return "{}: {} {}".format(self.sensor, self.value, self.sensor.unit)
