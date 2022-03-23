import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)

def ChangeDutyCycle(dutycycle):
    p.start(dutycycle)

try:
    while(True):
        val = int(input("Введите число"))
        ChangeDutyCycle(val)
        print(str(3.3*val/100))

finally:
    p.stop()
    GPIO.clean()