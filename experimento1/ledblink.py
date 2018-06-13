# livrarias necessarias
import RPi.GPIO as GPIO
import time
import signal
import sys

# para poder usar os pinos
GPIO.setmode(GPIO.BCM)

# pino a ser usado
led = 14

# limpar a GPIO, caso preciso
def limpa(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, limpa)

# define pino como saida
GPIO.setup(led, GPIO.OUT)

while True:

    GPIO.output(led, True)
    print("Ligado")
    time.sleep(1)
    GPIO.output(led, False)
    print("Desligado")
    time.sleep(1)
