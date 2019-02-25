import factory
from django.utils.text import slugify

from .. import models


class SensorFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Sensor
        django_get_or_create = ["slug"]

    name = "Sensor 1"
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))


class ObservationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Observation

    sensor = factory.SubFactory(SensorFactory)
    value = 1.0
