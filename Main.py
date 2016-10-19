import pygame, sys, time
from pygame.locals import *
pygame.init()

FPSCLOCK = pygame.time.Clock()

FPS = 4000

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('')

Black = (0, 0, 0)
White = (255, 255, 255)

Y1 = 200
Y2 = 200

Player1Score = 0
Player2Score = 0

font = pygame.font.SysFont(None, 96)

Cowboy = pygame.image.load("Images/ShipBridge.png")
Cow1Y = 250
Cow1X = 20

while True:

    window.fill(Black)
    window.blit(Cowboy, (Cow1X,Cow1Y))


    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        Cow2Y -= 0.25
        if Cow2Y == -1:
            Cow2Y = 0
    if keys[K_DOWN]:
        Cow2Y += 0.25
        if Cow2Y == 500:
            Cow2Y = 499
    if keys[K_w]:
        Cow1Y -= 0.25
        if Cow1Y == -1:
            Cow1Y = 0
    if keys[K_s]:
        Cow1Y += 0.25
        if Cow1Y == 500:
            Cow1Y = 499

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    FPSCLOCK.tick(FPS)