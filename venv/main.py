import pygame
from settings import Settings
from buildMap import BuildMap

def runGame():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mßode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Super Mario Bros.")

    map = BuildMap(screen, settings)



    
    map.makeMap(floors, bricks, questionblocks)

    pygame.mixer.init()

    while True:
        screen.fill((0, 0, 0))


runGame()