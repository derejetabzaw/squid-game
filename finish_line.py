import pygame


class FinishLine(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.surf = pygame.Surface((width,height))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (x,y))
    def display(self,display):
        display.blit(self.surf, self.rect)

    def check_game_won(self,player_pos):
        if player_pos < self.rect.top:
            return True



