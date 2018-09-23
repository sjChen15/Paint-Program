#testingStamps.py

from random import *
from pygame import * 
init()
   
RED  =(255,0,0) 
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
MINT=(44,214,104)
GRAPE=(55,18,102)
ROSERED=(193,27,27)
LILAC=(220,43,226)
PLUM=(56,26,56)
OLIVE=(85,107,47)
NAVY=(6,13,105)
ORCHID=(218,112,214)

col=(randint(0,20),randint(0,255),randint(0,255))

cake=image.load("cakes/cakeRoll.png")



size=(800,600) 
screen=display.set_mode(size)

running=True 

screen.fill(BLACK)

myClock=time.Clock()

while running:
    for evt in event.get():

        if evt.type==QUIT:
            running=False
            
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    display.flip()

    if mb[0]==1:
        screen.blit(cake,(mx,my))
    myClock.tick(60)
quit() 







    
