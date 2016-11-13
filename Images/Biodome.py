import pygame
import sys

# Create window
window_width = 640
window_height = 350
screen = pygame.display.set_mode([window_width, window_height])

# Define Sunset Function, background & increase pixel colour 6 times
def Sunset():
    Background = pygame.image.load('Biodome.jpg')
    screen.blit(Background,[0, 0])
    pxarray = pygame.PixelArray(screen)

    for i in range(0,6):
        for Y in xrange(window_height):
            for X in xrange(window_width):
                Red = screen.get_at((X, Y)).r
                Green = screen.get_at((X, Y)).g
                Blue = screen.get_at((X, Y)).b
                pxarray[X, Y] = (Red*0.8, Green*0.7, Blue*0.8)
        pygame.display.update()


    pygame.init()
while True:
    Sunset()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()