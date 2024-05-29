from pynput.keyboard import Key, Controller, keyCode
import RPi.GPIO as GPIO
from threading import Thread

class PinListener(Thread):

    def __init__(self, pin, key):
        Thread.__init__(self)
        self.pin = pin
        self.key = key

    def run(self):
        while True:
            while GPIO.input(self.pin) == GPIO.HIGH:
                keyboard.press(self.key)        #press the key associated with the pin
                #print(""+str(self.pin)+"	"+str(self.key))
                if stopFlag == True:
                    keyboard.release(self.key)
                    return
            keyboard.release(self.key)
            if stopFlag == True:
                return

#set the GPIO in BOARD mode and set all the GPIO pins in input mode with pull down resistance
def setup():
    GPIO.setmode(GPIO.BOARD)
    for i in range(len(pins)):
        GPIO.setup(pins[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #print("Setup complete")

#safely exit the program after all the threads have stopped
def destroy():
    GPIO.cleanup()
    stopFlag= True
    sDownT.join()       #wait the last thread started to stop

#start all the threads
def startThreads():
    #start esc and enter threads
    escT.start()
    enterT.start()
    #start first player threads
    fUpT.start()
    fLeftT.start()
    fRightT.start()
    fDownT.start()
    #start second player threads
    sUpT.start()
    sLeftT.start()
    sRightT.start()
    sDownT.start()
    #print("All the threads have started")


pins=[32, 31, 38, 36, 40, 37, 12, 11, 15, 13]
keys=[Key.esc, Key.enter, Key.up, Key.left, Key.right, Key.down, KeyCode.from_char('w'), KeyCode.from_char('a'), KeyCode.from_char('d'), KeyCode.from_char('s')]
keyboard= Controller()
stopFlag= False
#esc and enter are in common
escT = PinListener(pins[0], keys[0])
enterT = PinListener(pins[1], keys[1])
#first player buttons
fUpT = PinListener(pins[2], keys[2])
fLeftT = PinListener(pins[3], keys[3])
fRightT = PinListener(pins[4], keys[4])
fDownT = PinListener(pins[5], keys[5])
#second player buttons
sUpT = PinListener(pins[6], keys[6])
sLeftT = PinListener(pins[7], keys[7])
sRightT = PinListener(pins[8], keys[8])
sDownT = PinListener(pins[9], keys[9])

setup()
try:
    startThreads()
    while True:
        pass            #the main thread just continously check if CTRL+C is pressed
except KeyboardInterrupt:
    destroy()
