from random import randint

class Thing:
	def __init__(self, root, x='0', y='0', spritename="default.gif"):
		sprite = PhotoImage(file=spritename)
		self.x = x
		self.y = y
		root.create_image(self.x, self.y, image=sprite)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def update(self):
		new_x, new_y = randint(-3,5)
		root.move(self, new_x, new_y)



	 
