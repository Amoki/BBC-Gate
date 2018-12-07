import nxppy
import time


class NfcReader:
    def __init__(self):
        self.mifare = nxppy.Mifare()

    def read_nfc_sync(self):
        while True:
            try:
                uid = self.mifare.select()
                print(uid)
                return uid
            except nxppy.SelectError:
                # SelectError is raised if no card is in the field.
                pass
            time.sleep(1)


if __name__ == "__main__":
    reader = NfcReader()
    while True:
        uid = reader.read_nfc_sync()
