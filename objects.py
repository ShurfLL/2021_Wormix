import math
import random
import pygame
import numpy as np
from physics import calculate_accelerations
from map_editor import map_collision


class Player():
    def __init__(self):
        self.name = ""
        self.health = 500
        self.x = 0
        self.m = 10
        self.y = 0
        self.an = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.r = 20
        self.on_ground = False
        self.orientation = None
        self.sprite = 'models/cat.png'
        self.weapon = None

    
    def move(self, event, borders):
        if not self.on_ground:
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.vx = -5
            if event.key == pygame.K_RIGHT:
                self.vx = 5
            if event.key == pygame.K_UP:
                self.vy = -10
            if event.key == pygame.K_DOWN:
                self.vy = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.vx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.vy = 0

    def falling(self, borders):
        if self.on_ground:
            self.vx, self.vy = 0, 0
        else:
            calculate_accelerations(self)

    def check_for_ground(self, borders):
        self.on_ground = False
        b_x = np.shape(borders)[1]-1
        for i in range(max(self.x-self.r, 0),min(self.x+self.r, b_x)):
            if not borders[self.y+self.r][i]:
                self.on_ground = True
        print(self.on_ground)


class AbstractWeapon():
    def __init__(self):
        self.name = ""
        self.caption = ""
        self.an = 0
        self.bullet = None
        self.orientation = None
        self.sprite = None


class AbstractBullet():
    def __init__(self):
        self.name = ""
        self.an = 0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.orientation = None
        self.sprite = None


class Rocket(AbstractBullet):
    def __init__(self):
        super().__init__()
        self.name = "Rocket"
        self.sprite = 'models/rocket.png'




class Bazooka(AbstractWeapon):
    rocket = Rocket()
    def __init__(self):
        super().__init__()
        self.name = "Bazooka"
        self.caption = "Boom-Boom"
        self.sprite = 'models/bazooka.png'
        self.bullet = rocket


"""        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.vx = -10
            if event.key == pygame.K_RIGHT:
                self.vx = 10
            if event.key == pygame.K_UP:
                self.vy = -10
            if event.key == pygame.K_DOWN:
                self.vy = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.vx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.vy = 0"""