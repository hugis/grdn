import pytest

from .. import models
from . import factories


pytestmark = pytest.mark.django_db


def test_sensor_str():
    sensor = factories.SensorFactory()
    assert str(sensor) == sensor.name


def test_observation_str():
    sensor = factories.SensorFactory(name="Sensor 1", unit=models.Sensor.UNIT_LUX)
    observation = factories.ObservationFactory(sensor=sensor)
    assert str(observation) == "Sensor 1: 1.0 lux"
