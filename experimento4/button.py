# modulos necessarios
import RPi.GPIO as GPIO
import time
import signal
import sys

# para poder usar os pinos
GPIO.setmode(GPIO.BCM)

# pino a ser usado
button = 14

# limpar a GPIO, caso preciso
def limpa(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, limpa)

# define pino como saida
GPIO.setup(button, GPIO.IN)

while True:

    if GPIO.input(button) == True:
        print("Botao pressionado")

    else:
        print("Botao despressionado")

    time.sleep(0.08)
