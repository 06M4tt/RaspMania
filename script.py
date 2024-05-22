'''

      32(esc)                           38(up)
                            36(left)                  40(right)
      31(enter)                         37(down)

'''
from pynput.keyboard import Key, Controller
import RPi.GPIO as GPIO
from threading import Thread
import time

class pinListener(Thread):

    def __init__(self, pin, key):
        Thread.__init__(self)
        self.pin = pin
        self.key = key

    def run(self):
        while True:
            while GPIO.input(self.pin) == GPIO.HIGH:
                keyboard.press(self.key)
            keyboard.release(self.key)
            #print(""+str(self.pin)+"	"+str(self.key))
            if stopFlag == True:
                return

def setup():
    GPIO.setmode(GPIO.BOARD)
    for i in range(len(pins)):
        GPIO.setup(pins[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #print("Setup completato")

def destroy():
    GPIO.cleanup()
    stopFlag= True
    downT.join()

def startThreads():
    escT.start()
    enterT.start()
    upT.start()
    leftT.start()
    rightT.start()
    downT.start()

pins=[32, 31, 38, 36, 40, 37]
keys=[Key.esc, Key.enter, Key.up, Key.left, Key.right, Key.down]
keyboard= Controller()
stopFlag= False
escT = pinListener(pins[0], keys[0])
enterT = pinListener(pins[1], keys[1])
upT = pinListener(pins[2], keys[2])
leftT = pinListener(pins[3], keys[3])
rightT = pinListener(pins[4], keys[4])
downT = pinListener(pins[5], keys[5])

setup()

try:
    startThreads()
    while True:
        pass
except KeyboardInterrupt:
    destroy()
