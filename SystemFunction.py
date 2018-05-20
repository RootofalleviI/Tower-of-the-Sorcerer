## Function File
import pygame
from pygame import *
from SystemObject import *
from MonsterObject import *

WHITE = 255, 255, 255
DARKRED = 210, 15, 0
RED = 250, 150, 150
GREEN = 110, 235, 120
BLUE = 160, 180, 255
GOLD = 220, 210, 60
GREY = 165, 155, 155
BLACK = 0, 0, 0

def blackScreen(string, seconds):
    pygame.init()
    screen = pygame.display.set_mode((900, 550))
    screen.fill(BLACK)
    font = pygame.font.Font("./Font/BlackDahlia.ttf", 40)
    text = font.render(string, True, WHITE)
    screen.blit(text, (350, 250))
    pygame.display.update()
    pygame.time.wait(seconds * 1000)


def information(screen):
    screen = pygame.display.set_mode((640, 480))
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen = pygame.display.set_mode((900, 550))
                    done = True

        bgImg = pygame.image.load("./imgSource/System/bgImg.jpg").convert()
        bgImg = pygame.transform.scale(bgImg, (640, 480))
        screen.blit(bgImg, (0, 0))

        fontTitle = pygame.font.Font("./Font/BlackDahlia.ttf", 32)
        fontText = pygame.font.Font("./Font/BlackDahlia.ttf", 30)
        fontPrompt = pygame.font.Font("./Font/PAPYRUS.ttf", 25)

        message = ('', '', \
                       'Press ARROW KEYS to move', \
                       'Press SPACE to select options', \
                       'Press ENTER to confirm', \
                       #'Please keep your SHELL open for dialogues',
                       '', '', '', \
                       '                                 Developed by David Duan')
        textList = []
        for line in message:
            textList.append(fontText.render(line, True, (160, 180, 255)))

        for i in range(len(textList)):
            screen.blit(textList[i], (40, 35 * i + 100))
        line1 = fontTitle.render("You are a warrior to fight against the darkness", True,  (250, 150, 150))
        screen.blit(line1, (5, 50))
        systemText = fontPrompt.render("Press Enter...", True, (255, 255, 255))
        screen.blit(systemText, (450, 430))
        
        pygame.display.update()


def inputVal(screen, message):
    screen = pygame.display.set_mode((900, 550))
    current_string = []
    font = pygame.font.Font('./Font/printer.ttf', 40)
    sysFont = pygame.font.Font('./Font/PAPYRUS.TTF', 30)
    pygame.draw.rect(screen, WHITE, (600, 290, 150, 2), 3)
    done = False
    while not done:
        for event in pygame.event.get():
            keyinput = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    current_string = current_string[0: -1]
                    increment = current_string.count('i')
                    pygame.draw.rect(screen, BLACK, (600 + len(current_string) * 10 - 15 * increment,
                                                     250, 250 - len(current_string) * 20 +  20 * increment, 40))
                elif event.key == K_RETURN:
                    done = True
                elif event.key == K_MINUS:
                    current_string.append("_")
                elif 32 <= event.key <= 127 and len(current_string) < 8:
                    if keyinput[K_LSHIFT]:
                        event.key -= 32
                    current_string.append(chr(event.key))
                pygame.draw.rect(screen, WHITE, (600, 290, 150, 2), 3)
                if len(current_string) != 0:
                    image = sysFont.render(''.join(current_string), True, WHITE)
                    screen.blit(image, (600, 250))
            prompt = sysFont.render(message, True, WHITE)
            screen.blit(prompt, (100, 252))
            pygame.display.flip()
    screen.fill(BLACK)
    return ''.join(current_string)

def helpScreen(screen):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True

        bgImg = pygame.image.load("./imgSource/System/bgImg.jpg").convert()
        bgImg = pygame.transform.scale(bgImg, (640, 480))
        screen.blit(bgImg, (0, 0))

        fontTitle = pygame.font.Font("./Font/BlackDahlia.ttf", 32)
        fontText = pygame.font.Font("./Font/BlackDahlia.ttf", 30)
        fontPrompt = pygame.font.Font("./Font/PAPYRUS.ttf", 25)

        message = ('', '', \
                       'Press ARROW KEYS to move', \
                       'Press SPACE to select options', \
                       'Press ENTER to confirm', \
                       'Please keep your SHELL open for dialogues', '', '', \
                       '                                 Developed by David Duan')
        textList = []
        for line in message:
            textList.append(fontText.render(line, True, (160, 180, 255)))

        for i in range(len(textList)):
            screen.blit(textList[i], (40, 35 * i + 100))
        line1 = fontTitle.render("You are a warrior to fight against the darkness", True,  (250, 150, 150))
        screen.blit(line1, (5, 50))
        systemText = fontPrompt.render("Press Enter...", True, (255, 255, 255))
        screen.blit(systemText, (450, 430))
        
        pygame.display.update()
'''
pygame.init()
screen = pygame.display.set_mode((900, 550))
yourname = inputVal(screen, "Enter your name (8 char max):")
princessname = inputVal(screen, "Enter her name (8 char max):")
'''


    
