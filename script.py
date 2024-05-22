'''
                                        1°player												2°player
      32(esc)                           38(up)													12(up)
                            36(left)                  40(right)						11(left)				15(right)
      31(enter)                         37(down)												13(down)

'''
from pynput.keyboard import Key, Controller
import RPi.GPIO as GPIO
from threading import Thread

class pinListener(Thread):

    def __init__(self, pin, key):
        Thread.__init__(self)
        self.pin = pin
        self.key = key

    def run(self):
        while True:
            while GPIO.input(self.pin) == GPIO.HIGH:
                keyboard.press(self.key)
                #print(""+str(self.pin)+"	"+str(self.key))
                if stopFlag == True:
                    keyboard.release(self.key)
                    return
            keyboard.release(self.key)
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
    sDownT.join()

def startThreads():
    escT.start()
    enterT.start()
    fUpT.start()
    fLeftT.start()
    fRightT.start()
    fDownT.start()
    sUpT.start()
    sLeftT.start()
    sRightT.start()
    sDownT.start()

pins=[32, 31, 38, 36, 40, 37, 12, 11, 15, 13]
keys=[Key.esc, Key.enter, Key.up, Key.left, Key.right, Key.down]
keyboard= Controller()
stopFlag= False
#esc and enter are in common
escT = pinListener(pins[0], keys[0])
enterT = pinListener(pins[1], keys[1])
#first player buttons
fUpT = pinListener(pins[2], keys[2])
fLeftT = pinListener(pins[3], keys[3])
fRightT = pinListener(pins[4], keys[4])
fDownT = pinListener(pins[5], keys[5])
#second player buttons
sUpT = pinListener(pins[6], keys[2])
sLeftT = pinListener(pins[7], keys[3])
sRightT = pinListener(pins[8], keys[4])
sDownT = pinListener(pins[9], keys[5])

setup()

try:
    startThreads()
    while True:
        pass
except KeyboardInterrupt:
    destroy()
