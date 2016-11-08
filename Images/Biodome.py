import pygame, sys
from pygame.locals import *

#Create window
window_width = 640
window_height = 350
screen = pygame.display.set_mode([window_width, window_height])

#Background
Background = pygame.image.load('Biodome.jpg')


def Bbolt(screen):
    for Y in xrange(window_height):
        for X in xrange(window_width):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (Red/4, Green/4, Blue/4)

pygame.init

screen.blit(Background,[0, 0])
while True:
    keys_pressed = pygame.key.get_pressed()
    pxarray = pygame.PixelArray(screen)

    if keys_pressed[K_DOWN]:
        Bbolt(Background)

    del pxarray
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            sys.exit()