from microbit import *

# Block Breaker

gameRun = True
blocks = [9, 9, 9, 9, 9]
shots = []
blocksYpos = 0
shipPos = [2, 4]


def renderView():
    display.clear()
    # draw ship
    display.set_pixel(shipPos[0], shipPos[1], 9)
    # draw blocks
    for idx, val in enumerate(blocks):
        display.set_pixel(idx, 0, val)
    # draw shots
    if len(shots) > 0:
        for shot in shots:
            display.set_pixel(shot[0], shot[1], 4)


def moveElements():
    if len(shots) > 0:
        for idx, val in enumerate(shots):
            if shots[idx][1] >= 1:
                shots[idx][1] = shots[idx][1] - 1
            else:
                blocks[shots[idx][0]] = 0
                del shots[idx]
               

def processInput():
    if button_a.is_pressed() and button_b.is_pressed():
        if len(shots) < 2:
            shots.append([shipPos[0], shipPos[1]-1])
    elif button_a.is_pressed():
        if shipPos[0] > 0:
            shipPos[0] = shipPos[0] - 1
    elif button_b.is_pressed():
        if shipPos[0] < 4:
            shipPos[0] = shipPos[0] + 1


while gameRun:
    processInput()
    renderView()
    moveElements()
    sleep(150)
