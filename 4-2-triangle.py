import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decto2(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def dec2dec(value):
    signal = decto2(value)
    GPIO.output(dac, signal)

try:
    period = int(input("Enter period = "))
    while(True):
        for i in range(255):
            dec2dec(i)
            time.sleep(period/510)
        i = 255
        while i >= 0:
            dec2dec(i)
            time.sleep(period/510)
            i = i -1
finally:
    GPIO.output(dac, 0)
    GPIO.clean()

