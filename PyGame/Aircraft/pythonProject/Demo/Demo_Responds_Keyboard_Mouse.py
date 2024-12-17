import pygame
import sys

from pygame.constants import KEYDOWN, K_QUOTE
from pygame.locals import *

while True:
    for event in pygame.event.get():
        if event.type == QUTI:
            sys.exit()
        elif event.type == KEYDOWN:
            # handle key down
            if event.key == K_q:
                # do something
            elif event.key == K_a:
                # do something
            elif event.key == K_b:
                # do something
            elif event.key == K_c:
                # do something
        elif event.type == KEYUP:
            # handle key up
        elif event.type == MOUSEMOTION:
            # handle mouse motion
        elif event.type == MOUSEBUTTONDOWN:
            # handle mouse button down
        elif event.type == MOUSEBUTTONUP:
            # handle mouse button up