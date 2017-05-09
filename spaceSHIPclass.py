## spaceSHIPclass.py
## James
## Fall 15

import pygame, sys
from pygame.locals import *
from vector2class import vector2
from math import *

class spaceSHIP(pygame.sprite.Sprite):

    def __init__(self, pos, size, graphic, surf):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.xPOS = pos.vX
        self.yPOS = pos.vY
        self.POS = pos
        self.staticPos = pos
        self.SURF = surf
        self.GRAPHIC = graphic
        
        self.health = 3
        self.healthColor = (0, 0, 0)
        self.active = True

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        graphic1 = pygame.image.load(self.GRAPHIC).convert_alpha()
        graphic1 = pygame.transform.scale(graphic1, (self.WIDTH, self.HEIGHT))
        self.image.blit(graphic1, (0, 0))
        self.tempIMAGE = self.image
        
        self.rect = self.image.get_rect()
        self.rect.x = self.xPOS
        self.rect.y = self.yPOS
        
        w, h = self.image.get_size()
        self.staticPos = vector2(self.xPOS - w//2, self.yPOS - h//2)        

    def rotateSS(self, theta):

        self.image = pygame.transform.rotate(self.tempIMAGE, theta)
        w, h = self.image.get_size()
        self.POS = vector2(self.xPOS - w//2, self.yPOS - h//2)
        self.rect = self.image.get_rect()
        self.rect.x = self.POS.vX
        self.rect.y = self.POS.vY

        
    def displaySpaceSHIP(self):
        
        if self.active:
            self.SURF.blit(self.image, (self.rect.x, self.rect.y))
            self.__displayHealth()
        #self.SURF.blit(self.image, (self.POS.vX - self.WIDTH//2, self.POS.vY - self.HEIGHT//2))
    
    def __displayHealth(self):
        
        for i in range(self.health):
            pygame.draw.rect(self.SURF, self.healthColor, [self.staticPos.vX + (i * 21), self.staticPos.vY - 20, 20, 20])
        
