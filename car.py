import pygame
import random
from pygame.locals import *

width = 100
height = 50

class Car(object):

	def __init__(self, pos, pos2, speed = 8):
		
		self.posx1 = range(2)
		self.posy1 = range(2)
		self.posx2 = range(2)
		self.posy2 = range(2)

		for i in range(2):
			(self.posx1[i], self.posy1[i]) = pos
			self.posx1[1] -= 100

		for j in range(2):
			(self.posx2[j], self.posy2[j]) = pos2
			self.posx2[1] += 100
			#print(self.posx2[i], self.posy2[i])

			#print(self.posx[i], self.posy[i])

		self.vx1 = speed
		self.vx2 = speed + 4

	def render(self, surface):
		self.car = range(2)
		self.car2 = range(2)

		for i in range(2):
			self.car[i] = pygame.image.load("car1.png")
			surface.blit(self.car[i], (self.posx1[i], self.posy1[i] + i*200))
			#print(self.posx[i], self.posy[i])

		for j in range(2):
			self.car2[j] = pygame.image.load("car2.png")
			surface.blit(self.car2[j], (self.posx2[j], self.posy2[j] + j*200))
			print(self.posx2[j], self.posy2[j])

	def move(self):
		
		for i in range(2):
			self.posx1[i] += self.vx1
			if(self.posx1[i] > 800):
				self.posx1[i] = 0 - random.randint(100,1000)

		for j in range(2):
			self.posx2[j] -= self.vx2
			if(self.posx2[j] < 0 - width):
				self.posx2[j] = 800 + random.randint(100,1000)