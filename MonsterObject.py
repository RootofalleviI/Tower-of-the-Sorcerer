## Monster Objects

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


class Monster(Basic):
    def __init__(self, screen, x, y):
        Basic.__init__(self, screen, x, y)
        self.type = "Monster"

class NormalMonster(Monster):
    def __init__(self, screen, x, y, img, hp, dmg, def_, gold):
        Monster.__init__(self, screen, x, y)

        self.image = pygame.image.load('./imgSource/All/{}.png'.format(img))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.__hp = hp
        self.__dmg = dmg
        self.__def = def_
        self.__gold = gold

    def getimage(self): return self.image
    def getdmg(self): return self.__dmg
    def getdef(self): return self.__def
    def gethp(self): return self.__hp
    def getgold(self): return self.__gold


class SpecialMonster(pygame.sprite.Sprite):
    pass
