import math
import random
import pygame
import numpy as np
from physics import calculate_accelerations
from map_editor import map_collision, check_traj, remove_part_of_map

def objects_collision(obj1, obj2):
    dist = int(math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2))
    return (obj1.r + obj2.r <= dist)


class AbstractWeapon():
    def __init__(self):
        self.name = ""
        self.caption = ""
        self.an = 0
        self.f_power = 0
        self.fire_on = False
        self.x = 0
        self.y = 0
        self.r = 10
        self.bullet = None
        self.orientation = None
        self.sprite = None

    def targetting(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.an < 90:
                self.an += 5
            if event.key == pygame.K_DOWN and self.an > 0:
                self.an -= 5

    def fire(self, event):
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            self.fire_on = True
        if self.fire_on:
            if self.f_power < 30:
                self.f_power += 1
        if event.type == pygame.KEYUP and event.key == K_SPACE:
            self.bullet.vx = self.f_power*math.cos(self.an)
            self.bullet.vy = -self.f_power*math.sin(self.an)
            self.fire_on = False
            return self.bullet

    # def fire_start(self):
    #     self.fire_on = True

    # def power_up(self):
    #     if self.fire_on:
    #         if self.f_power < 30:
    #             self.f_power += 1

    # def fire_end(self):
    #     self.bullet.vx = self.f_power*math.cos(self.an)
    #     self.bullet.vy = -self.f_power*math.sin(self.an)
    #     self.fire_on = False
    #     return self.bullet


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
        self.r = 5
        self.fire_force = 0
        self.active = True
        self.orientation = None
        self.sprite = None

    def bullet_collision(self, borders, image_mass, players):
        if map_collision(self, borders):
            self.active = False
            remove_part_of_map(self.x, self.y, self.fire_force, borders, image_mass)
            for player in players:
                dist = ( player.x - self.x ) ** 2 + ( player.y - self.y ) ** 2
                if dist <= self.fire_force ** 2:
                    collision_an = math.atan2((player.y - self.y), (player.x - self.x))    #Угол окидывания игрока
                    player.health -= int( 125 - 125 * dist / self.fire_force )      #Нанесение урона игроку
                    player.vx +=  math.cos(collision_an) * ( v_0 - v_0 * dist / self.fire_force )     #Откидывание игрока из-за взрыва
                    player.vy +=  math.sin(collision_an) * ( v_0 - v_0 * dist / self.fire_force )


class Rocket(AbstractBullet):
    def __init__(self):
        super().__init__()
        self.name = "Rocket"
        self.an = 0
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
        self.sprite = 'models/Bazooka.png'
        self.bullet = Rocket()



class UziBullet(AbstractBullet):
    def __init__(self):
        super().__init__()
        self.name = "UziBullet"
        self.an = 0
        self.fire_force = 4
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
        self.sprite = 'models/Uzi.png'
        self.bullet = UziBullet()


class Player():
    bazooka = Bazooka()
    uzi = Uzi()
    available_weapons = dict({'bazooka':bazooka, 'uzi':uzi})        #Доступные оружия для игрока
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
        self.sprite = 'models/cat.png'
        self.weapon = None
    
    def give_weapon(self, dict_weapons, name):
        self.weapon = weapons[name]
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_RIGHT:
                self.move_right = False

    def jump(self, borders):
        if not check_traj(self, 0, -20, borders):
            self.y -= 20
            #self.vx = 3 if self.orientation == "right" else -3
            if self.orientation == "right":
                self.vx = 3
            elif self.orientation == "left":
                self.vx = -3
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
                self.start_jump = False
                self.jump(borders)
                
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

    def give_weapon(self):
        self.weapon = weapon_selection(available_weapons)         #Нужно создать функцию выбора оружия из словаря оружий