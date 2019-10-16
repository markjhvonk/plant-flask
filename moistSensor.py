import time
from gpiozero import InputDevice
# import RPi.GPIO as GPIO
from time import sleep

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.IN)
# # loop through 50 times, on/off for 1 second
# while True:
#     GPIO.output(7, True)
#     time.sleep(1)
# GPIO.cleanup()

sensor = InputDevice(17)

while True:
    print('is_active?')
    print(sensor.is_active)
    print(sensor.value)
    sleep(1)
