## Mr. Agnew File

import pygame
from NPC_Base import MrAgnew

class MrAgnewF1(MrAgnew):
    def __init__(self, screen, x, y, img):
        MrAgnew.__init__(self, screen, x, y, img)
        self.dialogueList = ["Hello!",
                             "Welcome to the Tower of the Sorcerer.",
                             "You may call me Mr. Agnew.",
                             "!What are those!?",
                             "Those bones?",
                             "...",
                             "People who have failed in the past.",
                             "I hope you won't become one of them...",
                             "!Anything I need to know before starting my adventure?",
                             "You see that yellow door? You need a yellow key to open it.",
                             "Each type of door has a corresponding type of key...",
                             "Don't worry if you feel there's too much to learn.",
                             "I will guide you throughout your adventure.",
                             "!Thank you!",
                             "Best of luck!"]
        self.dialogueList2 = ["Best of luck!"]
        self.icon = self.image













                                     
