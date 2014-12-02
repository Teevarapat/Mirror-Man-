import pygame 
from pygame.locals import *

import gamelib
from player import Player
from car import Car
from checkcollision import CheckCollision

class MirrorMan(gamelib.SimpleGame):
	PURPLE = pygame.Color('purple')

	def __init__(self):
		super(MirrorMan, self).__init__('Mirror Man', MirrorMan.PURPLE)
		self.gameover = False
		self.player = Player((380, 10))
		self.car = Car(0, 125, 'yellow')
		self.car2 = Car(800, 225, 'red')
		self.car3 = Car(-100, 325, 'yellow')
		self.car4 = Car(900, 425, 'red')
		#self.checkcollision = CheckCollision(self.player, self.car, self.car2, self.car3, self.car4)

	def init(self):
		super(MirrorMan, self).init()

	def update(self):
		collision = CheckCollision()
		if not self.gameover:
			self.car.move()
			self.car2.move()
			self.car3.move()
			self.car4.move()

			if self.is_key_pressed(K_UP):
				self.player.move_up()
			elif self.is_key_pressed(K_DOWN):
				self.player.move_down()
			elif self.is_key_pressed(K_LEFT):
				self.player.move_left()
			elif self.is_key_pressed(K_RIGHT):
				self.player.move_right()

		if collision.iamhit(self.player, self.car, self.car2, self.car3, self.car4):
			self.gameover = True

	def render(self, surface):

		self.background = pygame.image.load("background.png")
		surface.blit(self.background, (0, 0))
		self.player.render(surface)
		self.car.render(surface)
		self.car2.render(surface)
		self.car3.render(surface)
		self.car4.render(surface)

		if self.gameover:
			self.bye = pygame.image.load("gameover.jpg")
			surface.blit(self.bye, (150, 150))


def main():
	game = MirrorMan()
	game.run()

if __name__ == '__main__':
	main()