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
		self.orientation = None
		self.sprite = 'models/cat'
		self.weapon = None



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


