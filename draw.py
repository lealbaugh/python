from Tkinter import *
import thing

master = None
w = None
player = None

def main(): 
	global master
	master = Tk()

	global w
	w = Canvas(master, width=200, height=100, highlightthickness=0)
	w.pack()
	w.focus_set()


	global player
	player = thing.Player(w, 0, 0, spritename="butterfly.gif")
	
	w.bind("<Up>", lambda arg: player.move("up", 10))
	w.bind("<Right>", lambda arg: player.move("right", 10))
	w.bind("<Left>", lambda arg: player.move("left", 10))
	w.bind("<Down>", lambda arg: player.move("down", 10))


	gamelogic()
	master.mainloop()

def gamelogic():
	player.update()
	master.after(50, gamelogic)




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

	#	w.bind("<Motion>", update_sprite)
	
	#global sprite 
	#sprite = w.create_rectangle(0,0,100,100)
	
	