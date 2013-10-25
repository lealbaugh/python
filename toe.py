class Board:
	def __init__(self):
		self.board = [[' ' for col in range(3)] for row in range(3)]
		self.value = None
		self.move = None
		

	def get_board(self):
		return self.board

	def __str__(self):
		board = ''
		for row in self.board:
			board += "|".join(row)+"\n"
		return board


	def set_board(self,board):
		self.board = board
		self.value = None

	def is_finished(self):
		return self.check_three_same() is not None

	def set_spot(self, row, col):
		if self.board[row][col] ==' ':
			self.board[row][col]=self.get_player()
			return True
		else:
			return False

	def get_value(self):
		if not self.value:
			self.update_knowledge()
		return self.value

	def update_knowledge(self):
		winner = self.check_three_same()
		if winner:
			if winner == 'X':
				self.value = 1
			else:
				self.value = -1
		else:
			self.value, self.move = self.create_children()

	def make_move(self):
		if self.is_finished():
			print self
			print "Game Over!"
			return
		if not self.move:
			found = False
			for r in range(len(self.board)):
				for c in range(len(self.board)):
					if self.set_spot(r,c):
						found = True
						break
				if found:
					break
			print self
		else:
			self.set_spot(self.move[0], self.move[1])
			print self
		self.move = None
		self.value = None

	def robot_move(self):
		self.update_knowledge()
		self.make_move()


	def get_player(self):
		turns = 0
		for r in self.board:
			for i in r:
				if i!=" ":
					turns +=1
		return 'X' if turns%2==0 else 'O'

	def create_children(self):
		player = self.get_player()
		children_values = []
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				if self.board[row][col] == ' ':
					child = Board()
					child.set_board([r[:] for r in self.board])
					child.set_spot(row,col)
					child_value = child.get_value()
					children_values.append([child_value, [row, col]])
		if not children_values:
			return [0, None]
		return max(children_values) if player == 'X' else min(children_values)


	def three_same(self, ls):
		a,b,c = ls
		if a == b and b == c:
			if a == " ":
				return None
			else:
				return a
		else:
			return None


	def check_three_same(self):
		successful_player = None
		for row in self.board:
			successful_player = successful_player or self.three_same(row)
		for col in range(len(self.board)):
			successful_player = successful_player or self.three_same([self.board[row][col] for row in range(len(self.board))])
		successful_player = successful_player or self.three_same([self.board[0][0],self.board[1][1],self.board[2][2]]) 
		successful_player = successful_player or self.three_same([self.board[0][2],self.board[1][1],self.board[2][0]])

		return successful_player


if __name__ == '__main__':
	board = Board()
	while not board.is_finished():
		if board.get_player() == 'X':
			row = input("Enter row:")
			col = input("Enter column:")
			board.move = [row,col]
			board.make_move()
		else:
			board.robot_move()





