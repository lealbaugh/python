from Tkinter import *
import Thing

master = None
old_x = 0
old_y = 0
w = None
sprite = None
butterfly = None
rect = None

def main(): 
	global master
	master = Tk()
	global w
	w = Canvas(master, width=200, height=100)
	w.pack()
	w.bind("<Motion>", update_sprite)
	global butterfly
	butterfly = PhotoImage(file="butterfly.gif")
	global sprite 
	sprite = w.create_image(old_x, old_y, image=butterfly)
	global rect
	rect = w.create_rectangle(0, 0, 10, 10, fill="blue")

	gamelogic()
	master.mainloop()

def gamelogic():
	w.move(rect, randint(-5,5), randint(-5,5))
	master.after(50, gamelogic)


def update_sprite(thisevent):
	global old_x, old_y

	new_x, new_y = thisevent.x, thisevent.y
	dx = new_x - old_x
	dy = new_y - old_y
	old_x = new_x
	old_y = new_y
	w.move(sprite, dx, dy)

		



if __name__ == "__main__": 
	main()

#_________________________________________________________________________________________
#	global rect
#	rect = w.create_rectangle(old_x, old_y, old_x + rect_length, old_y + rect_width, fill="blue")
#	rect_length = 10
#	rect_width = 10
#	rect = None

	#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
	#rect = w.create_rectangle(0, 0, 10, 10, fill="blue")