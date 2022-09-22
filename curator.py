import random
import pygame 
import enum 

from player import Player 

curator_red = pygame.image.load("resources/curater/redlight.png")
curator_green = pygame.image.load("resources/curater/greenlight.jpg")
curator_turning = pygame.image.load("resources/curater/turning.jpg")

RED_STATE_TIME_RANGE = (1000,6000)
GREEN_STATE_TIME_RANGE = (400,3000)
TURNING_STATE_TIME_RANGE = (150,400)

class CuratorState(enum.Enum):
    RED = 1 
    GREEN = 2
    TURNING = 3

class Curator(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,player:Player):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.surf = pygame.Surface((width,height))
        self.rect = self.surf.get_rect(center = (x,y))
        self.state = CuratorState.GREEN
        self.last_state = CuratorState.TURNING 
        self.state_time_start = pygame.time.get_ticks()
        self.state_wait_time = random.uniform(GREEN_STATE_TIME_RANGE[0],GREEN_STATE_TIME_RANGE[1])
        self.player = player
        self.last_player_pos_y = player.rect.bottom
    def update(self):
        time_elapsed = (pygame.time.get_ticks() - self.state_time_start)
        if time_elapsed > self.state_wait_time:
            if self.state == CuratorState.GREEN:
                self.last_state = CuratorState.GREEN
                self.state = CuratorState.TURNING
                self.state_wait_time = random.uniform(TURNING_STATE_TIME_RANGE[0], TURNING_STATE_TIME_RANGE[1])
            elif self.state == CuratorState.TURNING and self.last_state == CuratorState.GREEN:
                self.last_state = CuratorState.TURNING
                self.state = CuratorState.RED
                self.state_wait_time = random.uniform(RED_STATE_TIME_RANGE[0],RED_STATE_TIME_RANGE[1])
                self.last_player_pos_y = self.player.rect.bottom
            elif self.state == CuratorState.TURNING and self.last_state == CuratorState.RED:
                self.last_state = CuratorState.TURNING
                self.state = CuratorState.GREEN 
                self.state_wait_time = random.uniform(GREEN_STATE_TIME_RANGE[0],GREEN_STATE_TIME_RANGE[1])
            elif self.state == CuratorState.RED:
                self.last_state = CuratorState.RED
                self.state = CuratorState.RED 
                self.state = CuratorState.TURNING
                self.state_wait_time = random.uniform(TURNING_STATE_TIME_RANGE[0],TURNING_STATE_TIME_RANGE[1])
            self.state_time_start = pygame.time.get_ticks()

    def display(self,display):
        if self.state == CuratorState.GREEN:
            display.blit(curator_green,self.rect)
        elif self.state == CuratorState.TURNING:
            display.blit(curator_turning,self.rect)
        elif self.state == CuratorState.RED:
            display.blit(curator_red,self.rect)

    def detect_movement(self):
        if self.state == CuratorState.RED:
            if self.player.rect.bottom < self.last_player_pos_y:
                return True
        False