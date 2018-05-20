import pygame, random, sys
from pygame import *

WHITE = 255, 255, 255
DARKRED = 210, 15, 0
RED = 250, 150, 150
GREEN = 110, 235, 120
BLUE = 160, 180, 255
GOLD = 220, 210, 60
GREY = 165, 155, 155
BLACK = 0, 0, 0

def game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    bgImg = pygame.image.load("./image/background.png").convert()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.quit()
                sys.exit()

        screen.blit(bgImg, (0, 0))
        pygame.display.update()

def blackScreen():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    screen.fill(BLACK)
    font = pygame.font.Font("BlackDahlia.ttf", 40)
    text = font.render("FLOOR ZERO", True, WHITE)
    screen.blit(text, (220, 200))
    pygame.display.update()
    pygame.time.wait(2000)
	
