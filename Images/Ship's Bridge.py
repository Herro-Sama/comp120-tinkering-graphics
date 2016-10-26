import pygame, sys, random, time
from pygame.locals import *

class Ball:
    def __init__(self):
        # Choose a random position
        self.pos_x = random.randrange(350, 450)
        self.pos_y = random.randrange(250, 350)

        # Choose a random speed
        self.speed_x = random.randrange(-10, 10)
        self.speed_y = random.randrange(-10, 10)
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
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Bounce off the walls
        if self.pos_x < 0:
            self.pos_x = random.randrange(350, 450)
        if self.pos_x > window_width:
            self.pos_x = random.randrange(350, 450)

        if self.pos_y < 0:
            self.pos_y = random.randrange(250, 350)
        if self.pos_y > window_height:
            self.pos_y = random.randrange(250, 350)

        if keys_pressed[K_s]:
            self.speed_x = random.randrange (-10, 10)
            self.speed_y = random.randrange (-10, 10)

        if self.speed_x and self.speed_y >= 1:
            self.image = pygame.transform.rotate(self.image, 45)


    def draw(self):
        print "This should never be called"

class CircleBall(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        width = self.radius
        height = self.height
        self.image = pygame.draw.rect(screen, self.colour, (pos_x, pos_y, width, height ))

    def resize(self):
        self.radius -= 1
        if self.radius < 1:
            self.radius = random.randrange(5,10)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file,location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# Initialise PyGame
pygame.init()
clock = pygame.time.Clock()

window_width = 800
window_height = 600
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
BackGround = Background('ShipBridge.png', [0,0])
# Initialise lists for ball data
balls = []

# Create balls
num_balls = 100
for ball_index in xrange(num_balls):
    shape = random.choice([CircleBall])
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
        ball.resize()


    screen.blit(BackGround.image, BackGround.rect)
    # Flip the display and regulate the frame rate
    pygame.display.flip()
    clock.tick(60)
