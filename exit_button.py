import time
from utils import door

from gpiozero import Button, SmoothedInputDevice
from signal import pause

# button = SmoothedInputDevice(26, pull_up=False, threshold=0.8, sample_wait=0.05, partial=True)
button = Button(26, bounce_time=0.5)


def open_door():
    print("Opening door from exit button")
    door.open()


if __name__ == "__main__":
    button.when_pressed = open_door
    pause()
