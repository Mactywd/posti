import pygame
from config import screen, h, w, ppl
import config
import json

bkg = pygame.image.load(config.resource_path('dependencies/bkg.png'))
options_bkg = pygame.image.load(config.resource_path('dependencies/options_bkg.png'))
title_font = pygame.font.Font(config.resource_path('dependencies/Sandbox.ttf'), 70)
sub_font = pygame.font.Font(config.resource_path('dependencies/Sandbox.ttf'), 40)
norm_font = pygame.font.Font(config.resource_path('dependencies/Sandbox.ttf'), 20)

semi_phase = 'menu'

# Rects 'n stuff

def draw_rect(rect):
    return pygame.Rect(rect.left-5, rect.top-5, rect.w+7, rect.h+3)

start = title_font.render("INIZIA", True, pygame.Color('#D3BA00'))
options = title_font.render('OPZIONI', True, pygame.Color('#D3BA00'))

start_rect = pygame.Rect(w/4-start.get_width()/2, h/3-start.get_height()/2, start.get_width(), start.get_height())
options_rect = pygame.Rect(w/4*3-options.get_width()/2, h/3-options.get_height()/2, options.get_width(), options.get_height())

start_rect_draw = draw_rect(start_rect)
options_rect_draw = draw_rect(options_rect)

sound_txt = title_font.render("SUONI", True, pygame.Color('#545454'))
sound_rect = pygame.Rect(w/2-sound_txt.get_width()/2, h/3*2+40, sound_txt.get_width(), sound_txt.get_height())
sound_rect_draw = pygame.Rect(sound_rect.left-60, sound_rect.top-10, sound_rect.w+120, sound_rect.h+10)


click = pygame.mixer.Sound(config.resource_path('dependencies/sound/click.wav'))

instructions = json.loads(open(config.resource_path('dependencies/instructions.json')).read())

# Event handling 
def menu_handling(event):
    global semi_phase
    if semi_phase == 'menu':
        if event.type == pygame.MOUSEBUTTONDOWN:
            mp = pygame.mouse.get_pos()
            if start_rect_draw.collidepoint(mp):
                config.phase = 'main'
                if config.sound:
                    click.play()
            elif options_rect_draw.collidepoint(mp):
                semi_phase = 'options'
                if config.sound:
                    click.play()
        
    elif semi_phase == 'options':
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                semi_phase = 'menu'
                if config.sound:
                    click.play()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mp = pygame.mouse.get_pos()
            if sound_rect_draw.collidepoint(mp):
                config.sound = not config.sound

            

# Draw handling
def menu_drawing():
    if semi_phase == 'menu':
        screen.blit(bkg, (0, 0))

        screen.blit(start, start_rect)
        screen.blit(options, options_rect)

        pygame.draw.rect(screen, pygame.Color('#D3BA00'), start_rect_draw, 3, 5)
        pygame.draw.rect(screen, pygame.Color('#D3BA00'), options_rect_draw, 3, 5)
    
    if semi_phase == 'options':
        screen.blit(options_bkg, (0, 0))
        
        title = title_font.render("COME USARE", True, (0, 0, 0))
        subt_1 = sub_font.render("INZIARE", True, (0, 0, 0))
        subt_1_txt_1 = norm_font.render(instructions["ISTRUZIONI"]["COME INIZIARE"][0], True, (0, 0, 0))
        subt_1_txt_2 = norm_font.render(instructions["ISTRUZIONI"]["COME INIZIARE"][1], True, (0, 0, 0))

        screen.blit(title, (w/2-title.get_width()/2, 120))
        screen.blit(subt_1, (120, 200))
        screen.blit(subt_1_txt_1, (110, 250))
        screen.blit(subt_1_txt_2, (110, 250 + 25))

        subt_2 = sub_font.render("COMANDI", True, (0, 0, 0))
        subt_2_txt_1 = norm_font.render(instructions["ISTRUZIONI"]["COMANDI"][0], True, (0, 0, 0))
        subt_2_txt_2 = norm_font.render(instructions["ISTRUZIONI"]["COMANDI"][1], True, (0, 0, 0))
        subt_2_txt_3 = norm_font.render(instructions["ISTRUZIONI"]["COMANDI"][2], True, (0, 0, 0))

        screen.blit(subt_2, (120, 320))
        screen.blit(subt_2_txt_1, (110, 370))
        screen.blit(subt_2_txt_2, (110, 400))
        screen.blit(subt_2_txt_3, (110, 430))
        
        if config.sound:
            rect_color = (0, 255, 0)
        else:
            rect_color = (255, 0 , 0)
        
        pygame.draw.rect(screen, rect_color, sound_rect_draw, 0, 30)
        pygame.draw.rect(screen, pygame.Color('#545454'), sound_rect_draw, 5, 30)
        screen.blit(sound_txt, sound_rect)