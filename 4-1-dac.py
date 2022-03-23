import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxU = 3.3




def decto2(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def dec2dec(value):
    signal = decto2(value)
    GPIO.output(dac, signal)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while(True):
        inputStr = input("Write please integer number from 0 to 255")
        
        if inputStr.isdigit():
            value = int(inputStr)
            if value >= levels:
                print("Eror")
            print(str((maxU/2**8) * int(inputStr)))
            dec2dec(value)
        elif inputStr == 'q':
            print("Error")
        else:
            print("Error")

finally:
    GPIO.output(dac, 0)
    GPIO.clean()