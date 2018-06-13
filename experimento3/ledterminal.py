# livrarias necessarias
import RPi.GPIO as GPIO
import time
import signal
import sys

l = "L"
d = "D"

# para poder usar os pinos
GPIO.setmode(GPIO.BCM)

# pinos a serem usados
def checkpin():
    
    print("Deseja ligar ou desligar um led: (L/D)")
    escolha = input()

    if escolha == l: 

        print("Digite o led a ser ligado: (1, 2, 3)")
        led = input()

        if led == 1:
            led = 14
            GPIO.setup(led, GPIO.OUT)
            return led, True 

        elif led == 2:
            led = 15
            GPIO.setup(led, GPIO.OUT)
            return led, True 

        elif led == 3:
            led = 18
            GPIO.setup(led, GPIO.OUT)
            return led, True 

        else:
            checkpin()

    elif escolha == d:

        print("Digite o led a ser desligado: (1, 2, 3)")
        led = input()

        if led == 1:
            led = 14
            GPIO.setup(led, GPIO.OUT)
            return led, False 

        elif led == 2:
            led = 15
            GPIO.setup(led, GPIO.OUT)
            return led, False 

        elif led == 3:
            led = 18
            GPIO.setup(led, GPIO.OUT)
            return led, False 

        else:
            checkpin()
    
    else:
        checkpin()

# limpar a GPIO, caso preciso
def limpa(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, limpa)

# define pinos como saida

while True:

    GPIO.output(checkpin())

