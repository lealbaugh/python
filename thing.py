from Tkinter import *
from random import randint

class Sprite(object):
	def __init__(self, world, this_x=0, this_y=0, spritename="default.gif"):
		self.sprite = PhotoImage(file=spritename)
		self.x = this_x
		self.y = this_y
		self.future_x = 0
		self.future_y =0
		self.world = world
	#	self.image = self.world.create_rectangle(self.x, self.y, self.x+10, self.y+10, fill="blue")
		self.image = self.world.create_image(self.x, self.y, image=self.sprite)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def update(self):
		new_x, new_y = randint(-3,5)
		world.move(self, new_x, new_y)


class Player(Sprite):
	def move(self, direction="left", displacement=1):
		print direction
		if direction == "up":
			self.future_y = self.y - displacement
		elif direction == "down":
			self.future_y = self.y + displacement
		elif direction == "right":
			self.future_x = self.x + displacement
		elif direction == "left":
			self.future_x = self.x - displacement
			
		dx = self.future_x - self.x
		dy = self.future_y - self.y
		self.x = self.future_x
		self.y = self.future_y
		self.world.move(self.image, dx, dy)


	def update(self):
		pass
