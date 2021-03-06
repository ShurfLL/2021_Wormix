"""Модуль содержит класс взрыва и функции изображения, визуализации объектов игры."""

import pygame
import sys
from os import path

W = 1400
"""Ширина окна"""

H = 660
"""Высота окна"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
"""Параметры цвета"""

pygame.init()
sc = pygame.display.set_mode((W, H))
sc.fill((100, 150, 200))

FPS = 60


# def rot_center(image, angle):
#     """поворачивает surface отн. центра."""

#     loc = image.get_rect().center
#     rot_sprite = pygame.transform.rotate(image, angle)
#     rot_sprite.get_rect().center = loc
#     return rot_sprite
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Explosion(pygame.sprite.Sprite):
    """Создание спрайта взрыва."""
    def __init__(self, center, size):
        """Конструктор принимает координаты центра взрыва и его параметрический размер."""
        pygame.sprite.Sprite.__init__(self)   # инициализатор встроенных классов Sprite
        self.size = size
        self.image = explosion_anim[self.size][0] 
        self.rect = self.image.get_rect()   # вычисление прямоугольника, который может окружить картинку
        self.rect.center = center   
        self.frame = 0
        self.last_update = pygame.time.get_ticks()   # количество миллисекунд, прошедшее с момента вызова pygame.init()
        self.frame_rate = 50   # скорость смены кадров: чем больше, тем медленнее

    def update(self):
        """Смена кадров, в зависимости от прошедшего времени."""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


explosion_anim = {}
explosion_anim['lg'] = []

for i in range(9):
    """Заполнение словаря рисунками взрыва."""
    filename = 'models/regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename)
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)

all_sprites = pygame.sprite.Group()


def draw_object(obj): 
    """Рисует на экране произвольный объект."""
    surf=obj.sprite
    surf=pygame.transform.scale(surf, (2*obj.r, 2*obj.r))
    surf = rot_center(surf, obj.an)
    if obj.orientation == "right":
        surf=pygame.transform.flip(surf,1, False)
    sc.blit(surf, (obj.x-obj.r, obj.y-obj.r))

    
def draw_surface(name): 
    """Создаёт на экране поверхность."""
    surf = pygame.image.load(name)
    rect = surf.get_rect(bottomright=(W, H))
    sc.blit(surf, rect)
    pygame.display.update()


def create_boom(x,y): 
    """Вызывывает спрайт взрыва с центром в точке."""
    global all_sprites
    expl = Explosion((x, y), 'lg')
    all_sprites = pygame.sprite.Group() # инициализация группы
    all_sprites.add(expl) # добавление спрайта в группу

    
def show_boom(): 
    """Изображает спрайт на экране."""
    global all_sprites
    all_sprites.update()
    all_sprites.draw(sc)
    #pygame.display.update()
    
    
def draw_health_box(obj):
    """Изображает прямоугольник, показывающий уровень здоровья игрока."""
    pygame.draw.rect(sc, BLUE, (obj.x - obj.r - 2, obj.y - 1.5 * obj.r - 2, 40, 7))
    pygame.draw.rect(sc, RED, (obj.x - obj.r, obj.y - 1.5*obj.r, obj.health / 12.5, 3))

