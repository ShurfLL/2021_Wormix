import pygame
import numpy as np
import math
from physics import calculate_accelerations
from map_editor import map_collision, check_traj

class AbstractWeapon():
    def __init__(self):
        self.name = ""
        self.caption = ""
        self.an = 0
        self.wan = 0
        self.f_power = 0
        self.fire_on = False
        self.x = 0
        self.y = 0
        self.r = 20
        self.bullet = None
        self.orientation = None
        self.sprite = None

    def targetting(self, event):    ######## Пофиксить прицеливание!!!!!!!!!!!!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.an < 90:
                self.wan = -5
            if event.key == pygame.K_DOWN and self.an > -90:
                self.wan = 5
        if self.an >= 80 or self.an <= -80:
            self.wan = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_UP:
                self.wan = 0
        

    def fire(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.fire_on = True
        if self.fire_on:
            if self.f_power < 30:
                self.f_power += 1
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.bullet.vx = self.f_power*math.cos(self.an)
            self.bullet.vy = -self.f_power*math.sin(self.an)
            self.fire_on = False
            return self.bullet

    def update(self, event):##### Тут тоже!!!!!!!
        self.targetting(event)
        self.fire(event)


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
        self.r = 10
        self.max_damage = 0
        self.fire_force = 0
        self.active = True
        self.orientation = None
        self.sprite = None

    def bullet_collision(self, borders, image_mass, players):
        for player in players:
            if object_collision(self, player) or map_collision(self, borders):
                self.active = False
                remove_part_of_map(self.x, self.y, self.fire_force, borders, image_mass)
                for player in players:
                    dist = ( player.x - self.x ) ** 2 + ( player.y - self.y ) ** 2
                    if dist <= self.fire_force ** 2:
                        collision_an = math.atan2((player.y - self.y), (player.x - self.x))    #Угол окидывания игрока
                        player.health -= int( self.max_damage - self.max_damage * dist / self.fire_force )      #Нанесение урона игроку
                        player.vx +=  math.cos(collision_an) * ( v_0 - v_0 * dist / self.fire_force )     #Откидывание игрока из-за взрыва
                        player.vy +=  math.sin(collision_an) * ( v_0 - v_0 * dist / self.fire_force )


class Rocket(AbstractBullet):
    def __init__(self):
        super().__init__()
        self.name = "Rocket"
        self.max_damage = 90
        self.fire_force = 15
        self.active = True
        self.orientation = "right"
        self.sprite = 'models/Rocket.png'



class Bazooka(AbstractWeapon):
    def __init__(self):
        super().__init__()
        self.name = "Bazooka"
        self.orientation = "left"
        self.caption = "Boom-Boom"
        self.bullet = "Rocket"
        self.sprite = 'models/bazooka.png'
        self.bullet = Rocket()



class UziBullet(AbstractBullet):
    def __init__(self):
        super().__init__()
        self.name = "UziBullet"
        self.an = 0
        self.fire_force = 4
        self.max_damage = 50
        self.active = True
        self.orientation = "right"
        self.sprite = 'models/UziBullet.png'


class Uzi(AbstractWeapon):
    def __init__(self):
        super().__init__()
        self.name = "Uzi"
        self.orientation = "left"
        self.caption = "Boom-Boom"
        self.bullet = "UziBullet"
        self.sprite = 'models/uzi.png'
        self.bullet = UziBullet()


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
        self.start_bjump = False
        self.on_ground = False
        self.orientation = "left"
        self.move_left = False
        self.move_right = False
        self.sprite = 'models/cat.png'
        self.weapon = Uzi()
    
    def give_weapon(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            self.weapon = Bazooka()
            self.weapon.x = self.x
            self.weapon.y = self.y
            self.weapon.orientation = self.orientation
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            self.weapon = Uzi()
            self.weapon.x = self.x
            self.weapon.y = self.y
            self.weapon.orientation = self.orientation

    def weapon_update(self):
        if self.weapon != None:
            self.weapon.x = self.x
            self.weapon.y = self.y
            self.weapon.orientation = self.orientation

            
    def get_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left = True
                self.orientation = "left"
            if event.key == pygame.K_RIGHT:
                self.move_right = True
                self.orientation = "right"
            if event.key == pygame.K_RETURN:
                self.start_jump = True
            if event.key == pygame.K_r:
                self.start_bjump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_RIGHT:
                self.move_right = False

    def jump(self, borders):
        if not check_traj(self, 0, -3, borders):
            self.on_ground = False
            self.y -= 3
            #self.vx = 3 if self.orientation == "right" else -3
            if self.orientation == "right":
                self.vx = 10
            elif self.orientation == "left":
                self.vx = -10
            self.vy = -15
            self.start_jump = False

    def backjump(self, borders):
        if not check_traj(self, 0, -3, borders):
            self.on_ground = False
            self.y -= 3
            #self.vx = 3 if self.orientation == "right" else -3
            if self.orientation == "right":
                self.vx = -3
            elif self.orientation == "left":
                self.vx = 3
            self.vy = -25
            self.start_bjump = False
    
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
                self.jump(borders)
            if self.start_bjump:
                self.backjump(borders)
        else:
            calculate_accelerations(self)

    def check_for_speed(self):
        if self.vy >= 10:
            self.ay = 0

    def check_for_ground(self, borders):
        self.on_ground = False
        b_x = np.shape(borders)[1]-1
        for i in range(max(self.x-self.r, 0),min(self.x+self.r, b_x)):
            if not borders[self.y+self.r][i]:
                self.on_ground = True


class Death_water():
    def __init__():
        self.time = 300
        self.y = 0
        self.sprite = "models/water.png"

if __name__ == "__main__":
    print("This module is not for direct call!")
