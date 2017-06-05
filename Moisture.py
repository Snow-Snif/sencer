import spidev
import time
import os
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0)
GPIO.setmode(GPIO.BCM)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1] & 3) << 8) + adc[2]

moisture_pin = 2;

delay = 1

while True:
    # read the analog pin
    moisture = ReadChannel(0)
    print("--------------------")
    print("moisture: {0}".format(moisture))
    time.sleep(delay)