# This code is from Tech with Tim Pygame Tutorial videos
import pygame
pygame.init()

# Top left of display is 0,0
# Bottom right of display is 500, 500
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pong Escape")

score = 0

class paddle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8 # how many pixels we can move by

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

class circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.yVel = 4 # how many pixels we can move by
        self.xVel = 4 # how many pixels we can move by

    def draw(self, win):
        self.move()
        pygame.draw.circle(win, (0,255,0), (self.x, self.y), self.radius)

    def move(self):
        if self.x < 500 - self.radius and self.x > 0 + self.radius:
            self.x += self.xVel
        else:
            self.xVel = self.xVel * -1
            self.x += self.xVel

        if self.y > 0 + self.radius:
            self.y += self.yVel
        else:
            self.yVel = self.yVel * -1
            self.y += self.yVel

def lose():
    font1 = pygame.font.SysFont('8-Bit-Madness', 100)
    text = font1.render('Game Over', 1, (255,0,0))
    # want text in the middle of screen
    win.blit(text, (250 - (text.get_width()/2), 240 - (text.get_height()/2)))
    pygame.display.update()
    keys = pygame.key.get_pressed()
    quit = False
    while quit == False:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                pygame.quit()

def redrawGameWindow():
    pad.draw(win)
    ball.draw(win)
    text = font.render('Score: ' + str(score), 1, (255,0,0))
    win.blit(text, (390, 10))
    pygame.display.update()

# font name, size, bold, italic
font = pygame.font.SysFont('8-Bit-Madness', 30, True)
pad = paddle(210, 480, 48, 10)
ball = circle(100, 300, 6)

run = True
while run:
    pygame.time.delay(25)

    if ball.y + ball.radius > pad.y and ball.x > pad.x and ball.x < (pad.x + pad.width):
        # divide by (pad.width/2)/4 because we need total paddle with to be 8
        # 48/2 = 24. 24/4 = 6
        distanceFromCentreOfPaddle = int((ball.x - (pad.x + pad.width/2)) / ((pad.width/2)/4))
        print(distanceFromCentreOfPaddle)
        # Tan -1 (4) = 75 degress (angle we want ball to go at if ball hits edge of paddle)
        # Therefore, xVel must be 4 times yVel if we hit here. 
        ball.xVel = ball.yVel * distanceFromCentreOfPaddle
        ball.yVel = ball.yVel * -1
        ball.y += ball.yVel
        score += 1
    elif ball.y + ball.radius > pad.y and (ball.x < pad.x or ball.x > (pad.x + pad.width)):
        lose()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # position of rect is from top left corner, therefore
    # > vel rather than > 0 because if we were at position x = 0,
    # we could still move 5 pixels to the left
    if keys[pygame.K_LEFT] and pad.x > pad.vel:
        pad.x -= pad.vel
    # - width because 0 is in top left, not right
    if keys[pygame.K_RIGHT] and pad.x < 500 - pad.width - pad.vel:
        pad.x += pad.vel


    win.fill((0,0,0))  # Fills the screen with black
    # pygame.draw.rect(win, (255,0,0), (x, y, width, height)) 
    # pygame.draw.circle(win, (0, 255, 0), )  
    # pygame.display.update() 
    redrawGameWindow()

pygame.quit()