## textClass.py
## James
## Spring 16

import pygame, sys
from pygame.locals import *

class textGraphic(object):

    def __init__(self, surf, text, color, pos, size):
        self.Surf = surf
        info = pygame.display.Info()
        dh = info.current_h
        dw = info.current_w
        self.active = True
        self.titleFont = pygame.font.SysFont("Sylfaen", 120)
        self.Text = text
        self.color = color
        self.size = size
        self.TextSurf = self.titleFont.render(self.Text, True, self.color, None)
        self.TextSurf = pygame.transform.scale(self.TextSurf, (self.size[0], self.size[1]))
        self.Pos = pos

    def display(self):
        if self.active:
            self.Surf.blit(self.TextSurf, self.Pos)

    def changeText(self, newText):
        self.Text = newText
        self.TextSurf = self.titleFont.render(self.Text, True, self.color, None)
        self.TextSurf = pygame.transform.scale(self.TextSurf, (self.size[0], self.size[1]))