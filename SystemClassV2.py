## SystemClass V2.0

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

    def update(self):
        data = self.__name__ + '()'
        exec("self.data = player." + data)
        try:
            if twoParts: self.image = self.__font.render(twoParts + str(self.data), True, color)
            else: self.image = self.__font.render(str(self.data), True, color)
        except: pass
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)


        

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

'''
class Conversation():
    def __init__(self, character, text, category, returnVal = ''):
        if category == 0:
            print("<{}>: {}".format(character, text))
        elif category == 1:
            exec(returnVal +'= input("<{}>: {}".format(character, text))')
'''
        
class SubtitleText(pygame.sprite.Sprite):
    def __init__(self, screen, character, text, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.font = pygame.font.Font('./Font/PAPYRUS.TTF', 30)
        self.image = self.font.render(character.name + text, True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)









        
