from Tkinter import *

old_x = 0
old_y = 0
rect_length = 10
rect_width = 10
rect = None
w = None

def main(): 
	master = Tk()
	global w
	w = Canvas(master, width=200, height=100)
	w.pack()

	w.create_line(0, 0, 200, 100)
	w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
	#rect = w.create_rectangle(0, 0, 10, 10, fill="blue")
	w.bind("<Motion>", update_square)

	mainloop()

def update_square(thisevent):
	global old_x, old_y, rect

	new_x, new_y = thisevent.x, thisevent.y
	dx = new_x - old_x
	dy = new_y - old_y
	old_x = new_x
	old_y = new_y

	try: 
		w.move(rect, dx, dy)
	except: 
		rect = w.create_rectangle(new_x, new_y, new_x + rect_length, new_y + rect_width, fill="blue")


if __name__ == "__main__": 
	main()
