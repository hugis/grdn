from django.conf import settings
from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt


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
        self.stdout.write(f"Connected with result code {rc}")
        client.subscribe(f"{settings.MQTT_TOPIC}/+")

    def on_message(self, client, userdata, msg):
        self.stdout.write(f"{msg.topic} {msg.payload}")
