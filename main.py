import math
import pygame


WIDTH = 800
HEIGHT = 600
FPS = 30


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
cat = pygame.Surface((400,400))
cat = pygame.Surface.convert_alpha(cat)
cat.fill((0,0,0,0))
cat_image = pygame.image.load('models/cat.png').convert()
cat.blit(cat_image, (0,0))
screen.blit(cat, (0,0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()