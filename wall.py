import pygame 
import time 
from config import *

class wall: 
    
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
    
        game_over_surface = my_font.render(
        'You lose' , True, RED)
    
        game_over_rect = game_over_surface.get_rect()
    
        game_over_rect.midtop = (SCREEN_HEIGHT/2, SCREEN_WIDTH/4)
    
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
    
        time.sleep(2)
    
        pygame.quit()
    
        quit()
       