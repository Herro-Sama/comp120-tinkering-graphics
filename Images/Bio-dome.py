import pygame, sys, time


#Colour
white = (255,255,255)

#Create window
window_width = 1024
window_height = 578
screen = pygame.display.set_mode([window_width, window_height])

#Background
Background = pygame.image.load('Bio-dome.jpg')
screen.blit(Background,[0, 0])

#Circle drawing
sun = pygame.draw.circle(screen, white, (330, 140), 15, 0)

pygame.init

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False