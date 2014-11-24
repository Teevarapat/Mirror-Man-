import pygame
from pygame.locals import *

width = 100
height = 50

class Car(object):

	def __init__(self, pos, speed = 1):
		(self.posx, self.posy) = pos
		self.vx = speed

	def render(self, surface):
		self.car = pygame.image.load("car1.png")
		surface.blit(self.car, (self.posx, self.posy))

	def move(self):
		while True:
			self.posx += self.vx
			if(self.posx > 800):
				self.posx = 0 - width