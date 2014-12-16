import pygame
from player import Player
from car import Car

width = 21
height = 43

class CheckCollision (object):

	def iamhit(self, player, car, car2, car3, car4):
		self.player = player
		self.car = car
		self.car2 = car2
		self.car3 = car3
		self.car4 = car4

		if self.player.getX() < self.car.getX() + 100 and self.player.getX() + width > self.car.getX():
			if self.player.getY() + height > self.car.getY() and self.player.getY() < self.car.getY() + 50:
				#print 'i am hit by car 1'
				return True

		elif self.player.getX() < self.car3.getX() + 100 and self.player.getX() + width > self.car3.getX():
			if self.player.getY() + height > self.car3.getY() and self.player.getY() < self.car3.getY() + 50:
				#print 'i am hit by car3'
				return True

		elif self.player.getX() > self.car2.getX() and self.player.getX() + width < self.car2.getX() + 100:
			if self.player.getY() + height > self.car2.getY() and self.player.getY() < self.car2.getY() + 50:
				#print 'i am hit by car2'
				return True

		elif self.player.getX() > self.car4.getX() and self.player.getX() + width < self.car4.getX() + 100:
			if self.player.getY() + height > self.car4.getY() and self.player.posy < self.car4.getY() + 50:
				#print 'i am hit by car4'
				return True