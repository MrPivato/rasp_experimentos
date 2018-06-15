# livrarias necessarias
import RPi.GPIO as GPIO
import time
import signal
import sys

# para poder usar os pinos
GPIO.setmode(GPIO.BCM)

# pinos a serem usados
led1 = 14 # xor
led2 = 15 # or
led3 = 18 # and

bot1 = 23
bot2 = 24

# vars logicas
a = False
b = False
c = False

# limpar a GPIO, caso preciso
def limpa(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, limpa)

# define pino como saida
GPIO.setup(bot1, GPIO.IN)
GPIO.setup(bot2, GPIO.IN)

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

while True:

    a = GPIO.input(bot1)
    b = GPIO.input(bot2)

    print("----------------------------------\nValores: ")
    print(a, b) 
    
    print("----------\nxor: ")
    c = a ^ b
    print(c)
    GPIO.output(led1, c)

    print("----------\nor: ")
    c = a or b
    print(c)
    GPIO.output(led2, c)

    print("----------\nand: ")
    c = a and b
    print(c)
    GPIO.output(led3, c)

    time.sleep(0.12)
