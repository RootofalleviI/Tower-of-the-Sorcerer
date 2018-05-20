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
    ## If initDialogue == True, there will be a conversation
dialogueGroup = pygame.sprite.Group()
    ## This is just the group for dialogue-related stuff

targetObj = None
    ## The reference of target
targetNum = -999
    ## The numerical representation of target

pickupBoolean = False
targetIcon = None
pickupThing = None
pickupName = ''
amountToChange = 0
    ## Pick up stuff

monsterobject = None
monsterBoolean = False

playerNameStr = ''
princessName = 'Princess'
    ## These two are just globals 

def game():
    ## Standard set-up procedures
    screen = pygame.display.set_mode((900, 550))
    clock = pygame.time.Clock()
    bottomLayer = pygame.Surface((900, 550)).convert()
    bottomLayer.fill(BLACK)
    background = Background(screen)


    ## First major part, groups.
    sprites = pygame.sprite.OrderedUpdates()
    sidebar = pygame.sprite.Group()

    list_of_all_groups = list(pygame.sprite.Group() for x in range(11)) ## 5 needs to be changed in the future
    map_object = list(list(list(None for a in range(15)) for b in range(15))for c in range(11))
	## The last number = (total floor + 2) because I have two intro levels
	
	
    ## Initialization
    player = Player(screen, 7, 14)
    princess = Princess(screen, -999, -999)
    
    global FloorMap ## we imported this directly so we need to global it
    global playerNameStr, princessName ## and those two global strings
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
                if dataNum in list(range(61, 71)): # Shield
                    map_object[floor][row][column] = Shield(screen, -999, -999, dataNum)
                if dataNum == 801:
                    map_object[floor][row][column] = MrAgnewF1(screen, -999, -999, dataNum)
                if dataNum == 99:
                    map_object[floor][row][column] = player
                if dataNum == -99: ## Bones F
                    map_object[floor][row][column] = Bones(screen, -999, -999)
                if dataNum == 100: ## Normal Princess
                    map_object[floor][row][column] = princess
                if dataNum == 101: ## F0 first major conversation
                    princess = PrincessF0(screen, -999, -999)
                    map_object[floor][row][column] = princess
                if dataNum == 102: ## F0 far far away 
                    princess = PrincessF0Far(screen, -999, -999)
                    map_object[floor][row][column] = princess
                if dataNum == 103: ## The "nice sword" one
                    princess = PrincessF1(screen, -999, -999)
                    map_object[floor][row][column] = princess
                    
                if map_object[floor][row][column]:
                   list_of_all_groups[0].add(map_object[floor][row][column])

        sprites.add(background)
        sprites.add(list_of_all_groups)
        

    current_floor = 2
    #player.setX(3)
    #player.setY(2)

    ## Parts of the UI
    ## Gosh this is disgusting, don't touch this
    ytracker = Icon(screen, player,"./imgSource/System/Items/ykeys.png", BLACK, 30, 360)
    btracker = Icon(screen, player,"./imgSource/System/Items/bkeys.png", BLACK, 30, 400)
    rtracker = Icon(screen, player,"./imgSource/System/Items/rkeys.png", BLACK, 30, 440)
    goldtracker = Icon(screen, player,"./imgSource/System/Items/gold.png", BLACK, 30, 483)
    lvltracker = StatusLevel(screen, player)    
    playericon = Icon(screen, player,'player.getimage()', WHITE, 30, 50, (40, 40))
    playername = PlayerName(screen, player)
    dmgtracker = Icon(screen, player,"./imgSource/System/dmgIcon.png", WHITE, 30, 105)
    deftracker = Icon(screen, player,"./imgSource/System/defIcon.png", WHITE, 30, 145)
    hptracker = Icon(screen, player,"./imgSource/System/hpIcon.png", WHITE, 30, 185)
    getykey = YKeyNumber(screen, player)
    getbkey = BKeyNumber(screen, player)
    getrkey = RKeyNumber(screen, player)
    getgold = GoldNumber(screen, player)
    getdmg = DmgNumber(screen, player)
    getdef = DefNumber(screen, player)
    gethp = HpNumber(screen, player)
    sword = SwordIcon(screen, player)
    shield = ShieldIcon(screen, player)
    floortracker = FloorTracker(screen, current_floor)
    
    sidebar.add(ytracker, btracker, rtracker, getykey, getbkey, getrkey, lvltracker,\
                playericon, playername, goldtracker, getgold, dmgtracker, deftracker, \
                hptracker, getdmg, getdef, gethp, sword, shield, floortracker) 

    line1 = TextButton(screen, "Function  Key", "./Font/FestivalBudayaXXXI.otf", 18,
                       GREY, BLACK, 690, 195)
    help_ = TextButton(screen, " Help        H", "./Font/FestivalBudayaXXXI.otf", 18,
                       GREY, BLACK, 700, 220)
    info = TextButton(screen, " Info         I", "./Font/FestivalBudayaXXXI.otf", 18,
                       GREY, BLACK, 700, 243)
    load = TextButton(screen, " Load        L", "./Font/FestivalBudayaXXXI.otf", 18,
                       GREY, BLACK, 700, 266)
    save = TextButton(screen, " Save         S", "./Font/FestivalBudayaXXXI.otf", 18,
                       GREY, BLACK, 700, 289)

    ## Global these two categories
    global initDialogue, dialogueGroup
    global targetObj, targetNum
    
    finished = False ## Main boolean variable
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                display.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                
                playerx = int((player.getX() - 160) / 32)
                playery = int(player.getY() / 32)

                if event.key == pygame.K_i:
                    information(screen)
                
                if event.key == pygame.K_UP:
                    player.changeimage(3)
                    if movable(player, map_object,FloorMap, current_floor,playerx, playery-1):
                        FloorMap[current_floor][playery-1][playerx]= 99
                        FloorMap[current_floor][playery][playerx] = 0
                        map_object[current_floor][playery-1][playerx]= player
                        map_object[current_floor][playery][playerx] = None
                    
                    data_change = change_floor(player, map_object,FloorMap, current_floor, playerx, playery, playerx, playery-1)
                    current_floor = data_change[0]
                    FloorMap = data_change[1]
                    map_object = data_change[2]
                    
                    
                if event.key == pygame.K_DOWN:
                    player.changeimage(0)
                    if movable(player, map_object, FloorMap, current_floor,playerx, playery+1):
                        FloorMap[current_floor][playery+1][playerx]= 99
                        FloorMap[current_floor][playery][playerx] = 0
                        map_object[current_floor][playery+1][playerx]= player
                        map_object[current_floor][playery][playerx] = None
                    
                    data_change = change_floor(player, map_object,FloorMap, current_floor, playerx, playery, playerx, playery+1)
                    current_floor = data_change[0]
                    FloorMap = data_change[1]
                    map_object = data_change[2]
                    
                    
                if event.key == pygame.K_LEFT:
                    player.changeimage(1)
                    if movable(player, map_object, FloorMap, current_floor,playerx-1, playery):
                        FloorMap[current_floor][playery][playerx-1]= 99
                        FloorMap[current_floor][playery][playerx] = 0
                        map_object[current_floor][playery][playerx-1]= player
                        map_object[current_floor][playery][playerx] = None
                    
                    data_change = change_floor(player, map_object,FloorMap, current_floor, playerx, playery, playerx-1, playery)
                    current_floor = data_change[0]
                    FloorMap = data_change[1]
                    map_object = data_change[2]
                    
                    
                if event.key == pygame.K_RIGHT:
                    player.changeimage(2)
                    if movable(player, map_object, FloorMap,current_floor,playerx+1, playery):
                        FloorMap[current_floor][playery][playerx+1]= 99
                        FloorMap[current_floor][playery][playerx] = 0
                        map_object[current_floor][playery][playerx+1]= player
                        map_object[current_floor][playery][playerx] = None
                    
                    data_change = change_floor(player, map_object,FloorMap, current_floor, playerx, playery, playerx+1, playery)
                    current_floor = data_change[0]
                    FloorMap = data_change[1]
                    map_object = data_change[2]
                    
                ## update methods
                getykey.setykey(player)
                getbkey.setbkey(player)
                getrkey.setrkey(player)
                getgold.setgold(player)
                lvltracker.setlevel(player)
                getdmg.setdmg(player)
                getdef.setdef(player)
                gethp.sethp(player)
                playername.setname(player)
                sword.setimg(player)
                shield.setimg(player)
                floortracker.setfloor(current_floor)
               
            for row in range(15):
                for column in range(15):
                    if map_object[current_floor][row][column]:
                        map_object[current_floor][row][column].setX(column)
                        map_object[current_floor][row][column].setY(row)

        global monsterBoolean
        if monsterBoolean:
            global monsterobject
            bg = Icon(screen, player,"./imgSource/System/battle.png", BLACK, 397, 250)
            monstericon_ = MonsterIcon(screen, monsterobject)
            monsterdmg = MonsterDmg(screen, monsterobject)
            monsterdef = MonsterDef(screen, monsterobject)
            monsterhp = MonsterHP(screen, monsterobject)
            playericon_ = Icon(screen, player,'player.geticon()', WHITE, 399, 142)
            dmgicon = Icon(screen, player,"./imgSource/System/dmgIcon.png", WHITE, 367, 280)
            deficon = Icon(screen, player,"./imgSource/System/defIcon.png", WHITE, 367, 320)
            hpicon = Icon(screen, player,"./imgSource/System/hpIcon.png", WHITE, 367, 360)
            #animation = Animation(screen)
            battleGroup = pygame.sprite.Group()
            battleGroup.add(bg, monstericon_, playericon_, monsterdmg, monsterdef, monsterhp,
                            dmgicon, deficon, hpicon)#, animation)
            donewithbattle = False
            while not donewithbattle:

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #if event.key == pygame.K_RETURN:
                            battleGroup.empty()
                            donewithbattle = True

                    #player.updatehp(battleResult(player, monsterobject))
                    battleGroup.clear(screen, bottomLayer)
                    battleGroup.update()
                    battleGroup.draw(screen)
                    pygame.display.flip()
            monsterBoolean = False
            
        sprites.clear(screen, bottomLayer)
        sidebar.clear(screen, bottomLayer)

        sprites.update()
        sidebar.update()

        sprites.draw(screen)
        sidebar.draw(screen)
        
        help_.display()
        line1.display()
        save.display()
        info.display()
        load.display()
        
        ## Ok this dialogue part is also a mess
        if initDialogue:
            enter = PressEnter(screen)
            try:
                if not ConvList[targetNum]:
                    dialogueList = targetObj.dialogueList
                    ConvList[targetNum] = True
                else:
                    dialogueList = targetObj.dialogueList2
            except:
                dialogueList = targetObj.dialogueList
            notAdded = True
            
            while dialogueList:
                if dialogueList[0][0] == '@': ## Princess
                    speakerIcon = ConvIcon(screen, targetObj.icon)
                    speakerName = ConvName(screen, princessName, targetObj.type)
                    speakerWords = ConvConv(screen, dialogueList[0][1:])
                elif dialogueList[0][0] == '!': ## Player 
                    speakerIcon = ConvIcon(screen, player.icon)
                    speakerName = ConvName(screen, player.getname(), "Player")
                    speakerWords = ConvConv(screen, dialogueList[0][1:])
                else: ## NPC
                    speakerIcon = ConvIcon(screen, targetObj.icon)
                    speakerName = ConvName(screen, targetObj.name, targetObj.type)
                    speakerWords = ConvConv(screen, dialogueList[0])
                dialogueGroup.add(speakerIcon, speakerName, enter)
                if notAdded:
                    dialogueGroup.add(speakerWords)
                    notAdded = False
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            dialogueList = dialogueList[1:]
                            dialogueGroup.empty()
                            notAdded = True
                
                dialogueGroup.clear(screen, bottomLayer)
                dialogueGroup.update()
                dialogueGroup.draw(screen)
                pygame.display.flip()
            
            initDialogue = False

        
        
        global pickupBoolean
        if pickupBoolean:
            global pickupThing, amountToChange, targetIcon
            changedObj = ChangeStats(screen, amountToChange[0], int(amountToChange[1:]), pickupThing)
            enter = PressEnter(screen)
            icon = PickupIcon(screen, targetIcon)
            pickupGroup = pygame.sprite.Group()
            pickupGroup.add(changedObj, enter, icon)
            doneWithpickupBoolean = False
            while not doneWithpickupBoolean:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #if event.key == pygame.K_RETURN:
                            pickupGroup.empty()
                            doneWithpickupBoolean = True
                
                pickupGroup.clear(screen, bottomLayer)
                pickupGroup.update()
                pickupGroup.draw(screen)
                pygame.display.flip()
            pickupBoolean = False
        '''
        global battleBoolean
        if battleBoolean:
            global enemyIcon, amountToChange, targetIcon
            changedObj = ChangeStats(screen, amountToChange[0], int(amountToChange[1:]), pickupThing)
            enter = PressEnter(screen)
            icon = PickupIcon(screen, targetIcon)
            pickupGroup = pygame.sprite.Group()
            pickupGroup.add(changedObj, enter, icon)
            doneWithpickupBoolean = False
            while not doneWithpickupBoolean:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #if event.key == pygame.K_RETURN:
                            pickupGroup.empty()
                            doneWithpickupBoolean = True
                
                    pickupGroup.clear(screen, bottomLayer)
                    pickupGroup.update()
                    pickupGroup.draw(screen)
                    pygame.display.flip()
            pickupBoolean = False
        '''
        
        pygame.display.flip()



def movable(player, map_object, FloorMap, current_floor, targetx, targety):
    global initDialogue, targetObj, targetNum, princessName, SwordList
    global pickupThing, amountToChange, pickupBoolean, targetIcon
    global monsterobject, monsterBoolean

    print(targetx, targety)
    if targety > 14 or targety < 0 or targetx > 14 or targetx < 0: return False # Out of range
    else:
        target = FloorMap[current_floor][targety][targetx]
        obj = map_object[current_floor][targety][targetx]
        targetNum = target

    if target in [1, 3, 4, 5]: return False # Walls

    elif target == 102: # Special conversation in Floor Intro
        initDialogue = True
        targetObj = obj
        return True
        
    elif target in [11, 12]: # Potions, needs update
        pickupBoolean = True
        pickupThing = ' HP'
        if target == 11:
            obj.kill()
            player.updatehp(10)
            amountToChange = '+10'
            targetIcon = obj.image
            return True
        elif target == 12:
            obj.kill()
            player.updatehp(20)
            amountToChange = '+20'
            targetIcon = obj.image
            return True

    elif target in [21, 22]: # Gems, needs update
        pickupBoolean = True
        if target == 21:
            pickupThing = ' Damage'
            amountToChange = '+5'
            targetIcon = obj.image
            obj.kill()
            player.updatedmg(5)
            return True
        elif target == 22:
            pickupThing = ' Armor'
            amountToChange = '+5'
            targetIcon = obj.image
            obj.kill()
            player.updatedef(5)
            return True

        
    elif target in list(range(201, 211)): # Keys
        pickupBoolean = True
        targetIcon = obj.image
        amountToChange = '+1'
        if target == 201:
            pickupThing = ' Yellow Key'
            obj.kill()
            player.updateykey(1)
            return True
        elif target == 202:
            pickupThing = ' Blue Key'
            obj.kill()
            player.updatebkey(1)
            return True
        elif target == 203:
            pickupThing = ' Red Key'
            obj.kill()
            player.updaterkey(1)
            return True

    
    elif target in list(range(221, 231)): # Doors
        if target == 221:
            if player.getykey() > 0:
                obj.kill()
                player.updateykey(-1)
                return True
            else: return False
        elif target == 222:
            if player.getbkey() > 0:
                obj.kill()
                player.updatebkey(-1)
                return True
            else: return False
        elif target == 223:
            if player.getrkey() > 0:
                obj.kill()
                player.updaterkey(-1)
                return True
            else: return False
        elif target == 229:
            obj.kill()
            return True
        return False

    elif target in [91, 92, 91.5]: # Stairs, need updates
        if target == 91 and current_floor == 1:
            player.setname(inputVal(screen, "Enter your name (8 char max):"))
            princessName = inputVal(screen, "Enter her name (8 char max):")                 
        return False

    elif target in list(range(501, 601)): # Monsters, need updates
        monsterobject = obj
        monsterBoolean = True
        if fightable(player, obj):
            rounds = int(obj.gethp() / (player.getdmg() - obj.getdef()))
            if obj.getdmg() - player.getdef() > 0:
            	losthp = (obj.getdmg() - player.getdef()) * rounds
            else: losthp = 0
            player.updatehp(-losthp)
            player.updategold(obj.getgold())
            if player.gethp() > 0:
                obj.kill()
                return True
        return False
	    
    elif target in list(range(100, 151)): # Princess
        initDialogue = True
        targetObj = obj
        return False
    
    elif target in list(range(51, 71)):
        obj.kill()
        player.updatedmg(SwordList[target])
        player.setsword(obj.image)
        pickup = True
        pickupObj = obj
        return True
	    
    elif target in list(range(801, 851)): # Mr. Agnew
        initDialogue = True
        targetObj = obj
        return False
    
    else:
        return True


def change_floor(player, map_object, FloorMap, current_floor, currentx, currenty, x, y):
    # [y, x]
    down = [[-1,-1],[-1,-1],[2,3],[12,3],[1,2],[2,13],[1,12],[-1,-1],[1,2],[2,13]]
    up = [[-1,-1],[13,7],[12,7],[2,3],[3,7],[2,13],[1,12],[-1,-1],[1,2],[2,13]]
    playerx = currentx
    playery = currenty
   
    if x > 14 or y > 14:
        return [current_floor, FloorMap, map_object]
    if FloorMap[current_floor][y][x] in [91, 91.5, 92]:
        for b in range(15):
            for c in range(15): 
                if map_object[current_floor][b][c] != None:
                #try:
                    map_object[current_floor][b][c].setX(-999)
                    map_object[current_floor][b][c].setY(-999)
                #except: pass
                
        if FloorMap[current_floor][y][x] in [91, 91.5]:
            current_floor += 1
            FloorMap[current_floor][up[current_floor][0]][up[current_floor][1]]= 99
            FloorMap[current_floor-1][playery][playerx] = 0
            map_object[current_floor][up[current_floor][0]][up[current_floor][1]]= player
            map_object[current_floor-1][playery][playerx] = None
           

        elif FloorMap[current_floor][y][x] == 92:
            current_floor -= 1 
            FloorMap[current_floor][down[current_floor][0]][down[current_floor][1]]= 99
            FloorMap[current_floor+1][playery][playerx] = 0
            map_object[current_floor][down[current_floor][0]][down[current_floor][1]]= player
            map_object[current_floor+1][playery][playerx] = None
            
    
    return [current_floor, FloorMap, map_object]


def fightable(player, monster):
    return player.getdmg() > monster.getdef()

main()

























