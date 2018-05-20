## NPC Base Classes

import pygame

class Basic(pygame.sprite.Sprite):
    """
    The root class
    self.x and self.y are pixels, not coordinates
    """    
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 32 * x + 160
        self.y = 32 * y
    def getY(self): return self.y
    def getX(self): return self.x
    def setX(self, x): self.x = 32 * x + 160
    def setY(self, y): self.y = 32 * y
    def update(self): self.rect.topleft = (self.x, self.y)


class NPC(Basic):
    """
    The NPC base class
    Initialize the type for all NPCs
    Sets self.type = "NPC"
    """
    def __init__(self, screen, x, y):
        Basic.__init__(self, screen, x, y)
        self.group = "NPC"

class MrAgnew(NPC):
    """
    The MrAgnew base class
    Key point: self.image, self.rect, self.name, self.role
    """
    def __init__(self, screen, x, y, img):
        NPC.__init__(self, screen, x, y)
        self.image = pygame.image.load('./imgSource/All/{}.png'.format(img))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.name = 'Mr. Agnew'
        self.type = "Ally"


class Princess(Basic):
    def __init__(self, screen, x, y):
        Basic.__init__(self, screen, x, y)
        
        self.imageList = []
        for i in range(1, 14, 4):
            image = pygame.image.load(('./imgSource/Princess/images/Princess_'+\
                                       str(i).rjust(2, '0')+'.png')).convert()
            image.set_colorkey((0, 0, 0))
            self.imageList.append(image)
        self.image = self.imageList[0]
        self.image.set_colorkey((0, 0, 0))
        ## Here, self.imageList is useless because it will
        ## always be overriden

        self.screen = screen
        self.rect = self.image.get_rect()
        self.type = 'Ally'


class Merchant(NPC):
    """
    The Merchant base class
    Key point: self.image, self.rect, self.name, self.role
    """
    def __init__(self, screen, x, y, img):
        NPC.__init__(self, screen, x, y)
        self.image = pygame.image.load('./imgSource/All/{}.png'.format(img))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.name = 'Merchant'
        self.type = "Ally"
      

class Thief(NPC):
    """
    The Thief base class
    Key point: self.image, self.rect, self.name, self.role
    """
    def __init__(self, screen, x, y, img):
        NPC.__init__(self, screen, x, y)
        self.image = pygame.image.load('./imgSource/All/{}.png'.format(img))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.name = 'Thief'
        self.type = "Ally"


class Nemo(NPC):
    """
    The Nemo base class
    Key point: self.image, self.rect, self.name, self.role
    """
    def __init__(self, screen, x, y, img):
        NPC.__init__(self, screen, x, y)
        self.image = pygame.image.load('./imgSource/All/{}.png'.format(img))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.name = 'Nemo'
        self.type = "Ally"











        
