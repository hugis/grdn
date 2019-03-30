import re

from django.conf import settings
from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt

from ... import models


topic_regex = re.compile(r"^" + re.escape(settings.MQTT_TOPIC) + r"/(\d+)$")


class Command(BaseCommand):
    help = "Collect data from sensors"

    def handle(self, *args, **options):
        self.stdout.write("Start monitoring...")

        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(settings.MQTT_SERVER, 1883, 60)

        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        self.stdout.write("Connected with result code {}".format(rc))
        client.subscribe("{}/+".format(settings.MQTT_TOPIC))

    def on_message(self, client, userdata, msg):
        payload = float(msg.payload.decode("ascii"))
        m = topic_regex.match(msg.topic)
        if m:
            sensor_id = m.group(1)
            self.stdout.write("{}: {}".format(sensor_id, payload))

            try:
                sensor = models.Sensor.objects.get(pk=sensor_id)
            except models.Sensor.DoesNotExist:
                pass
            else:
                models.Observation.objects.create(sensor=sensor, value=payload)
