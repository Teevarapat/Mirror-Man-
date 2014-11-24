import pygame 
from pygame.locals import *

import gamelib
from player import Player
from car import Car

class MirrorMan(gamelib.SimpleGame):
	PURPLE = pygame.Color('purple')

	def __init__(self):
		super(MirrorMan, self).__init__('Mirror Man', MirrorMan.PURPLE)
		self.player = Player((380, 10))
		self.car = Car((0, 125))

	def init(self):
		super(MirrorMan, self).init()

	def update(self):
		self.car.move()

		if self.is_key_pressed(K_UP):
			self.player.move_up()
		elif self.is_key_pressed(K_DOWN):
			self.player.move_down()
		elif self.is_key_pressed(K_LEFT):
			self.player.move_left()
		elif self.is_key_pressed(K_RIGHT):
			self.player.move_right()

	def render(self, surface):
		self.background = pygame.image.load("background.png")
		surface.blit(self.background, (0, 0))
		self.player.render(surface)
		self.car.render(surface)

def main():
	game = MirrorMan()
	game.run()

if __name__ == '__main__':
	main()