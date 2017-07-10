import wiringpi
import time
import sys

motor1_pin = 16
motor2_pin = 21

param = sys.argv

order = param[1]

second = int(param[2])

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( motor1_pin, 1 )
wiringpi.pinMode( motor2_pin, 1 )

if order == "go":
    if second == 0:
        print("stop 0")
    else:
        print(str(second)+"per cycle")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 0 )
    time.sleep(second)
elif order == "back":
    if second == 0:
        print("stop 0")
    else:
        print(str(second)+"per cycle(rev)")
    wiringpi.digitalWrite( motor1_pin, 0 )
    wiringpi.digitalWrite( motor2_pin, 1 )
    time.sleep(second)

if order == "break" or second != 0:
    print("brake")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 1 )