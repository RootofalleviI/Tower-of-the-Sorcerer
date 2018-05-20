## System Object
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


## Walls
class Wall(Basic):
    def __init__(self, screen, x, y, type_of_wall):
        Basic.__init__(self, screen, x, y)
        self.type = 'Wall'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_wall)).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        
class Grass(Basic):
    def __init__(self, screen, x, y, type_of_grass):
        Basic.__init__(self, screen, x, y)
        self.type = 'Grass'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_grass)).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y


class Door(Basic):
    def __init__(self, screen, x, y, type_of_door):
        Basic.__init__(self, screen, x, y)
        self.type = 'Door'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_door)).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
'''     
class SpecialDoor(Door):
    def __init__(self, screen, x, y, type_of_door, trigger, FloorMap,
                 current_floor, *targets):
        Door.__init__(self, screen, x, y)
        self.targets = []
        for target in targets:
                self.targets.append(target)
        self.trigger = False
        self.FloorMap = FloorMap
        self.current_floor = current_floor

    def check(self):
        for x, y in self.targets:
            if self.FloorMap[self.current_floor][y][x] != 0:
                break
            else:
                self.trigger = True
        return
'''        
class Key(Basic):
    def __init__(self, screen, x, y, type_of_key):
        Basic.__init__(self, screen, x, y)
        self.type = 'Key'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_key)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y


class Stair(Basic):
    def __init__(self, screen, x, y, type_of_stair):
        Basic.__init__(self, screen, x, y)
        self.type = 'Stair'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_stair)).convert()
        self.image.set_colorkey((255, 255, 255))
        if type_of_stair == 91.5: self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y


class Potion(Basic):
    def __init__(self, screen, x, y, type_of_potion):
        Basic.__init__(self, screen, x, y)
        self.type = 'Potion'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_potion)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y


class Gem(Basic):
    def __init__(self, screen, x, y, type_of_gem):
        Basic.__init__(self, screen, x, y)
        self.type = 'Gem'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(type_of_gem)).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

class Bones(Basic):
    def __init__(self, screen, x, y):
        Basic.__init__(self, screen, x, y)
        self.type = 'Wall'
        self.image = pygame.image.load(
            "./imgSource/All/-99.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

class Sword(Basic):
    def __init__(self, screen, x, y, code_of_sword):
        Basic.__init__(self, screen, x, y)
        self.type = 'Weapon'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(str(code_of_sword))).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

class Shield(Basic):
    def __init__(self, screen, x, y, code_of_shield):
        Basic.__init__(self, screen, x, y)
        self.type = 'Shield'
        self.image = pygame.image.load(
            "./imgSource/All/{}.png".format(str(code_of_shield))).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y






    

        
