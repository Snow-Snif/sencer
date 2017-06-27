#don't use

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

def convertTemp(data,places):
    temp = ((330 * data) / float(1023)) - 50.0
    temp = round(temp, places)
    return temp

moisture_pin = 2;

delay = 1

while True:

    data = ReadChannel(2)
    volt = convertTemp(data,2)
    print("--------------------")
    print("moisture: {}({}V)".format(data,volt))
    time.sleep(delay)