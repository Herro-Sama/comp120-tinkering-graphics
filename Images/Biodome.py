import pygame, sys, time


#Colour
white = (255,255,255)

#Create window
window_width = 640
window_height = 350
screen = pygame.display.set_mode([window_width, window_height])

#Background
Background = pygame.image.load('Biodome.jpg')
screen.blit(Background,[0, 0])

pygame.init

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            sys.exit()