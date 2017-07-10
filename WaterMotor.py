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
        print("回転 止めるときはbreak 0コマンド！")
    else:
        print(str(second)+"秒回転")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 0 )
    time.sleep(second)
elif order == "back":
    if second == 0:
        print("逆回転 止めるときはbreak 0コマンド！")
    else:
        print(str(second)+"秒逆回転")
    wiringpi.digitalWrite( motor1_pin, 0 )
    wiringpi.digitalWrite( motor2_pin, 1 )
    time.sleep(second)

if order == "break" or second != 0:
    print("ブレーキ！")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 1 )