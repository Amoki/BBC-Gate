def setmode(mode):
    print(f"setmode: {mode}")


def setup(pin, in_or_out):
    print(f"setup: {pin}, {in_or_out}")


def output(pin, state):
    print(f"output: {pin}, {state}")


def cleanup():
    print("cleanup")


BCM = "BCM"
BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
LOW = "LOW"
HIGH = "HIGH"
