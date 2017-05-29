import spidev
import time
import sys

spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer([1, (8 + channel) << 4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def convertVolts(data):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, 4)
    return volts

def convertTemp(volts):
    temp = (100 * volts) - 50.0
    temp = round(temp, 4)
    return temp

delay = 5
while True:
    dataAdc = ReadChannel(0)
    volts = convertVolts(dataAdc)
    temp = convertTemp(volts)
    print("adc:"(dataAdc))
    print("volts:"(volts))
    print("temp:"(temp))
    time.sleep(delay)