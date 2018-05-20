import pygame
from pygame import *

pygame.init()

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else: pass

def display_box(screen, message):
    font = pygame.font.Font('./Font/printer.ttf', 40)
    pygame.draw.rect(screen, (255, 255, 255), \
                     (700, 400, 135, 22), 1)
    if len(message) != 0:
        image = font.render(message, True, (255, 255, 255))
        screen.blit(image,(705, 400))
    pygame.display.flip()


def ask(screen):
    current_string = []
    display_box(screen, ''.join(current_string))
    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0: -1]
            if current_string and current_string[-1] == 'w':
                increment = 17.3 - (len(current_string) * 0.4)
            else:
                increment = 14
            pygame.draw.rect(screen, (0, 0, 0),
                             (700 + (increment*len(current_string)),
                             400,(9 - len(current_string)) * 17, 22))
            pygame.display.flip()
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS and len(current_string) <= 8:
            current_string.append("_")
        elif inkey <= 127 and len(current_string) <= 8:
            current_string.append(chr(inkey))
        display_box(screen, ''.join(current_string))
        pygame.display.update()
    return ''.join(current_string)

