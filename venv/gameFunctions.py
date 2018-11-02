import pygame

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkDown(event)
        elif event.type == pygame.KEYUP:
            checkUp(event)

def checkDown(event):
    if event.key == pygame.K_RIGHT:
        print("right")

def checkUp(event):
    if event.key == pygame.K_RIGHT:
        print(".")
