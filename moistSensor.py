from gpiozero import InputDevice
from time import sleep

sensor = InputDevice(17)

while True:
    print(sensor)
    sleep(1)
