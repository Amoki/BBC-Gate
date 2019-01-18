import time
from utils import door

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    import utils.mock_gpio as GPIO

BUTTON = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def open_door(channel):
    print("Opening door from exit button")
    door.open()


if __name__ == "__main__":
    print(f"Listening button {BUTTON}")
    GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=open_door, bouncetime=500)
    while True:
        time.sleep(60)
