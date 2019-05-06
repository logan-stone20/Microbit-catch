from microbit import *
import random

display.scroll("Hello, lets play catch!")
display.show(Image.HAPPY)
sleep(2000)
display.scroll("Press both buttons to start")

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break

display.scroll("Lets start!")

playfield = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    ]

xpos = 2
ypos = len(playfield) - 1
playerBrightness = 9
pixBrightness = 7
alternator = 0
update = 0
pixxList = [] #Same indexes in pixxList and pixyList will
pixyList = [] #correspond to each items coordinates

#allocates falling items to their next positions
def fall(pixxList, pixyList):
    for i in range (len(pixyList)):
        pixyList[i] = pixyList[i] + 1
        #if the item is caught
        if pixyList[i] == ypos and pixxList[i] == xpos:
            display.set_pixel(pixxList[i], pixyList[i]-1 , 0)
            pixyList.pop(i)
            pixxList.pop(i)
            break
        #if item is not caught
        elif pixyList[i] == ypos and pixxList[i] != xpos:
            return False
    return True

#draws falling items in their new positions
def draw(pixxList, pixyList):
    for i in range (len(pixyList)):
        display.set_pixel(pixxList[i], pixyList[i], pixBrightness)
        if pixyList[i] > 0:
            display.set_pixel(pixxList[i], pixyList[i]-1 , 0)

#create a new falling item
def createPix(pixxList, pixyList):
    pix = random.randint(0, len(playfield[0])-1)
    pixxList.append(pix)
    pixyList.append(0)
    
display.set_pixel(xpos, ypos, playerBrightness)

while True:
    if button_a.is_pressed():
        if xpos > 0:
            xpos -= 1
            display.set_pixel(xpos, ypos, playerBrightness)
            display.set_pixel(xpos+1, ypos, 0)
            sleep(200)
    if button_b.is_pressed():
        if xpos < 4:
            xpos +=1
            display.set_pixel(xpos, ypos, playerBrightness)
            display.set_pixel(xpos-1, ypos, 0)
            sleep(200)
    if update % 5 == 0:
        if fall(pixxList, pixyList):
            if alternator % 3 == 0:
                createPix(pixxList, pixyList)
            alternator += 1
            draw(pixxList, pixyList)
        else: 
            break
    sleep(200)
    update += 1

display.scroll("Game Over")


