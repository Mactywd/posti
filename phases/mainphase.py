import pygame
from config import screen, w, h, ppl, rows, cols
import random
import config

off = 25
font1 = pygame.font.Font(config.resource_path('dependencies/GreenHostel.ttf'), 30)
font1.bold = True

stop = False
selected = [None, None]
ticks = 0 # Ticks from the last swap
delay_switch = False
randomize_sound = pygame.mixer.Sound(config.resource_path('dependencies/sound/randomize.wav'))
randomize_sound.set_volume(0.5)
swap_sound = pygame.mixer.Sound(config.resource_path('dependencies/sound/swap.wav'))
click = pygame.mixer.Sound(config.resource_path('dependencies/sound/click.wav'))
desk = pygame.image.load(config.resource_path('dependencies/desk.png'))
desk = pygame.transform.scale(desk, (125, 125))

group = [[pygame.Rect(w/cols*i+off/4, h/rows*j+off/4, (w-off*2)/cols, (h-off*2)/rows)
        for i in range(cols)]
        for j in range(rows)]

# Randomize function

def randomize():
    randomized = []

    pos_left = [i for i in range(0, 30)]
    ppl_left = [i for i in range(0, len(ppl))]
    for i in range(len(ppl)):
        person = random.choice(ppl_left)
        ppl_left.remove(person)
        
        table = random.choice(pos_left)
        pos_left.remove(table)

        randomized.append([table, person])
    
    return randomized

def main_handling(event):
    global selected, seat_id, swap_id, frames_passed, delay_switch, stop

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        config.phase = 'main_menu'
        if config.sound:
            click.play()
        return

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mp = pygame.mouse.get_pos()
        if mp[0] > w:
            return
        row = mp[1] // (h/rows)
        col = mp[0] // (w/cols)
        seat = col+row*cols
        
        if selected[0] is None:
            found = False
            lpd = 0
            for tb, pr in randomized:
                if found:
                    break
                elif tb == seat:
                    seat_id = lpd
                    found = True
                lpd += 1
            selected[0] = pygame.Rect(w/cols*col, h/rows*row, w/cols, h/rows)

        elif selected[1] is None:
            found = False
            lpd = 0
            for tb, pr in randomized:
                if found:
                    break
                elif tb == seat:
                    swap_id = lpd
                    found = True
                lpd += 1
            selected[1] = pygame.Rect(w/cols*col, h/rows*row, w/cols, h/rows)
            frames_passed = 0
            delay_switch = True
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        stop = not stop

def main_draw():
    global delay_switch, selected, ticks, randomized, frames_passed

    screen.fill(pygame.Color('#19D3CD'))

    if delay_switch:
        if frames_passed < 10:
            frames_passed += 1
        else:
            selected = [None, None]
            randomized[swap_id][1], randomized[seat_id][1] = randomized[seat_id][1], randomized[swap_id][1]
            delay_switch = False
            if config.sound:
                swap_sound.play()

    # Randomize intervall
    if stop == False:
        if ticks % 2 == 0:
            randomized = randomize()
            if config.sound:
                randomize_sound.play()
    
    # Drawing

    if selected[0] is not None:
        pygame.draw.rect(screen, pygame.Color('#00FF00'), selected[0])
    if selected[1] is not None:
        pygame.draw.rect(screen, pygame.Color('#FF0000'), selected[1])

    for row in group:
        for table in row:
            #pygame.draw.rect(screen, (0, 0, 0), table, 10, 15)
            screen.blit(desk, table.topleft)

    for tb, person in randomized:
        table = group[tb//cols]
        table = table[tb%cols]
        prsn = ppl[person].split(' ')
        person = font1.render(prsn[0], True, (255, 255, 0))
        screen.blit(person, (table.centerx-person.get_width()/2, table.centery-person.get_height()/2))
    
    ticks += 1