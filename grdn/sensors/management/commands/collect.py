from time import sleep

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect data from sensors"

    def handle(self, *args, **options):
        self.stdout.write("Start monitoring...")

        for x in range(1, 20):
            sleep(1)
            self.stdout.write(f"Count: {x}")


