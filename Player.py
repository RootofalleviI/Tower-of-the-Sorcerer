## Player

import pygame

class Basic(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 32 * x + 160
        self.y = 32 * y
    def getY(self): return self.y
    def getX(self): return self.x
    def setX(self, x): self.x = 32 * x + 160
    def setY(self, y): self.y = 32 * y
    def update(self): self.rect.topleft = (self.x, self.y)


class Player(Basic):
    def __init__(self, screen, x, y):
        Basic.__init__(self, screen, x, y)
        
        self.imageList = []
        for i in range(1, 14, 4):
            image = pygame.image.load(('./imgSource/Player/Player01_'+\
                                       str(i).rjust(2, '0')+'.png')).convert()
            self.imageList.append(image)
        self.image = self.imageList[0]
        '''
        self.image = pygame.image.load('./imgSource/All/99.png').convert()
        self.imageList = []
        while len(self.imageList) < 4:
        	self.imageList.append(self.image)
        '''
        self.icon = self.imageList[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.__name = 'Player'
        self.__hp = 100
        self.__dmg = 30
        self.__def = 20
        self.ykey = 0
        self.bkey = 0
        self.rkey = 1
        self.__gold = 0
        self.__level = 1
        self.swordIcon = pygame.image.load('./imgSource/All/empty.png').convert()
        self.swordIcon.set_colorkey((0, 0, 0))
        self.shieldIcon = pygame.image.load('./imgSource/All/empty.png').convert()
        self.shieldIcon.set_colorkey((0, 0, 0))

    def getname(self): return self.__name
    def setname(self, name): self.__name = name
    
    def getsword(self): return self.swordIcon
    def setsword(self, img): self.swordIcon = img

    def getshield(self): return self.shieldIcon
    def setshield(self, img): self.shieldIcon = img

    def getimage(self): return self.image
    def changeimage(self, index): self.image = self.imageList[index]
    def geticon(self): return self.imageList[0]
    
    def setykey(self, num): self.ykey = num
    def updateykey(self, num): self.ykey += num
    def getykey(self): return self.ykey

    def setbkey(self, num): self.bkey = num
    def updatebkey(self, num): self.bkey += num
    def getbkey(self): return self.bkey

    def setrkey(self, num): self.rkey = num
    def updaterkey(self, num): self.rkey += num
    def getrkey(self): return self.rkey

    def setlevel(self, num): self.__level = num
    def updatelevel(self, num): self.__level += num
    def getlevel(self): return self.__level

    def setdmg(self, num): self.__dmg = num
    def updatedmg(self, num): self.__dmg += num
    def getdmg(self): return self.__dmg

    def setdef(self, num): self.__def = num
    def updatedef(self, num): self.__def += num
    def getdef(self): return self.__def

    def sethp(self, num): self.__hp = num
    def updatehp(self, num): self.__hp += num
    def gethp(self): return self.__hp
    
    
    def setgold(self, num): self.__gold = num
    def updategold(self, num): self.__gold += num
    def getgold(self): return self.__gold
