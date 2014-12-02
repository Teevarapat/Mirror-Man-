import pygame
import random
from pygame.locals import *

width = 100
height = 50

class Car(object):

	def __init__(self, px, py, typecar, speed = 10):
		
		self.px = px
		self.py = py
		self.type = typecar

		self.vx = speed + random.randint(0,12)
		

	def render(self, surface):

		if self.type == 'yellow':
			self.car = pygame.image.load("car1.png")
			surface.blit(self.car, (self.px, self.py))

		elif self.type == 'red':
			self.car2 = pygame.image.load("car2.png")
			surface.blit(self.car2, (self.px, self.py))


	def move(self):
	
		if self.type == 'yellow':
			self.px += self.vx
			if(self.px > 800):
				self.px = 0 - random.randint(100,1000)

		if self.type == 'red':
			self.px -= self.vx
			if(self.px < 0 - width):
				self.px = 800 + random.randint(100,1000)

	def getX(self):
		return self.px

	def getY(self):
		return self.py