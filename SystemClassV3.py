## SystemClass V3

import pygame

WHITE = 255, 255, 255
BLACK = 0, 0, 0

class TextButton(pygame.sprite.Sprite):
    def __init__(self, screen, text, font, size, colorOff, colorOn, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        self.textNormal = self.font.render(text, True, colorOff)
        self.textHighlighted = self.font.render(text, True, colorOn)
        self.screen = screen

        self.pos = x, y
        self.selected = False

    def display(self):
        if self.selected:
            self.screen.blit(self.textHighlighted, self.pos)
        else:
            self.screen.blit(self.textNormal, self.pos)



class Icon(pygame.sprite.Sprite):
    def __init__(self, screen, player, image_path, colorKey, \
                 centerx, centery, transformScale = None):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        try:
            self.image = pygame.image.load(image_path).convert()
        except:
            exec('self.image = ' + image_path)
        if transformScale:
            self.image = pygame.transform.scale(self.image, transformScale)
        self.image.set_colorkey(colorKey)
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)

class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.image = pygame.image.load("./imgSource/System/inGame.png").convert()
        self.rect = self.image.get_rect()

class SubtitleText(pygame.sprite.Sprite):
    def __init__(self, screen, character, text, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.font = pygame.font.Font('./Font/PAPYRUS.TTF', 30)
        self.image = self.font.render(character.name + text, True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)

class YKeyNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.ykey = player.getykey()
    def setykey(self, player):
        self.ykey = player.getykey()
    def update(self):
        self.image = self.font.render(str(self.ykey), True, (255, 128, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (120, 360)
        self.rect.left = 90
        
    
class BKeyNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.bkey = player.getbkey()
    def setbkey(self, player):
        self.bkey = player.getbkey()
    def update(self):
        self.image = self.font.render(str(self.bkey), True, (0, 104, 204))
        self.rect = self.image.get_rect()
        self.rect.center = (120, 400)
        self.rect.left = 90

class RKeyNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.rkey = player.getrkey()
    def setrkey(self, player):
        self.rkey = player.getrkey()
    def update(self):
        self.image = self.font.render(str(self.rkey), True, (255, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (120, 440)
        self.rect.left = 90

class GoldNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.gold = player.getgold()
    def setgold(self, player):
        self.gold = player.getgold()
    def update(self):
        self.image = self.font.render(str(self.gold), True, (204, 104, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (120, 480)
        self.rect.left = 90

class StatusLevel(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/FestivalBudayaXXXI.otf", 28)
        self.level = player.getlevel()
    def setlevel(self, player):
        self.level = player.getlevel()
    def update(self):
        self.image = self.font.render('lvl: ' + str(self.level), True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 60)

class DmgNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.dmg = player.getdmg()
    def setdmg(self, player):
        self.dmg = player.getdmg()
    def update(self):
        self.image = self.font.render(str(self.dmg), True, (128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.left = 100
        self.rect.top = 82

class DefNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self._def = player.getdef()
    def setdef(self, player):
        self._def = player.getdef()
    def update(self):
        self.image = self.font.render(str(self._def), True, (128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.left = 100
        self.rect.top = 123

class HpNumber(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.hp = player.gethp()
    def sethp(self, player):
        self.hp = player.gethp()
    def update(self):
        self.image = self.font.render(str(self.hp), True, (128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.left = 100
        self.rect.top = 163

class PlayerName(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/FestivalBudayaXXXI.otf", 20)
        self.name = player.getname()
    def setname(self, player):
        self.name = player.getname()
    def update(self):
        self.image = self.font.render(self.name.center(8), True, (128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.left = 35
        self.rect.top = 8

class SwordIcon(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = player.getsword()
    def setimg(self, player):
        self.image = player.getsword()
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (700, 30)

class ShieldIcon(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = player.getshield()
    def setimg(self, player):
        self.image = player.getshield()
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.left = 800
        self.rect.top = 83

class ChangeStats(pygame.sprite.Sprite):
    def __init__(self, screen, sign, number, stat):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/PAPYRUS.ttf", 20)
        self.font.set_bold(True)
        self.image = self.font.render(sign + str(number) + stat,
                                      True, WHITE)
        
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.left = 700
        self.rect.top = 395

class PickupIcon(pygame.sprite.Sprite):
    def __init__(self, screen, icon):
        pygame.sprite.Sprite.__init__(self)
        self.image = icon
        
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.left = 650
        self.rect.top = 395

class FloorTracker(pygame.sprite.Sprite):
    def __init__(self, screen, number):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/FestivalBudayaXXXI.otf", 15)
        self.floor = number-1
    def setfloor(self, number):
        self.floor = number-1
    def update(self):
        if self.floor >= 0:
            self.image = self.font.render("Current floor: " + str(self.floor), True, BLACK)
            self.rect = self.image.get_rect()
            self.rect.left = 5
            self.rect.top = 525
        else:
            self.image = self.font.render("Current floor: $", True, BLACK)
            self.rect = self.image.get_rect()
            self.rect.left = 5
            self.rect.top = 525

class MonsterIcon(pygame.sprite.Sprite):
    def __init__(self, screen, monster):
        pygame.sprite.Sprite.__init__(self)
        self.image = monster.image
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.top = 218
        self.rect.left = 380

class MonsterDmg(pygame.sprite.Sprite):
    def __init__(self, screen, monster):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = monster.getdmg()
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
    def update(self):
        self.image = self.font.render(str(self.dmg), True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.top = 257
        self.rect.left = 410
        
class MonsterDef(pygame.sprite.Sprite):
    def __init__(self, screen, monster):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.def_ = monster.getdef()
    def update(self):
        self.image = self.font.render(str(self.def_), True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.top = 297
        self.rect.left = 410

class MonsterHP(pygame.sprite.Sprite):
    def __init__(self, screen, monster):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.hp = monster.gethp()
    def update(self):
        self.image = self.font.render(str(self.hp), True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.top = 337
        self.rect.left = 410


'''
class PlayerDmg(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.dmg = player.getdmg()
    def setdmg(self, player):
        self.dmg = player.getdmg()
    def update(self):
        self.image = self.font.render(str(self.dmg), True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = 310
        self.rect.top = 190

class PlayerDef(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self._def = player.getdef()
    def setdef(self, player):
        self._def = player.getdef()
    def update(self):
        self.image = self.font.render(str(self._def), True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = 310
        self.rect.top = 230

class PlayerHP(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./Font/EnglishTowne.TTF", 35)
        self.hp = player.gethp()
    def sethp(self, player):
        self.hp = player.gethp()
    def update(self):
        self.image = self.font.render(str(self.hp), True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = 310
        self.rect.top = 270

class String(pygame.sprite.Sprite):
    def __init__(self, screen, player, font, size, data, color,\
                 centerx, centery, twoParts = ''):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.__font = pygame.font.Font(font, size)
        exec("self.data = player." + data)

        if twoParts: self.image = self.__font.render(twoParts + str(self.data), True, color)
        else: self.image = self.__font.render(str(self.data), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)
'''
