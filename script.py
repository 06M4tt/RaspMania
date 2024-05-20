'''

      32(esc)                           38(up)
                            36(left)                  40(right)
      31(enter)                         37(down)

'''
from pynput.keyboard import Key, Controller
import RPi.GPIO as GPIO
from threading import Thread

class pinListener(Thread):

    def __init__(self, pin, key):
        Thread.__init__(self)
        self.pin = pin
        self.key= key

    def run(self):
        while True:
            if GPIO.input(pin) == GPIO.HIGH:
                keyboard.tap(key)
            if stopFlag == True:
                return

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(escP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(enterP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(upP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(leftP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(rightP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(downP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #print("Setup completato")

def destroy():
    GPIO.cleanup()
    stopFlag= True
    downT.join()

def setThreads():
    escT = pinListener(pins[0], keys[0])
    enterT = pinListener(pins[1], keys[1])
    upT = pinListener(pins[2], keys[2])
    leftT = pinListener(pins[3], keys[3])
    rightT = pinListener(pins[4], keys[4])
    downT = pinListener(pins[5], keys[5])

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

setup()
setThreads()

try:
    startThreads()
    while True:
        pass
except KeyboardInterrupt:
    destroy()
