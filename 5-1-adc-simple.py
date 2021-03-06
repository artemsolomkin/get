import RPi.GPIO as gpio
import time


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
comp = 4
troyka = 17
Vref = 3.3
bdepth = 8 

gpio.setmode( gpio.BCM )

gpio.setup( dac, gpio.OUT, initial=gpio.LOW )
gpio.setup( troyka, gpio.OUT, initial=gpio.HIGH )
gpio.setup( comp, gpio.IN )


def decto2(value):
    return [int(bit) for bit in bin( value ) [2:].zfill( bdepth )]

def adc():
    retvalue = 0
    for decVtest in range(2 ** bdepth):
        gpio.output( dac, decto2(decVtest) )
        time.sleep( 0.0007 )
        compsignal = gpio.input( comp )

        if compsignal == 0:
            retvalue = decVtest
            break

    return retvalue


try:
    while 1:
        decVfind = adc()
        binVfind = decto2(decVfind)

        print('decimal V = {}'.format(decVfind))
        print('binary V = {}'.format(binVfind))
        print('V = {}'.format( decVfind / ( 2 ** bdepth ) * Vref ))
        print( '' )
        


finally:
    gpio.output( dac, 0 )
    gpio.output( troyka, 0 )
    gpio.cleanup()