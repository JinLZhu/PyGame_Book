import pygame.event

MY_EVENT = pygame.USEREVENT + 1
event = pygame.event.Event(MY_EVENT,
                           attri1="attribute1",
                           attri2="attribute2")
pygame.event.post(event)