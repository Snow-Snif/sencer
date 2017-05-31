import spidev
import time
import sys

spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    #data = ((adc[1]&3) << 8) + adc[2]
    return (((adc[1]&3) << 8) + adc[2])

def convertVolts(data):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, 4)
    return volts

def convertTemp(volts):
    temp = (100 * volts) - 50.0
    temp = round(temp, 4)
    return temp

temp_channel = 0

delay = 1

while True:
    data = ReadChannel(0)
    volts = convertVolts(data)
    temp = convertTemp(volts)
    print("adc:".format(data))
    print("volts:".format(volts))
    print("temp:".format(temp))
    print("--------------------")
    time.sleep(1)