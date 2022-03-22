import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 1, 1, 1, 1, 1, 1, 1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in range(8):
    GPIO.output(dac[i], number[i])
    
time.sleep(5)

GPIO.output(dac, 0)
GPIO.cleanup()