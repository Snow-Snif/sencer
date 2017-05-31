import spidev
import time
import os
import sys

spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def convertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

def convertTemp(volts,places):
    temp = (100 * volts) - 50.0
    temp = round(temp, places)
    return temp

temp_channel = 0

delay = 1

while True:
    data = ReadChannel(0)
    volts = convertVolts(data,2)
    temp = convertTemp(data,2)
    print("Temp:{}({}V{}degC)".format(data,volts,temp))
    print("--------------------")
    time.sleep(1)