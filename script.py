'''

      32  esc                        38
                           36                  40
      31  enter                      37

'''
from pynput.keyboard import Key, Controller
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(escP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(enterP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(upP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(leftP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(rightP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(downP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    keyboard= Controller()

def destroy():
    GPIO.cleanup()

def loop():
    while True:
        for i in pins:
            if GPIO.input(i) == GPIO.HIGH:
                print("BUSSI",i)
            else:
                print("COSTA")

pins=[32,31,38,36,40,37]
key=['enter','esc','up','left','right','down']

escP=pins[0]
enterP=pins[1]
upP=pins[2]
leftP=pins[3]
rightP=pins[4]
downP=pins[5]

setup()

try:
    loop()
except KeyboardInterrupt:
    destroy()
