import pygame, sys, random, time, math
from pygame.locals import *

class Ball:
    def __init__(self):
        # Choose a random position
        self.pos_x = random.randrange(350, 450)
        self.pos_y = random.randrange(250, 350)

        speed = [-10,-5,5,10]

        # Choose a random speed
        self.speed_x = random.choice(speed)
        self.speed_y = random.choice(speed)
        if self.speed_x == 0:
            self.speed_x = random.randrange(-10, 10)
        if self.speed_x > 11:
            self.speed_x = random.randrange(-10, 10)
        if self.speed_x < -11:
            self.speed_x = random.randrange(-10, 10)
        if self.speed_y == 0:
            self.speed_y = random.randrange(-10, 10)
        if self.speed_y > 11:
            self.speed_y = random.randrange(-10, 10)
        if self.speed_y < -11:
            self.speed_y = random.randrange(-10, 10)


        # Choose a random size
        self.radius = random.randrange(1,5)
        self.height = random.randrange(10,30)
        # Choose a random colour
        Brown1 = (244,164,96)
        Brown2 = (210,180,140)
        Brown3 = (222,184,135)
        Brown4 = (255,228,196)
        White = (255,255,255)
        Colour = [White]
        self.colour = (random.choice(Colour))

    def update(self):

        Tie = pygame.image.load('Tie.gif')
        Xwing = pygame.image.load('Xwing.png')

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Bounce off the walls
        if self.pos_x < 0:
            self.pos_x = window_width
        if self.pos_x > window_width:
            self.pos_x = 0

        if self.pos_y < 0:
            self.pos_y = window_height
        if self.pos_y > window_height:
            self.pos_y = 0

        screen.blit(Tie,(self.pos_x,self.pos_y))
        screen.blit(Xwing, (self.pos_x - 60, self.pos_y - 60))

    def draw(self):
        print "This should never be called"

class Tie(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        width = self.radius
        height = self.height
        Tie = pygame.image.load('Tie.gif')

class Xwing(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        width = self.radius
        height = self.height
        Xwing = pygame.image.load('Xwing.png')



def Gbolt(screen):
    for Y in xrange(window_height):
        for X in xrange(window_width):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (Red/2, 255, Blue/2)

def Bbolt(screen):
    for Y in xrange(window_height):
        for X in xrange(window_width):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (Red/2, Green/2, 255)

def Rbolt(screen):
    for Y in xrange(window_height):
        for X in xrange(window_width):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (255, Green/2, Blue/2)


pygame.init()
clock = pygame.time.Clock()

window_width = 800
window_height = 600
imgX = 0
imgY = 0
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size,0,24)
BackGround = pygame.image.load('ShipBridge.png')
# Initialise lists for ball data
balls = []

# Create balls
num_balls = 10
for ball_index in xrange(num_balls):
    shape = random.choice([Tie,Xwing])
    new_ball = shape()
    balls.append(new_ball)

Black = (0,0,0)

# Main loop
running = True
while running:

    screen.fill(Black)
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen to black
    for ball in balls:
        ball.draw()
        ball.update()

    screen.blit(BackGround,(imgX,imgY))
    imgX = 0
    imgY = 0
    pxarray = pygame.PixelArray(screen)
    if keys_pressed[K_SPACE]:
        imgY += 5

    if keys_pressed[K_UP]:
        Gbolt(BackGround)

    if keys_pressed[K_RIGHT]:
        Bbolt(BackGround)

    if keys_pressed[K_DOWN]:
        Rbolt(BackGround)



    del pxarray
    pygame.display.update()
    clock.tick(60)
