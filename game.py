import sys
import pygame 
from pygame.locals import *
from player import Player 
from finish_line import FinishLine
from game_state import GameState
from curator import Curator 

global gamestate
gamestate = GameState.ACTIVE


ground_image = pygame.image.load("resources/background.jpg")


pygame.init()

clock = pygame.time.Clock()
FPS = 50

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 400

display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Red Light, Green Light")
player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT - 50) , 64 , 90)
finishline = FinishLine(SCREEN_WIDTH/2 , 200 , SCREEN_WIDTH, 3)
curator = Curator((SCREEN_WIDTH/2) - (50/2) , 50, 50, 100 , player)

all_entities = pygame.sprite.Group()
all_entities.add(player)
all_entities.add(finishline)
all_entities.add(curator)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display_surface.blit(ground_image,(0,0))
    for entity in all_entities:
        entity.display(display_surface)
    if gamestate == GameState.ACTIVE:
        player.move()
        curator.update()

        if curator.detect_movement():
            print ("You LOST!!!")
            game_state = GameState.LOST
                        
            pygame.init()

            clock = pygame.time.Clock()
            FPS = 50

            SCREEN_HEIGHT = 800
            SCREEN_WIDTH = 400

            display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

            pygame.display.set_caption("Red Light, Green Light")
            player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT - 50) , 64 , 90)
            finishline = FinishLine(SCREEN_WIDTH/2 , 200 , SCREEN_WIDTH, 3)
            curator = Curator((SCREEN_WIDTH/2) - (50/2) , 50, 50, 100 , player)

            all_entities = pygame.sprite.Group()
            all_entities.add(player)
            all_entities.add(finishline)
            all_entities.add(curator)
        elif finishline.check_game_won(player.rect.bottom):
            gamestate = GameState.WON
            print ("YOU WON")
    
    player.move()
    pygame.display.update()
    clock.tick(FPS)