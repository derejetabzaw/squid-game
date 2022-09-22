import sys
from tkinter import CENTER
import pygame 
from pygame.locals import *

vec = pygame.math.Vector2
ACC = 0.2
FRIC = -0.5


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.surf = pygame.Surface((width,height))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (x,y))

        self.pos = vec((x,y))
        self.rect.midbottom = self.pos 
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.acc.y = ACC
        
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos -= self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos




 

    def display(self,displaye_surface):
        displaye_surface.blit(self.surf , self.rect)
        
        
