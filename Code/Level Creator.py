import pygame

Win_x,Win_y = 1080*0.75,1920*0.75

def CreatingWindow():
    pygame.display.init()
    Window = pygame.display.set_mode((Win_y,Win_x))

def LoadLevel():
    print("Loading")

def NewLevel():
    print("Loading")
    pass

print("1.If you like to load a level")
print ("2.If you would like to create a new level")
UserChoice = int(input())
if UserChoice == 1:
    LoadLevel()
else:
    NewLevel()
        