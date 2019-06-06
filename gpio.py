import gpiozero
from gpiozero import Device
import os

if os.environ.get("ENV", "development") == "development":
    from gpiozero.pins.mock import MockFactory

    Device.pin_factory = MockFactory()
