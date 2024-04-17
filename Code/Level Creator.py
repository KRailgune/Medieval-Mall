###TODO###
# - Use 2dArray to store the LevelList


import pygame, os

Win_x,Win_y = 1080*0.75,1920*0.75
Clock = pygame.time.Clock()
FPS = 60
SavedLevels = os.listdir("D:\.My folder\Personal stuff\coding stuff\Coding Projects\Medieval Mall\Code\Levels")
Textures = os.listdir("D:\.My folder\Personal stuff\coding stuff\Coding Projects\Medieval Mall\Assets")

#Draws the level using the images in the assets folder
def DrawLevel(LevelList,Rows,Columns,TileSize,Window):
    for y in range(Columns):
        for x in range(Rows):
            TextureFromLevelList = pygame.image.load(f"D:\.My folder\Personal stuff\coding stuff\Coding Projects\Medieval Mall\Assets\{LevelList[y][x]}")
            Window.blit(TextureFromLevelList,(x*TileSize,y*TileSize))


def CreatingWindow(WindowName):
    pygame.display.init()
    Window = pygame.display.set_mode((Win_y,Win_x))
    pygame.display.set_caption(WindowName)
    return Window

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
        MapSize_x += TileSize-(MapSize_x%TileSize)
    if MapSize_y % TileSize != 0:
        MapSize_y += TileSize-(MapSize_y%TileSize)
    print(f"MapSize_x: {MapSize_x}\nMapSize_y: {MapSize_y}\nTileSize: {TileSize}")

    ##generates the empty textures for the level
    Rows , Columns = MapSize_x//TileSize,MapSize_y//TileSize
    LevelList = [[0 for j in range(Rows)]for i in range(Columns)]
    switch = True
    MetaSwitch = True
    for y in range(Columns):
        for x in range(Rows):
            if x==0:
                if MetaSwitch == True:
                    MetaSwitch=False
                    switch = MetaSwitch
                else:
                    MetaSwitch = True
                    switch = MetaSwitch

            if switch == True:
                LevelList[y][x] = "Utility\Empty0.png"
                switch = False
            else:
                LevelList[y][x] = "Utility\Empty1.png"
                switch = True

    Window = CreatingWindow("newLevel")
    while True:
        Window.fill(pygame.Color("#211522"))
        DrawLevel(LevelList,Rows,Columns,TileSize,Window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                try:
                    LevelList[mousepos[1]//TileSize][mousepos[0]//TileSize] = "Utility\Error.png"
                except IndexError:
                    pass

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==2:
                panning = True
                print("panning")
            elif event.type == pygame.MOUSEBUTTONUP and event.button==2:
                panning = False
                print("not panning")
            

        
        pygame.display.update()
        Clock.tick(FPS)


print("1.If you like to load a level")
print ("2.If you would like to create a new level")
UserChoice = int(input())
if UserChoice == 1:
    LoadLevel()
else:
    NewLevel()
        