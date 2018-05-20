## Conversation Interface
import pygame

class ConvIcon(pygame.sprite.Sprite):
    def __init__(self, screen, obj_img):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = obj_img
        self.rect = self.image.get_rect()
        self.rect.left = 160
        self.rect.top = 480
    
class ConvName(pygame.sprite.Sprite):
    def __init__(self, screen, obj_name,obj_type):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font = pygame.font.Font('./Font/PAPYRUS.TTF', 20)
        self.font.set_bold(True)
        if obj_type == "Ally":
            color = (110, 235, 120) # Green
        elif obj_type == "Player":
            color = 230, 230, 35 # Yellow
        else:
            color = (255, 255, 255)
        self.image = self.font.render(obj_name, True, color)
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 480
    
class ConvConv(pygame.sprite.Sprite):
    def __init__(self, screen, obj_conv):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font = pygame.font.Font('./Font/GamestationStorm.otf', 20)
        self.font.set_bold(True)
        self.obj_conv = obj_conv
        self.image = self.font.render(obj_conv, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 515
        self.good = False


class PressEnter(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font = pygame.font.Font('./Font/PAPYRUS.TTF', 18)
        self.font.set_bold(True)
        self.image = self.font.render("Press Enter...", True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left = 760
        self.rect.top = 500

class PickUp(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font = pygame.font.Font('./Font/PAPYRUS.TTF', 20)
        self.font.set_bold(True)
        self.image = self.font.render("You acquired", True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left = 650
        self.rect.top = 390
        self.display = False

class PickUpIcon(pygame.sprite.Sprite):
    def __init__(self, screen, obj):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = obj.image
        self.rect = self.image.get_rect()
        self.rect.left = 830
        self.rect.top = 390
        self.display = False


    
