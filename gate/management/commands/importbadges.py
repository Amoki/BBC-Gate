import time
from django.core.management.base import BaseCommand, no_translations
from nfc_reader.reader import NfcReader
from gate.models import Rfid


class Command(BaseCommand):
    help = "import badges"

    @no_translations
    def handle(self, *args, **options):
        reader = NfcReader()

        while True:
            time.sleep(1)  # Avoid multiple read
            uid = reader.read_nfc_sync()
            Rfid.objects.get_or_create(rfid_id=uid)

            self.stdout.write(self.style.SUCCESS("Imported rfid " + uid))
