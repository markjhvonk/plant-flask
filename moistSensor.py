import time
from gpiozero import InputDevice
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
sensor = InputDevice(17)


while True:
    print(GPIO.input(channel))
    # print('is_active?')
    # print(sensor.is_active)
    # print(sensor.value)
    sleep(1)
