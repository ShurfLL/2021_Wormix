import pygame
from objects import *
from map_editor import *
#from interface import *
from physics import *
from vis import *


cat = Player()
objects=[cat]
map_image = pilImageToSurface(image_mass)
print(type(map_image))
dt = 1

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    draw_map(map_image)
    recalculate_objects_positions(objects, dt)
    draw_object(cat)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        cat.move(event)
pygame.quit()
