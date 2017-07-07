import spidev
import time
import os


spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1]&3) << 8) + adc[2]

def convertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

def convertTemp(data,places):
    temp = ((data * 330) / float(1023) - 50.0)
    temp = round(temp, places)
    return temp

temp_channel = 0
light_channel = 1

delay = 1


while True:
    data = ReadChannel(0) #adc value
    volts = convertVolts(data,2) #volt
    temp = convertTemp(volts,2)



    light_level = ReadChannel(1)
    light_volts = convertVolts(light_level, 2)

    print("--------------------------------------------")
    print("Light: {} ({}V)".format(light_level, light_volts))
    print("Temp:{}({}V{}degC)".format(deta,volts,temp))
    time.sleep(delay)
