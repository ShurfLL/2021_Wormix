import pygame
from objects import *
from map_editor import *
from interface import *
from physics import *
from vis import *


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
    draw_map(map_image)
    inv.display()
    cat.check_for_ground(borders)
    cat.falling(borders)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        cat.move(event, borders)
    draw_object(cat)
    recalculate_objects_positions(objects, dt)
    pygame.display.update()
pygame.quit()
