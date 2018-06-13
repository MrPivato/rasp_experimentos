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

# define e comeca a PWM (pulse-width modulation)
pwm = GPIO.PWM(led, 1000)
pwm.start(0)

# vars de controle
brilho = 0
fade = 1

while True:
   
    brilho += fade

    pwm.ChangeDutyCycle(brilho)

    if brilho == 0 or brilho == 100:
        fade = -fade

    time.sleep(0.01)
    
