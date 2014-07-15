import life
import tkinter

CELL_SIZE = 4
WIDTH = 100
HEIGHT = 100

master = tkinter.Tk()

w = tkinter.Canvas(master, width=WIDTH*CELL_SIZE, height=HEIGHT*CELL_SIZE)
w.pack()

a = life.create_field(HEIGHT, WIDTH)
life.inhebit(a)

def tick():
    global a
    w.delete("all")
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            if a[i][j] != '.':
                w.create_rectangle(i* CELL_SIZE, j* CELL_SIZE, i* CELL_SIZE +1, j* CELL_SIZE +1)
    a = life.life(a)
    w.after(10, tick)


tick()
tkinter.mainloop()
