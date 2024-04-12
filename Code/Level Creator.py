import pygame, os

Win_x,Win_y = 1080*0.75,1920*0.75
Clock = pygame.time.Clock()
FPS = 60
SavedLevels = os.listdir("D:\.My folder\Personal stuff\coding stuff\Coding Projects\Medieval Mall\Code\Levels")
Textures = os.listdir("D:\.My folder\Personal stuff\coding stuff\Coding Projects\Medieval Mall\Assets")
LevelList = []


def DrawLevel(LevelList,MapSize_x,MapSize_y,TileSize):
    for tile in LevelList:
        

    pass

def CreatingWindow(WindowName):
    pygame.display.init()
    Window = pygame.display.set_mode((Win_y,Win_x))
    pygame.display.set_caption(WindowName)

##TODO
##Loads a level from the folder "levels"
def LoadLevel():
    print("Pick the level you would like:")
    for x in range(len(SavedLevels)):
        print(f"{x}. {SavedLevels[x]}")
    LevelChoice = int(input())
    print(f"Chosen: {SavedLevels[LevelChoice]}")

    CreatingWindow(SavedLevels[LevelChoice])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

#TODO
##Creates a new level
def NewLevel():
    TileSize = int(input("TileSize: "))
    MapSize = input("MapSize in the format '1920x1080':  ")

    ##extracts the x and y data
    for i in range(len(MapSize)):
        if MapSize[i] == "x":
            MapSize_x = MapSize[0:i]
            MapSize_y = MapSize[i+1:len(MapSize)]
    
    ##Casting int and making it a factor of TileSize
    MapSize_x = int(MapSize_x)
    MapSize_y = int(MapSize_y)
    if MapSize_x % TileSize != 0:
        MapSize_x += 16-(MapSize_x%TileSize)
    if MapSize_y % TileSize != 0:
        MapSize_y += 16-(MapSize_y%TileSize)
    print(f"MapSize_x: {MapSize_x}\nMapSize_y: {MapSize_y}\nTileSize: {TileSize}")

    ##generates the empty textures for the level
    switch = True
    for y in range(MapSize_y//TileSize):
        for x in range(MapSize_x//TileSize):
            if switch == True:
                LevelList.append("empty0")
            else:
                LevelList.append("empty1")
    CreatingWindow("newLevel")
    while True:
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        pygame.display.update()
        Clock.tick(FPS)


print("1.If you like to load a level")
print ("2.If you would like to create a new level")
UserChoice = int(input())
if UserChoice == 1:
    LoadLevel()
else:
    NewLevel()
        