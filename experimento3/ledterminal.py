# modulos necessarios
import RPi.GPIO as GPIO
import time
import signal
import sys

led1 = 14
led2 = 15
led3 = 18

# para poder usar os pinos
GPIO.setmode( GPIO.BCM )

# pinos a serem usados
def checkpin( led, state ):
    
    if True:
        if led == 1:
            if state == 1:
                state = True
                led = led1 
                return led, state

            elif state == 0:
                state = False
                led = led1
                return led, state

            else:
                pass

        elif led == 2:
            if state == 1:
                state = True
                led = led2
                return led, state

            elif state == 0:
                state = False
                led = led2
                return led, state

            else:
                pass
            
        elif led == 3:
            if state == 1:
                state = True
                led = led3
                return led, state

            elif state == 0:
                state = False
                led = led3
                return led, state

            else:
                pass
         
    else:
        pass

# limpar a GPIO, caso preciso
def limpa( signal, frame ):
    GPIO.cleanup()
    sys.exit(0)

signal.signal( signal.SIGINT, limpa )

# define pinos como saida
GPIO.setup( led1, GPIO.OUT )
GPIO.setup( led2, GPIO.OUT )
GPIO.setup( led3, GPIO.OUT )

while True:

    print("Digite o led, e se deseja ligar, ex:")
    print("(1 1 || ligar led 1) ou (2 0 || desligar led 2)")
    print("Um numero por linha!!!!")

    led = input()
    state = input()
    
    checkpin( led, state )
    
    GPIO.setup( led, GPIO.OUT )
    GPIO.output( led, state )

