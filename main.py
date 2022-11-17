import pygame
pygame.init()
import random
import sys
from config import screen, w, h
import config
from phases.mainphase import main_handling, main_draw
from phases.mainmenu import menu_handling, menu_drawing


def gameloop():
    while True:
        # Event handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if config.phase == 'main':
                main_handling(event)
            elif config.phase == 'main_menu':
                menu_handling(event)
    
        # Drawing
        screen.fill((255, 255, 255))

        if config.phase == 'main':
            main_draw()
        if config.phase == 'main_menu':
            menu_drawing()
        
        # Saving
        pygame.display.flip()

        pygame.time.Clock().tick(60)


if gameloop():
    pygame.quit()
