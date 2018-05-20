## V5.2
## David Duan

import sys, time, pygame
from pygame import *

from Player import *
from Princess import *
from MrAgnew import *

from SystemFunction import *
from SystemClassV3 import *
from SystemObject import *
from MonsterObject import *
from Dialogue import *

from FloorMap import FloorMap
from DataDict import DATADICT, ConvList, SwordList

pygame.init()
screen = pygame.display.set_mode((640, 480))

WHITE = 255, 255, 255
DARKRED = 210, 15, 0
RED = 250, 150, 150
GREEN = 110, 235, 120
BLUE = 160, 180, 255
GOLD = 220, 210, 60
GREY = 165, 155, 155
YELLOW = 230, 230, 35
BROWN = 204, 102, 0
PURPLE = 178, 102, 255

def main():
    pygame.display.set_caption("Tower of the Sorcerer")
    clock = pygame.time.Clock()

    bgImg = pygame.image.load("./imgSource/System/bgImg.jpg").convert()
    bgImg = pygame.transform.scale(bgImg, (640, 480))

    pygame.mixer.music.load("./Audio/introBGM.mid")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    select = pygame.mixer.Sound("./Audio/select.ogg")
    select.set_volume(0.3)

    fontFile1 = "./Font/BlackDahlia.ttf"
    title = TextButton(screen, "Tower of the Sorcerer", fontFile1, 60, WHITE, WHITE, 35, 80)
    start = TextButton(screen, "Start", fontFile1, 40, GREY, GREEN, 250, 190)
    load = TextButton(screen, "Continue", fontFile1, 40, GREY, GOLD, 250, 240)
    info = TextButton(screen, "Information", fontFile1, 40, GREY, BLUE, 250, 290)
    setting = TextButton(screen, "Setting",  fontFile1, 40, GREY, PURPLE, 250, 340)
    end = TextButton(screen, "Quit", fontFile1, 40, GREY, RED, 250, 390)

    start.selected = True
    statusList = ['start', 'load', 'info', 'setting', 'end']
    current = 0
    done = False
    while not done:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    select.play()
                    if current == 4:current = 0
                    else:current += 1
                    for elem in statusList:
                        exec(elem + '.selected = False')
                    exec(statusList[current] + '.selected = True')
                elif event.key == pygame.K_RETURN:
                    if current == 2: information(screen)
                    elif current == 3: pass # <<Setting>>
                    elif current == 4:
                        pygame.mixer.music.stop()
                        display.quit()
                        sys.exit()
                    elif current == 1: pass # <<Continue>>
                    elif current == 0:
                        global playerName
                        #playerName = input('Enter your name: ')
                        #blackScreen("FLOOR ZERO", 1)
                        game()
                        
        screen.blit(bgImg, (0, 0))
        title.display()
        start.display()
        load.display()
        info.display()
        setting.display()
        end.display()
        
        pygame.display.update()


initDialogue = False
dialogueGroup = pygame.sprite.Group()
pickupGroup = pygame.sprite.Group()
targetObj = None
targetNum = -999
playerNameStr = ''
princessName = 'Princess'
pickup = False
pickupObj = None
def game():
    screen = pygame.display.set_mode((900, 550))
    clock = pygame.time.Clock()
    bottomLayer = pygame.Surface((900, 550)).convert()
    bottomLayer.fill(BLACK)
    background = Background(screen)

    sprites = pygame.sprite.OrderedUpdates()
    sidebar = pygame.sprite.Group()

    list_of_all_groups = list(pygame.sprite.Group() for x in range(5))
    map_object = list(list(list(None for a in range(15)) for b in range(15))for c in range(5))

    player = Player(screen, 7, 14)
    princess = Princess(screen, -999, -999)
    
    global FloorMap
    global playerNameStr, princessName
    for floor in range(len(FloorMap)):
        for row in range(15): 
            for column in range(15):
                dataNum = FloorMap[floor][row][column]
                if dataNum in [1, 2, 3, 4, 5]: # Wall
                    map_object[floor][row][column] = Wall(screen, -999, -999, dataNum)
                if dataNum in [-10, -9, -8]: # Grass for intro level
                    map_object[floor][row][column] = Grass(screen, -999, -999, dataNum)
                if dataNum in list(range(221, 231)): # Door
                    map_object[floor][row][column] = Door(screen, -999, -999, dataNum)
                if dataNum in list(range(201, 211)): # Key
                    map_object[floor][row][column] = Key(screen, -999, -999, dataNum)
                if dataNum in [11, 12, 13, 14, 15]: # Potion
                    map_object[floor][row][column] = Potion(screen, -999, -999, dataNum)
                if dataNum in list(range(21, 31)): # Gem
                    map_object[floor][row][column] = Gem(screen, -999, -999, dataNum)
                if dataNum in list(range(501, 521)): # Monsters
                    _data = DATADICT[FloorMap[floor][row][column]]
                    map_object[floor][row][column] = NormalMonster(screen, -999, -999,\
                        dataNum, _data[0], _data[1], _data[2], _data[3])
                if dataNum in [91, 92, 91.5]: # Stairs
                    map_object[floor][row][column] = Stair(screen, -999, -999, dataNum)
                if dataNum in list(range(51, 61)): # Swords
                    map_object[floor][row][column] = Sword(screen, -999, -999, dataNum)
                if dataNum == 801:
                    map_object[floor][row][column] = MrAgnewF1(screen, -999, -999, dataNum)
                if dataNum == 99:
                    player = Player(screen, -999, -999)
                    map_object[floor][row][column] = player
                if dataNum == -99:
                    map_object[floor][row][column] = Bones(screen, -999, -999)
                if dataNum == 100:
                    princess = Princess(screen, -999, -999)
                    map_object[floor][row][column] = princess
                if dataNum == 101:
                    princess = PrincessF0(screen, -999, -999)
                    map_object[floor][row][column] = princess
                if dataNum == 102:
                    princess = PrincessF0Far(screen, -999, -999)
                    map_object[floor][row][column] = princess
                if dataNum == 103:
                    princess = PrincessF1(screen, 'Hi', -999, -999)
                    map_object[floor][row][column] = princess
                    
                if map_object[floor][row][column]:
                   list_of_all_groups[0].add(map_object[floor][row][column])

        sprites.add(background)
        sprites.add(list_of_all_groups)


    player.setX(7)
    player.setY(14)
    current_floor = 0

    while True:
        sprites.clear(screen, bottomLayer)

        sprites.update()

        sprites.draw(screen)
        
        pygame.display.flip()




main()


















