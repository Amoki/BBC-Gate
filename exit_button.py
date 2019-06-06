import time
from utils import door
import gpio
from gpiozero import Button, SmoothedInputDevice
from signal import pause

button = Button(26, bounce_time=0.5)


def open_door():
    print("Opening door from exit button")
    door.open()


if __name__ == "__main__":
    button.when_pressed = open_door
    pause()
