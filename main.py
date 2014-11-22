import pygame 
from pygame.locals import *

import gamelib

class MirrorMan(gamelib.SimpleGame):
	PURPLE = pygame.Color('purple')

	def __init__(self):
		super(MirrorMan, self).__init__('Mirror Man', MirrorMan.PURPLE)

	def init(self):
		super(MirrorMan, self)

	def update(self):
		pass

	def render(self):
		pass

def main():
	game = MirrorMan()
	game.run()

if __name__ == '__main__':
	main()