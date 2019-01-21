import time
from threading import Thread

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    import utils.mock_gpio as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)  # Set default as low


class OpenDoor(Thread):
    def run(self):
        print("OPENING DOOR")
        GPIO.output(12, GPIO.LOW)
        time.sleep(2)
        GPIO.output(12, GPIO.HIGH)
        print("CLOSING DOOR")


def open():
    OpenDoor().start()
