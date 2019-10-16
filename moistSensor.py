from gpiozero import InputDevice
from time import sleep

sensor = InputDevice(17, pull_up=true)

while True:
    print('is_active?')
    print(sensor.is_active)
    print(sensor.value)
    sleep(1)
