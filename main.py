import pygame
from objects import *
from map_editor import *
from interface import *
from physics import *
from vis import *

paused, playing = False, False
begging_flag = False
menu = MainMenu(sc)
settings = SettingsMenu(sc)
cat = Player()
inv = Inventory(sc, [cat.weapon])
cat.x=450
cat.y = 50
objects=[cat]
image_mass = image_to_mass('maps/map1.jpg')
borders=detect_void(image_mass)
map_image = pilImageToSurface(image_mass)
dt = 0.5
remove_part_of_map(450, 200, 300, borders, image_mass)
pause = Button(sc, W*5/6, H/6, pygame.image.load('models/pause_btn.png').convert_alpha(), 0.15)

start = pygame.mixer.Sound('music/while_playing.mp3')
start.play(-1)

fighting = pygame.mixer.Sound("music/fighting.mp3")
fighting.set_volume(0.2)

walk = pygame.mixer.Sound("music/walk-compress.mp3")

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    
    events = pygame.event.get()
    if menu.on:
        menu.draw()
        menu.check_events()
    
    if menu.quit:
        finished = True
    
    if menu.settings:
        menu.settings = False
        settings.on = True
        
    if settings.on:
        menu.settings = False
        settings.draw()
        for event in events:
            
            if event == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if settings.volume.button_rect.collidepoint(pos):
                    settings.volume.hit = True
            if event.type == pygame.MOUSEBUTTONUP:
                settings.volume.hit = False
        
        settings.check_events()
            
    if not settings.on:
        menu.on = True
        for event in events:
            if event == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if stg.button_rect.collidepoint(pos):
                        settings.volume.hit = True
            if event.type == pygame.MOUSEBUTTONUP:
                settings.volume.hit = False
            
    if menu.start_game:
        playing = True
        
    if playing:       
        start.stop()
        if begging_flag == False:
            fighting.play(-1)
            begging_flag = True
        draw_map(map_image)
        inv.display()
        cat.check_for_ground(borders)
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                cat.get_move(event)
                walk.play(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_boom(*event.pos)
                pygame.display.update()
                all_sprites.update()
        cat.move(borders)
        move_object(cat, dt, borders)
        draw_object(cat)
    
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
    
    show_boom()
    pygame.display.update()
pygame.quit()
