import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts)
    return volts

def ConvertTemp(data,places):
    temp = ((data * 330) / float(1023)) - 50
    temp = round(temp, places)
    return temp

light_channel = 0

delay = 5

while True:
    light_level = ReadChannel(light_channel)
    light_volts = ConvertVolts(light_level, 2)
    print "--------------------------------------------"
    print("Light: {} ({}V)".format(light_level, light_volts))
    time.sleep(delay)