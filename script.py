'''

      32(esc)                           38(up)
                            36(left)                  40(right)
      31(enter)                         37(down)

'''
from pynput.keyboard import Key, Controller
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(escP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(enterP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(upP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(leftP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(rightP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(downP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print("Setup completato")

def destroy():
    GPIO.cleanup()

def loop():
    while True:
        for i in range(len(pins)):
            if GPIO.input(pins[i]) == GPIO.HIGH:
                controller.tap(keys[i])

pins=[32, 31, 38, 36, 40, 37]
keys=[Key.esc, Key.enter, Key.up, Key.left, Key.right, Key.down]
keyboard= Controller()

escP= pins[0]
enterP= pins[1]
upP= pins[2]
leftP= pins[3]
rightP= pins[4]
downP= pins[5]


setup()

try:
    loop()
except KeyboardInterrupt:
    destroy()
