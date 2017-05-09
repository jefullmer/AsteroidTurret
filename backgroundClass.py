## backgroundClass.py
## James
## Spring 16

import pygame, sys
from pygame.locals import *

class background(object):
    
    def __init__(self, surf, image):
        self.surf = surf
        info = pygame.display.Info()
        dh = info.current_h
        dw = info.current_w
        
        self.image = image
        self.image = pygame.transform.scale(self.image, (dw, dh))
    
    def displayBack(self):
        self.surf.blit(self.image, [0, 0])