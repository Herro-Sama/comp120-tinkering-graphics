import pygame
import sys
import time
from pygame.locals import *

# Colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

# Create window
window_width = 640
window_height = 350
screen = pygame.display.set_mode([window_width, window_height])

# Define Sunset Function, background & increase pixel colour 4 times
def Sunset():
    Background = pygame.image.load('Biodome.jpg')
    screen.blit(Background,[0, 0])
    pxarray = pygame.PixelArray(Background)
    for i in range(0, 4):
        for Y in xrange(window_height):
            for X in xrange(window_width):
                Red = screen.get_at((X, Y)).r
                Green = screen.get_at((X, Y)).g
                Blue = screen.get_at((X, Y)).b
                pxarray[X, Y] = (Red*0.8, Green*0.7, Blue*0.7)
                pygame.display.update()

pygame.init
while True:
    Sunset()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()