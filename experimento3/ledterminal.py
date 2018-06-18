# modulos necessarios
import RPi.GPIO as GPIO
import time
import signal
import sys

# num dos leds (referentes a GPIO)
led1 = 14
led2 = 15
led3 = 18

# para poder usar os pinos
GPIO.setmode(GPIO.BCM)

# limpar a GPIO, caso preciso
def limpa(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, limpa)

# define pinos como saida
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

while True:

    print("Digite o numero do led que deseja ligar/desligar:")
    led = input()

    print("Digite o estado: (1 = ligar, 0 = desligar)")
    state = input()

    if True:
        if led == 1:
            if state == 1:
                state = True
                led = led1 

            elif state == 0:
                state = False
                led = led1

            else:
                pass

        elif led == 2:
            if state == 1:
                state = True
                led = led2

            elif state == 0:
                state = False
                led = led2

            else:
                pass

        elif led == 3:
            if state == 1:
                state = True
                led = led3

            elif state == 0:
                state = False
                led = led3

            else:
                pass

    else:
        pass

    GPIO.output(led, state)