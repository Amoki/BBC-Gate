from utils.nfc import NfcReader


if __name__ == "__main__":
    reader = NfcReader()
    while True:
        uid = reader.read_nfc_sync()
