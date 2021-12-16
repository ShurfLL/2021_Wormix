import pygame
from objects import *
from map_editor import *
from interface import *
from physics import *
from vis import *

paused, playing, settings = False, False, False
begging_flag = False
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

start = pygame.mixer.Sound('music/while_playing.mp3')
start.play(-1)

fighting = pygame.mixer.Sound("music/fighting.mp3")

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    
    events = pygame.event.get()

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
        start.stop()
        if begging_flag == False:
            fighting.play(-1)
            begging_flag = True
        draw_map(map_image)
        pause = Button(sc, W*5/6, H/6, pygame.image.load('models/pause_btn.png').convert_alpha(), 0.15)
        pause.display()
        if pause.click():
            paused = True
        inv.display()
        cat.check_for_ground(borders)
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                cat.get_move(event)
        cat.move(borders)
        move_object(cat, dt, borders)
        draw_object(cat)

        
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
            
    
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
pygame.quit()