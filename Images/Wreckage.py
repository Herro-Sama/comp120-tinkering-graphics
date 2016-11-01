import pygame, sys, random, time
from pygame.locals import *

class Ball:
    def __init__(self):
        # Choose a random position
        self.pos_x = random.randrange(0, window_width)
        self.pos_y = random.randrange(0, window_height)

        # Choose a random speed
        self.speed_x = random.randrange(-10, 10)
        self.speed_y = random.randrange(-10, 10)

        # Prevent balls from being stationary or too fast
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
        self.radius = random.randrange(1,6)

        # Choose a colour from the list
        Brown1 = (244,164,96)
        Brown2 = (210,180,140)
        Brown3 = (222,184,135)
        Brown4 = (255,228,196)
        Colour = [Brown1,Brown2,Brown3,Brown4]
        self.colour = (random.choice(Colour))

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Transfer position x to opposite side of the screen
        if self.pos_x < 0:
            self.pos_x = window_width
        if self.pos_x > window_width:
            self.pos_x = 0

        # Transfer position y to opposite side of the screen
        if self.pos_y < 0:
            self.pos_y = window_height
        if self.pos_y > window_height:
            self.pos_y = 0

        # Unify the direction balls are traveling
        if keys_pressed[K_s]:
            self.speed_x = random.randrange (1, 10)
            self.speed_y = random.randrange (1, 10)
        if keys_pressed[K_w]:
            self.speed_x = random.randrange (-10, 0)
            self.speed_y = random.randrange (-10, 0)

    # Test code to try resize balls
    def resize(self):
        if keys_pressed[K_d]:
            self.radius = self.radius + 1
        if keys_pressed[K_a]:
            self.radius = self.radius - 1

        if self.radius >= 6:
            self.radius = 5
        if self.radius <= 0:
            self.radius = 1

    def draw(self):
        print "This should never be called"

# Draw the particles on the screen
class Particle(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        radius = self.radius
        pygame.draw.circle(screen, self.colour, (pos_x, pos_y), radius)

# Create background image
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# Initialise PyGame
pygame.init()
clock = pygame.time.Clock()

window_width = 1280
window_height = 600
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
BackGround = Background('wreckage.jpg', [0,0])
# Initialise lists for ball data
balls = []

# Create particles
num_particles = 3000
for ball_index in xrange(num_particles):
    shape = random.choice([Particle])
    new_ball = shape()
    balls.append(new_ball)
Black = (0,0,0)

# Main loop
running = True
while running:
    # Add background image and activate key presses
    screen.fill(Black)
    screen.blit(BackGround.image, BackGround.rect)
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen to black
    for ball in balls:
        ball.draw()
        ball.update()
        ball.resize()

    # Flip the display and regulate the frame rate
    pygame.display.flip()
    clock.tick(60)
