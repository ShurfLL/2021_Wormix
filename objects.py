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
		self.orientation
		self.sprite = 'models/cat'
		self.weapon



class AbstractWeapon():
    def __init__(self):
        self.name = ""
        self.caption = ""
        self.an = 0
        self.bullet
        self.orientation
        self.sprite


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
		self.orientation
		self.sprite


class bazooka(AbstractWeapon):
	def __init__(self):
		super().__init__()
		self.name = "Bazooka"
		self.caption = "Boom-Boom"
		self.sprite = 'models/bazooka.png'

