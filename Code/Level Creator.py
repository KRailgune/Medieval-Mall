###TODO###
##fix issue that drawing a circle doesnt get cleared on the surface

import pygame, os, random

Win_x,Win_y = 1080*0.75,1920*0.75
Clock = pygame.time.Clock()
FPS = 120

def DrawLines():
    
    pass

def DrawOrigin(surface,origin):
    pygame.draw.circle(surface,(255,0,0),(origin),10)

def NewLevel_Setup():
    TileSize = int(input("TileSize: "))
    print("Preparing Editor")
    return TileSize

def LoadLevel_Setup():
    print("Pick the level you would like:")
    pass

def Panning(event,Origin,panning,offset):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button==2:
        panning = True
        mousepos = pygame.mouse.get_pos()
        offset = mousepos[0]-Origin[0],mousepos[1]-Origin[1]

    elif event.type == pygame.MOUSEBUTTONUP and event.button==2:
        panning = False

    return panning,offset


##--------------------MAIN-----------------------##
print("1.If you like to load a level")
print ("2.If you would like to create a new level")
WindowName = "NewLevel"
UserChoice = int(input())
if UserChoice == 1:
    LoadLevel_Setup()
else:
    TileSize = NewLevel_Setup()

## window init
pygame.display.init()
Window = pygame.display.set_mode((Win_y,Win_x),pygame.RESIZABLE)
pygame.display.set_caption(WindowName)

## run loop
origin = 0,0
offset = 0,0
panning = False
while True:

    Window.fill((255,255,255))
    DrawOrigin(Window,origin)

    if panning == True:
        mousepos = pygame.mouse.get_pos()
        origin = (mousepos[0]-offset[0]),(mousepos[1]-offset[1])
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        panning,offset = Panning(event,origin,panning,offset)

    print(Clock.get_fps())
    pygame.display.update()
    Clock.tick(FPS)