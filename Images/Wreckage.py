import pygame
import random

class Ball:
    def __init__(self):
        # Choose a random position
        self.pos_x = random.randrange(0, window_width)
        self.pos_y = random.randrange(0, window_height)

        # Choose a random speed
        self.speed_x = random.randrange(-5, 5)
        self.speed_y = random.randrange(-5, 5)

        # Choose a random size
        self.radius = random.randrange(2, 20)

        # Choose a random colour
        red = random.randrange(180, 255)
        green = random.randrange(50, 60)
        blue = random.randrange(0, 90)
        self.colour = (red, green, blue)

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Bounce off the walls
        if self.pos_x < 0:
            self.pos_x += window_width
        if self.pos_x > window_width:
            self.pos_x -= 0

        if self.pos_y < 0:
            self.pos_y += window_height
        if self.pos_y > window_height:
            self.pos_y -= 0

    def draw(self):
        print "This should never be called"


class SquareBall(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        radius = self.radius
        rect = (pos_x - radius, pos_y - radius, 2 * radius, 2 * radius)
        pygame.draw.rect(screen, self.colour, rect)


class CircleBall(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        radius = self.radius
        pygame.draw.circle(screen, self.colour, (pos_x, pos_y), radius)


class TriangleBall(Ball):
    def draw(self):
        pos_x = self.pos_x
        pos_y = self.pos_y
        radius = self.radius
        points = [(pos_x - radius, pos_y + radius), (pos_x, pos_y - radius), (pos_x + radius, pos_y + radius)]
        pygame.draw.polygon(screen, self.colour, points)

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
BackGround = Background('wreckage.jpg', [0,0])
# Initialise lists for ball data
balls = []

# Create balls
num_balls = 100
for ball_index in xrange(num_balls):
    shape = random.choice([CircleBall])
    new_ball = shape()
    balls.append(new_ball)

# Main loop
running = True

screen.blit(BackGround.image, BackGround.rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen to black
    for ball in balls:
        ball.draw()
        ball.update()
        object.blit(ball)
    # Flip the display and regulate the frame rate
    pygame.display.flip()
    clock.tick(120)
