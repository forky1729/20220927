import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
#GPIO.setup(dac,GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]



"""
#1
try:
    while True:
        g = input()
        if g=="q":
            break
        else:
            if g.isdigit()==True:
                g= int(g)
                if g>255:
                    print("error!!!")
                else:
                    GPIO.output(dac,decimal2binary(g))
                    print((g*3.3)/256)
            else:
                print("error!!!")
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
"""

"""
#2
T = int(input())
try:
    while True:
        for i in range (0,256):
            GPIO.output(dac,decimal2binary(i))
            print(i)
            time.sleep(256/T)
        for i in range (255,-1,-1):
            GPIO.output(dac,decimal2binary(i))
            print(i)
            time.sleep(256/T)
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])

"""




#3
#GPIO.output(dac, [0,0,0,0,0,0,0,0])
GPIO.setup(24,GPIO.OUT)
nu = 100
p = GPIO.PWM(24, nu)
p.start(0)

try: 
    while True:
        k = int(input())
        p.ChangeDutyCycle(k)
finally:
    GPIO.cleanup()
