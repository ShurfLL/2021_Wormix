import pygame
from objects import *
from map_editor import Map
from interface import *
from physics import move_object
from vis import *

paused, playing = False, False
beginning_flag = False

menu = MainMenu(sc)
settings = SettingsMenu(sc)
pause = PauseMenu(sc)

cat1 = Player(450, 50, True)
cat2 = Player(600, 400) 
inv = Inventory(sc, [cat1.weapon])
players = [cat1, cat2]
weapons = [cat1.weapon, cat2.weapon]
bullets = []
water = Death_water()
game_map = Map()
game_map.create_map('maps/map1.jpg')
dt = 0.5
start = pygame.mixer.Sound('music/while_playing.ogg')
start.play(-1)
start.set_volume(0.2)
fighting = pygame.mixer.Sound("music/fighting.ogg")
fighting.set_volume(0.2)
walk = pygame.mixer.Sound("music/walk-compress.ogg")


def game(beginning_flag, playing):
    """Соединяет все элементы игры и обнавляет ее состояния"""
    start.stop()
    if beginning_flag == False:
        fighting.play(-1)
        beginning_flag = True
    game_map.draw_map(sc)
    inv.draw()
    pause.draw()
    pause.check_events()
    if pause.to_menu:
        fighting.stop()
        if beginning_flag == True:
            start.play(-1)
            beginning_flag = False
        pause.on = False
        pause.to_menu = False
        playing = False
        menu.on = True
    if pause.settings:
        fighting.stop()
        if beginning_flag == True:
            start.play(-1)
            beginning_flag = False
        pause.on = False
        pause.settings = False
        playing = False
        settings.on = True
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        for cat in players:
            if cat.active:
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    cat.get_move(event)
                    cat.give_weapon(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bullets.append(cat.weapon.fire_start())
            cat.weapon.get_target(event)
            # cat.weapon.update(event) 
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # create_boom(*event.pos)
            # pygame.display.update()
            # all_sprites.update()
    for bullet in bullets:
        draw_object(bullet)
        move_object(bullet, dt, game_map.borders)
    for cat in players:
        cat.weapon.target()
        cat.check_for_ground(game_map.borders)
        cat.move(game_map.borders)
        move_object(cat, dt, game_map.borders)
        cat.weapon_update()
        draw_object(cat)
        draw_object(cat.weapon)
        draw_health_box(cat)
        water.kill_player(cat)
    water.rise_of_water_level()
    water.draw(sc)
    
    return beginning_flag, playing

def main_menu(finished, playing):
    """Обновляет состояния меню"""
    if menu.on:
        menu.draw()
        menu.check_events()
    
    if menu.quit:
        finished = True
    
    if menu.settings:
        menu.settings = False
        settings.on = True
        
    if menu.info:
        menu.AboutMenu()
        
    if menu.start_game:
        menu.start_game = False
        playing = True
        menu.on = False
    return finished, playing

def settings_menu(beginning_flag):
    """Обновляет состояния настроек и музыки"""
    if settings.on:
        fighting.stop()
        if beginning_flag == True:
            start.play(-1)
            beginning_flag = False
        menu.settings = False
        settings.draw()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if settings.volume.button_rect.collidepoint(pos):
                    settings.volume.hit = True
            if event.type == pygame.MOUSEBUTTONUP:
                settings.volume.hit = False
        start.set_volume(settings.volume.start_val/100)
        fighting.set_volume(settings.volume.start_val/100)
        walk.set_volume(settings.volume.start_val/100)
        settings.check_events()
        
    if not settings.on:
        menu.on = True
    return beginning_flag

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    
    finished, playing = main_menu(finished, playing)    
    beginning_flag = settings_menu(beginning_flag)
        
    if playing:
        beginning_flag, playing = game(beginning_flag, playing)
        
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
    show_boom()
    pygame.display.update()
pygame.quit()
