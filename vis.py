import pygame as pg
import sys

W = 1400
H = 660

sc = pg.display.set_mode((W, H))
sc.fill((100, 150, 200))

def draw_surface(name):
    surf = pg.image.load(name)
    rect = surf.get_rect(bottomright=(W, H))
    sc.blit(surf, rect)
    pg.display.update()

def draw_left_worm(x,y):
    surf1 = pg.image.load('worms_left.png')
    new_worm = pg.transform.scale(surf1, (60, 60))
    new_worm.set_colorkey((255, 255, 255))
    sc.blit(new_worm, (x, y))
    pg.display.update()

draw_surface('3flour22.jpg')
draw_left_worm(550, 580)


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pg.time.delay(20)
