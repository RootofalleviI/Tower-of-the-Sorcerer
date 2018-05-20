## Princess

import pygame
from NPC_Base import Princess  
        
class PrincessF0Far(Princess):
    """
    Intro floor
    I'm having self.image and self.icon as two separate
    attributes in case I need them in the future.
    """
    def __init__(self, screen, x, y):
        Princess.__init__(self, screen, x, y)
        self.image = pygame.image.load('./imgSource/All/black.png').convert()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.icon = self.image
        self.name = "Far far away..."
        self.dialogueList = ["--- Help! Help! Help!",
                             "!What was that???"]
       

class PrincessF0(Princess):
    def __init__(self, screen, x, y):
        Princess.__init__(self, screen, x, y)
        self.icon = pygame.image.load('./imgSource/All/100.png').convert()
        self.icon.set_colorkey((0, 0, 0))
        self.image = self.icon
	
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.dialogueList = ["@Thank you!",
                                 "@I was on my way to the Tower of the Sorcerer...",
                                 "@I would've died if you didn't save me!",
                                 "!Why are you going there?",
                                 "@*sob* My father... the king... was held capture...",
                                 "@I'm trying to save him... all by myself...",
                                 "!Let me help you!",
                                 "@Really!?",
                                 "@O good Lord, I don't know how to thank you!",
                                 "@You see that path behind me?",
                                 "@That is the way to the Tower.",
                                 "!Meet you there!"
                                 ]

        self.dialogueList2 = ["@Good luck!"]
    
        

class PrincessF1(Princess):
    def __init__(self, screen, x, y):
        Princess.__init__(self, screen, x, y)
        self.icon = pygame.image.load('./imgSource/All/103.png').convert()
        self.icon.set_colorkey((0, 0, 0))
        self.image = self.icon
	
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.dialogueList = ["@Nice sword!",
                                 "@I'll meet you upstairs.",
                                 "@Be safe!",
                                 ]

        self.dialogueList2 = ["@Be safe!"]
   
    
