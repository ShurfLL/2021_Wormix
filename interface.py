import pygame
from objects import Bazooka

FPS = 30
WIDTH = 800
HEIGHT = 500


GAMESCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #
GAMESCREEN.fill((0, 0, 0)) #
    

def get_object_pic(weapon):
    return pygame.image.load(weapon.sprite)


class Inventory():
    def __init__(self, weapons):
        self.inventory = weapons
        self.x, self.y = WIDTH/3, HEIGHT*4/5
    
    
    def display_inventory(self, display):
        dx = 0
        for gun in self.inventory:
            window = pygame.Surface((70, 50))
            window.fill((186, 140, 99))
            window.blit(pygame.transform.scale(get_object_pic(gun), (70,50)),
                        (0, 0))
            display.blit(window,  (self.x + dx, self.y))
            dx += 70
        
        
    def cursor():
        pass
    
    
pygame.init()
'''
проверка
inv = Inventory([bazooka()])
inv.display_inventory(GAMESCREEN)
'''

class Menu():
    def __init__(self, game):
        pass
    

class PauseMenu(Menu):
    def __init__(self):
        pass

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()