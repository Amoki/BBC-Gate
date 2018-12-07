import os
import time
import requests

from reader import NfcReader


API_URL = os.environ.get("API_URL", "http://localhost:8000")

reader = NfcReader()

while True:
    time.sleep(2)  # Avoid multiple read
    uid = reader.read_nfc_sync()
    print(f"Scanned {uid}")
    try:
        response = requests.post(API_URL + "/rfid", json={"rfid_id": uid})
        print(f"Door API responded with {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Unable to connect to API server")
