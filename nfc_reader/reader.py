import time

try:
    import nxppy
except ModuleNotFoundError:
    import mock_nxppy as nxppy


class NfcReader:
    def __init__(self):
        self.mifare = nxppy.Mifare()

    def read_nfc_sync(self):
        while True:
            try:
                return self.mifare.select()
            except nxppy.SelectError:
                # SelectError is raised if no card is in the field.
                time.sleep(0.5)
