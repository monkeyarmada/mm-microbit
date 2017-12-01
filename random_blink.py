from microbit import *
import random


def checkPixels():
    lit = False
    for x in range(0, 5):
        for y in range(0, 5):
            if display.get_pixel(x, y) > 0:
                lit = True
                return lit


run = True

while run:
    lit = checkPixels()
    if lit:
        display.clear()
    else:
        display.set_pixel(random.randint(0, 4), random.randint(0, 4), random.randint(0, 9))
    
    sleep(200)