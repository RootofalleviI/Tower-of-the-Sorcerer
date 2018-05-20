## V5.1
## David Duan

import sys, time, pygame
from pygame import *
from SystemFunction import *
from SystemClassV3 import *
from ObjectClassP1V3 import *
from ObjectClassP2V3 import *
from Player import *
from MrAgnew import *
from Princess import *
from Dialogue import *
from DataDict import DATADICT
from FloorMap import FloorMap


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

playerName = ''
def main():
    pygame.display.set_caption("Tower of the Sorcerer")

    bgImg = pygame.image.load("./imgSource/System/bgImg.jpg").convert()
    bgImg = pygame.transform.scale(bgImg, (640, 480))

    pygame.mixer.music.load("./Audio/introBGM.mid")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    select = pygame.mixer.Sound("./Audio/select.ogg")
    select.set_volume(0.3)
    clock = pygame.time.Clock()
    
    title = TextButton(screen, "Tower of the Sorcerer", \
                       "./Font/BlackDahlia.ttf", 60, WHITE, WHITE, 35, 80)
    start = TextButton(screen, "Start", "./Font/BlackDahlia.ttf",\
                       40, GREY, GREEN, 250, 190)
    load = TextButton(screen, "Continue", "./Font/BlackDahlia.ttf", \
                      40, GREY, GOLD, 250, 240)
    info = TextButton(screen, "Information", "./Font/BlackDahlia.ttf",
                      40, GREY, BLUE, 250, 290)
    setting = TextButton(screen, "Setting",  "./Font/BlackDahlia.ttf",
                      40, GREY, PURPLE, 250, 340)
    end = TextButton(screen, "Quit", "./Font/BlackDahlia.ttf",
                     40, GREY, RED, 250, 390)

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
                    if current == 4:
                        current = 0
                    else:
                        current += 1
                    for elem in statusList:
                        code = elem + '.selected = False'
                        exec(code)
                    exec(statusList[current] + '.selected = True')
                elif event.key == pygame.K_RETURN:
                    if current == 2:
                        information(screen)
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
        
dialogue = False
dialogueGroup = pygame.sprite.Group()
obj = None
def game():
    screen = pygame.display.set_mode((900, 550))
    clock = pygame.time.Clock()
    bottomLayer = pygame.Surface((640, 480)).convert()
    bottomLayer.fill(BLACK)
    background = Background(screen)
    
    sprites = pygame.sprite.OrderedUpdates()
    sidebar = pygame.sprite.Group()
    

    list_of_all_groups = list(pygame.sprite.Group() for x in range(4))
    map_object = list(list(list(None for a in range(15)) for b in range(15))for c in range(4))

    global FloorMap
    for floor in range(len(FloorMap)):
        for row in range(15):
            for column in range(15):
                if FloorMap[floor][row][column] == -11:
                    map_object[floor][row][column] = FlowerMore(screen, -999, -999)
                if FloorMap[floor][row][column] == -12:
                    map_object[floor][row][column] = FlowerLess(screen, -999, -999)
                if FloorMap[floor][row][column] == -4:
                    map_object[floor][row][column] = WallLightGrey(screen, -999, -999)
                if FloorMap[floor][row][column] == -3:
                    map_object[floor][row][column] = WallBlue(screen, -999, -999)
                if FloorMap[floor][row][column] == -2:
                    map_object[floor][row][column] = Grass(screen, -999, -999)
                if FloorMap[floor][row][column] == -1:
                    map_object[floor][row][column] = WallGrey(screen, -999, -999)
                if FloorMap[floor][row][column] == 0: # Wall
                    map_object[floor][row][column] = Wall(screen, -999, -999)
                if FloorMap[floor][row][column] == 1: # Empty
                    pass
                if FloorMap[floor][row][column] in list(range(221, 231)): # Door
                    data = FloorMap[floor][row][column]
                    map_object[floor][row][column] = Door(screen, -999, -999, data)
                if FloorMap[floor][row][column] in list(range(201, 211)): # Keys
                    data = FloorMap[floor][row][column]
                    map_object[floor][row][column] = Key(screen, -999, -999, data)
                if FloorMap[floor][row][column] in [11, 12]:
                    data = FloorMap[floor][row][column]
                    map_object[floor][row][column] = Potion(screen, -999, -999, data)
                if FloorMap[floor][row][column] in list(range(21, 31)):
                    data = FloorMap[floor][row][column]
                    map_object[floor][row][column] = Gem(screen, -999, -999, data)
                if FloorMap[floor][row][column] in list(range(501, 521)):
                    data = FloorMap[floor][row][column]
                    _data = DATADICT[FloorMap[floor][row][column]]
                    map_object[floor][row][column] = NormalMonster(screen, -999, -999,\
                        data, _data[0], _data[1], _data[2], _data[3])
                if FloorMap[floor][row][column] == 801:
                    data = FloorMap[floor][row][column]
                    map_object[floor][row][column] = MrAgnewF0(screen, -999, -999, data)
                if FloorMap[floor][row][column] == 99:
                    player = Player(screen, -999, -999)
                    map_object[floor][row][column] = player
                if FloorMap[floor][row][column] == 101:
                    princess = PrincessF0(screen, -999, -999)
                    map_object[floor][row][column] = princess
                if FloorMap[floor][row][column] in [91, 92]:
                    data = FloorMap[floor][row][column]
                    map_object[floor][row][column] = Stair(screen, -999, -999, data)
                    
                if map_object[floor][row][column] != None :
                   list_of_all_groups[0].add(map_object[floor][row][column])

        sprites.add(background)
        sprites.add(list_of_all_groups)

    playerx = 7
    playery = 14
    player.setX(playerx)
    player.setY(playery)
    current_floor = 0

    global playerName
    global dialogueGroup, dialogue
    player.name = playerName

    ytracker = Icon(screen, player, "./imgSource/System/Items/ykeys.png", BLACK, 30, 260)
    btracker = Icon(screen, player, "./imgSource/System/Items/bkeys.png", BLACK, 30, 300)
    rtracker = Icon(screen, player, "./imgSource/System/Items/rkeys.png", BLACK, 30, 340)
    goldtracker = Icon(screen, player, "./imgSource/System/Items/gold.png", BLACK, 30, 383)
    lvltracker = StatusLevel(screen, player)    
    playericon = Icon(screen, player, 'player.getimage()', WHITE, 30, 50, (40, 40))
    playername = String(screen, player, "./Font/FestivalBudayaXXXI.otf", 20, 'getname()', \
                        (128, 128, 128), 80, 25)

    dmgtracker = Icon(screen, player, "./imgSource/System/dmgIcon.png", WHITE, 680, 43)
    deftracker = Icon(screen, player, "./imgSource/System/defIcon.png", WHITE, 680, 83)
    hptracker = Icon(screen, player, "./imgSource/System/hpIcon.png", WHITE, 680, 123)
    getykey = YKeyNumber(screen, player)
    getbkey = BKeyNumber(screen, player)
    getrkey = RKeyNumber(screen, player)
    getgold = GoldNumber(screen, player)
    getdmg = DmgNumber(screen, player)
    getdef = DefNumber(screen, player)
    gethp = HpNumber(screen, player)
    sidebar.add(ytracker, btracker, rtracker, getykey, getbkey, getrkey, lvltracker,\
                playericon, playername, goldtracker, getgold, dmgtracker, deftracker, \
                hptracker, getdmg, getdef, gethp) 

    x = 1
    done = False
    while not done:
        if x == 0: # Smooth Movement but FPS lag
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            playerx = int((player.getX() - 160) / 32)
            playery = int(player.getY() / 32)
            
            keys = pygame.key.get_pressed()
            if keys[K_LSHIFT] or keys[K_RSHIFT]: # if SHIFT is pressed: increase movement speed
                clock.tick(30)
            else:
                clock.tick(12)
            if keys[K_UP]:
                player.changeimage(3)
                if movable( player, map_object,FloorMap, current_floor,playerx, playery-1):
                    FloorMap[current_floor][playery-1][playerx]= 99
                    FloorMap[current_floor][playery][playerx] = 1
                    map_object[current_floor][playery-1][playerx]= player
                    map_object[current_floor][playery][playerx] = None
            if keys[K_DOWN]:
                player.changeimage(0)
                if movable( player, map_object, FloorMap, current_floor,playerx, playery+1):
                    FloorMap[current_floor][playery+1][playerx]= 99
                    FloorMap[current_floor][playery][playerx] = 1
                    map_object[current_floor][playery+1][playerx]= player
                    map_object[current_floor][playery][playerx] = None
            if keys[K_LEFT]:
                player.changeimage(1)
                if movable( player, map_object, FloorMap, current_floor,playerx-1, playery):
                    FloorMap[current_floor][playery][playerx-1]= 99
                    FloorMap[current_floor][playery][playerx] = 1
                    map_object[current_floor][playery][playerx-1]= player
                    map_object[current_floor][playery][playerx] = None
            if keys[K_RIGHT]:
                player.changeimage(2)
                if movable( player, map_object, FloorMap,current_floor,playerx+1, playery):
                    FloorMap[current_floor][playery][playerx+1]= 99
                    FloorMap[current_floor][playery][playerx] = 1
                    map_object[current_floor][playery][playerx+1]= player
                    map_object[current_floor][playery][playerx] = None
                            
            getykey.setykey(player)
            getbkey.setbkey(player)
            getrkey.setrkey(player)
            getgold.setgold(player)
            lvltracker.setlevel(player)

            for row in range(15):
                for column in range(15):
                    if map_object[current_floor][row][column] != None:
                        map_object[current_floor][row][column].setX(column)
                        map_object[current_floor][row][column].setY(row)

        else: # Normal Movement
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    display.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    playerx = int((player.getX() - 160) / 32)
                    playery = int(player.getY() / 32)

                    if event.key == pygame.K_UP:
                        player.changeimage(3)
                        if movable(player, map_object,FloorMap, current_floor,playerx, playery-1):
                            FloorMap[current_floor][playery-1][playerx]= 99
                            FloorMap[current_floor][playery][playerx] = 1
                            map_object[current_floor][playery-1][playerx]= player
                            map_object[current_floor][playery][playerx] = None

                    if event.key == pygame.K_DOWN:
                        player.changeimage(0)
                        if movable(player, map_object, FloorMap, current_floor,playerx, playery+1):
                            FloorMap[current_floor][playery+1][playerx]= 99
                            FloorMap[current_floor][playery][playerx] = 1
                            map_object[current_floor][playery+1][playerx]= player
                            map_object[current_floor][playery][playerx] = None

                    if event.key == pygame.K_LEFT:
                        player.changeimage(1)
                        if movable(player, map_object, FloorMap, current_floor,playerx-1, playery):
                            FloorMap[current_floor][playery][playerx-1]= 99
                            FloorMap[current_floor][playery][playerx] = 1
                            map_object[current_floor][playery][playerx-1]= player
                            map_object[current_floor][playery][playerx] = None

                    if event.key == pygame.K_RIGHT:
                        player.changeimage(2)
                        if movable(player, map_object, FloorMap,current_floor,playerx+1, playery):
                            FloorMap[current_floor][playery][playerx+1]= 99
                            FloorMap[current_floor][playery][playerx] = 1
                            map_object[current_floor][playery][playerx+1]= player
                            map_object[current_floor][playery][playerx] = None
                    
                    getykey.setykey(player)
                    getbkey.setbkey(player)
                    getrkey.setrkey(player)
                    getgold.setgold(player)
                    lvltracker.setlevel(player)
                    getdmg.setdmg(player)
                    getdef.setdef(player)
                    gethp.sethp(player)

                for row in range(15):
                    for column in range(15):
                        if map_object[current_floor][row][column] != None:
                            map_object[current_floor][row][column].setX(column)
                            map_object[current_floor][row][column].setY(row)
        
        sprites.clear(screen, bottomLayer)
        sidebar.clear(screen, bottomLayer)
        
        sprites.update()
        sidebar.update()
        
        sprites.draw(screen)
        sidebar.draw(screen)

        
        if dialogue:
            enter = PressEnter(screen)
            dialogueList = obj.dialogueList
            xd = True
            while dialogueList:
                if dialogueList[0][0] != '!':   
                    speakerIcon = ConvIcon(screen, obj.image)
                    speakerName = ConvName(screen, obj.name, obj.type)
                    speakerWords = ConvConv(screen, dialogueList[0])
                else:
                    speakerIcon = ConvIcon(screen, player.icon)
                    speakerName = ConvName(screen, player.getname(), "Player")
                    speakerWords = ConvConv(screen, dialogueList[0][1:])
                dialogueGroup.add(speakerIcon, speakerName, enter)
                if xd:
                    dialogueGroup.add(speakerWords)
                    xd = False
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            dialogueList = dialogueList[1:]
                            dialogueGroup.empty()
                            xd = True
                            
                dialogueGroup.clear(screen, bottomLayer)
                sprites.clear(screen, bottomLayer)
                sidebar.clear(screen, bottomLayer)
                sprites.update()
                sidebar.update()
                dialogueGroup.update()
                sprites.draw(screen)
                sidebar.draw(screen)
                dialogueGroup.draw(screen)
                pygame.display.flip()          
            dialogue = False
            
        pygame.display.flip()
        
def movable(player, map_object, FloorMap, current_floor, targetx, targety):
    global dialogue, obj
    if targety > 14 or targetx > 14:
        return False
    else:
        targetObj = FloorMap[current_floor][targety][targetx]
    if targetObj in [0, -1]: # Wall
        return False
    elif targetObj == 101: # Princess
        dialogue = True
        obj = map_object[current_floor][targety][targetx]
        return False
    elif targetObj in list(range(221, 232)): # Door
        if targetObj == 221:
            if player.getykey() > 0:
                map_object[current_floor][targety][targetx].kill()
                player.updateykey(-1)
                return True
            else:
                return False
        elif targetObj == 222:
            if player.getbkey() > 0:
                map_object[current_floor][targety][targetx].kill()
                player.updatebkey(-1)
                return True
            else:
                return False
        elif targetObj == 223:
            if player.getrkey() > 0:
                map_object[current_floor][targety][targetx].kill()
                player.updaterkey(-1)
                return True
            else:
                return False
    elif targetObj in list(range(201, 212)): # keys
        if targetObj == 201:
            map_object[current_floor][targety][targetx].kill()
            player.updateykey(1)
            return True
        elif targetObj == 202:
            map_object[current_floor][targety][targetx].kill()
            player.updatebkey(1)
            return True
        elif targetObj == 203:
            map_object[current_floor][targety][targetx].kill()
            player.updaterkey(1)
            return True
    elif targetObj in list(range(11, 13)): # potions
        if targetObj == 11:
            map_object[current_floor][targety][targetx].kill()
            player.updatehp(10)
            return True
        elif targetObj == 12:
            map_object[current_floor][targety][targetx].kill()
            player.updatehp(20)
            return True
    elif targetObj in list(range(21, 31)): # gems
        if targetObj == 21:
            map_object[current_floor][targety][targetx].kill()
            player.updatedmg(5)
            return True
        elif targetObj == 22:
            map_object[current_floor][targety][targetx].kill()
            player.updatedef(5)
            return True
    elif targetObj in [91, 92]: # Stairs, implemented in another function
        return False
    elif targetObj in list(range(501, 601)):
        return False
    elif targetObj in list(range(801, 810)):
        dialogue = True
        obj = map_object[current_floor][targety][targetx]
        return False
    
    return True

# Another change_floor function here

main()


















