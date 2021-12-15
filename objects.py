import math
import random
import pygame
import numpy as np
from physics import calculate_accelerations
from map_editor import map_collision, check_traj


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
        self.dx = 2
        self.dy = 5
        self.start_jump = False
        self.on_ground = False
        self.orientation = "left"
        self.move_left = False
        self.move_right = False
        self.V_sign = 0
        self.sprite = 'models/cat.png'
        self.weapon = None
    
    def get_move(self, event):

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                self.move_left = True
                self.orientation = "left"
            if event.key == pygame.K_RIGHT:
                self.move_right = True
                self.orientation = "right"
            if event.key == pygame.K_SPACE:
                self.start_jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_RIGHT:
                self.move_right = False
        
        
        #if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        """
        if (event.type == pygame.KEYDOWN):
            is_up = 1
        else:
            is_up = -1   
        

        if event.key == pygame.K_LEFT:
            self.V_sign -= 1 * is_up

        if event.key == pygame.K_RIGHT:
            self.V_sign += 1 * is_up 


        print(self.V_sign)
"""

    def jump(self):
        self.vx = 3
        self.vy = -20
    
    
    def move(self,borders):
        if self.on_ground:
            if self.move_right and not check_traj(self, self.dx, 0, borders):
                self.x += self.dx
            elif self.move_right and not check_traj(self, self.dx, -self.dy, borders):
                self.x += self.dx
                self.y -= self.dy
            if self.move_left and not check_traj(self, -self.dx, 0, borders):
                self.x -= self.dx
            elif self.move_left and not check_traj(self, -self.dx, -self.dy, borders):
                self.x -= self.dx
                self.y -= self.dy
            if self.start_jump:
                self.jump()
                self.start_jump = False
        else:
            calculate_accelerations(self)

    def check_for_speed(self):
        if self.vy >= 10:
            self.ay = 0


    def check_for_ground(self, borders):
        self.on_ground = False
        b_x = np.shape(borders)[1]-1
        for i in range(max(self.x-self.r, 0),min(self.x+self.r, b_x)):
            if not borders[self.y+self.r+3][i]:
                self.on_ground = True


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
                self.vy = 0

                    def move(self, borders):
        if self.on_ground:
            if self.move_left:
                self.x -= 1
                if map_collision(self, borders):
                    self.y -= 5
                    if map_collision(self, borders):
                        self.y += 5
                        self.x += 1
            if self.move_right:
                self.x += 1
                if map_collision(self, borders):
                    self.y -= 5
                    if map_collision(self, borders):
                        self.y += 5
                        self.x -= 1
    
    def jump(self):
        if self.on_ground:
            self.vy -= 5
            if self.orientation == "right":
                self.vx += 5
            else:
                self.vx -= 5



    def falling(self, borders):
        if self.on_ground:
            self.vy = 0
        else:
            self.ay = 10"""