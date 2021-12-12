import pygame
from objects import *
from map_editor import *
from interface import *
from physics import *
from vis import *

paused, playing, settings = False, False, False
cat = Player()
inv = Inventory(sc, [cat.weapon])
cat.x=400
cat.y = 50
objects=[cat]
map_image = pilImageToSurface(image_mass)
dt = 0.5

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    
    
    if not playing and not paused:
        state = MainMenu(sc)
        if state[1]:
            finished = True
        if state[2]:
            settings = True
        if state[0]:
            playing = True
        if state[3]:
            AboutMenu(sc)
            
            
    if settings:
        stg = SettingsMenu(sc)
        if not stg:
            settings = False
            
            
    if playing:       
        draw_map(map_image)
        pause = Button(sc, W*5/6, H/6, pygame.image.load('models/pause_btn.png').convert_alpha(), 0.15)
        pause.display()
        if pause.click():
            paused = True
        inv.display()
        cat.check_for_ground(borders)
        cat.falling(borders)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            cat.move(event, borders)
        draw_object(cat)
        recalculate_objects_positions(objects, dt)
        
    if paused:
        pause_menu = PauseMenu(sc)
        if pause_menu[0]:
            paused = False
        if pause_menu[1]:
            playing = False
            paused = False
        if pause_menu[2]:
            settings = True
            playing = False
            paused = False
            
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
pygame.quit()
