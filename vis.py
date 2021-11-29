import pygame as pg
import sys

W = 1400
H = 660

sc = pg.display.set_mode((W, H))
sc.fill((100, 150, 200))

def draw(name):

    surf = pg.image.load(name)
    rect = surf.get_rect(bottomright=(W, H))
    sc.blit(surf, rect)
    pg.display.update()



draw('3flour22.jpg')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pg.time.delay(20)
