import pygame
from pygame.locals import *

width = 21
height = 43

class Player(object):
	
	self.posx = 0
	self.posy = 0

	def __init__(self, pos):
		(self.posx , self.posy) = pos

	def render(self,surface):
		self.man = pygame.image.load("man1.png").convert()
		surface.blit(self.man,(self.posx, self.posy))

	def move_up(self):
		self.posy -= 5
		if self.posy < 0:
			self.posy = 0

	def move_down(self):
		self.posy += 5
		if self.posy > 600 - height:
			self.posy = 600 - height

	def move_left(self):
		self.posx -= 5
		if self.posx < 0: 
			self.posx = 0

	def move_right(self):
	 	self.posx += 5
	 	if self.posx > 800 - width:
	 		self.posx = 800 - width
		