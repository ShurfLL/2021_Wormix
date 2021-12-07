import math
import random
import pygame


class Player():
    def __init__(self):
        self.name = ""
        self.health = 500
        self.x = 0
        self.y = 0
        self.an = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.r = 20
        self.orientation = None
        self.sprite = 'models/cat.png'
        self.weapon = None

    
    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.vx = -1
            if event.key == pygame.K_RIGHT:
                self.vx = 1
            if event.key == pygame.K_UP:
                self.vy = -1
            if event.key == pygame.K_DOWN:
                self.vy = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.vx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.vy = 0





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


