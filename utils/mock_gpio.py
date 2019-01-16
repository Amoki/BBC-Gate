def setmode(mode):
    print(f"setmode: {mode}")


def setup(pin, in_or_out):
    print(f"setup: {pin}, {in_or_out}")


def output(pin, state):
    print(f"output: {pin}, {state}")


def cleanup():
    print("cleanup")


def add_event_detect(pin, mode, callback, bouncetime):
    print(f"add_event_detect on pin {pin}, mode={mode} with bouncetime={bouncetime}")


BCM = "BCM"
BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
LOW = "LOW"
HIGH = "HIGH"
PUD_DOWN = "PUD_DOWN"
