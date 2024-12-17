import pygame

from pygame.locals import *

while True:
    pygame.event.pump()
    # pygame.event.get()
    # pygame.event.wait()
    # pygame.event.poll()
    # pygame.event.clear()

    '''
        handle mouse input
    '''

    buttons = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    # do something

    '''handle keyboard input'''
    keys = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    # do something

    '''handle keyboard input'''
    keys = pygame.key.get_pressed()
    if keys[K_q]:
        # do something
        pass
    elif keys[K_a]:
        # do something
        pass
    elif keys[K_b] and keys[K_c]:
        # do something
        pass