import pygame

class CheckCollision (object):
	def iamhit(self, p, cx1, cy1, cx2, cy2):
		(self.ppx, self.ppy) = p
		self.cpx1 = [] , self.cpx2 = []
		self.cpy1 = [] , self.cpy2 = []

		for i in range(2):
			self.cpx1[i] = cx1(i)
			self.cpy1[i] = cy1(i)
			self.cpx2[i] = cx2(i)
			self.cpy2[i] = cy2(i)

			if self.ppx < self.cpx1[i] + 100 and self.ppx + 21 > self.cpx1[i] + 100:
				if self.ppy + 43 > self.cpy1[i] and self.ppy < self.cpy1[i] + 50:
					print 'i am hit'
					return True 



