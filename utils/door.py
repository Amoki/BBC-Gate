import time
from threading import Thread

from gpiozero import LED

door = LED(12, initial_value=False, active_high=False)


class OpenDoor(Thread):
    def run(self):
        print("OPENING DOOR")
        door.on()
        time.sleep(2)
        door.off()
        print("CLOSING DOOR")


def open():
    OpenDoor().start()
