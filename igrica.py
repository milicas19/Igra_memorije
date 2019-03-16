from tkinter import *

class MatrixOfButtons:
    #master je root
    def __init__(self,master,frame,n):
        photo=PhotoImage(file='a.gif')
        for i in range(0,n):
            for j in range(0,n):
                self.b = Button(frame,image=photo,text = str(i)+''+str(j))
                self.b.image=photo
                self.b.grid(row = i,column = j)

def raise_frame(frame):
    frame.tkraise()

def sel():
    if var1.get()==1:
        print("1 vs rac")
        raise_frame(f_one_player)
        m = MatrixOfButtons(root,f_one_player,var.get())
    else:
        print("1 vs 1")
        raise_frame(f_two_players)
        m = MatrixOfButtons(root,f_two_players,var.get())

root = Tk()

f_start = Frame(root)
f_one_player = Frame(root)
f_two_players = Frame(root)

f_one_player.grid(row=0, column=0, sticky='news')
f_two_players.grid(row=0, column=0, sticky='news')
f_start.grid(row=0, column=0, sticky='news')

Label(f_start, text='Izaberite opciju:').pack()
var1 = IntVar()
P1 = Radiobutton(f_start, text="1 vs rac", variable=var1, value=1)
P1.pack()
P2 = Radiobutton(f_start, text="1 vs 1", variable=var1, value=2)
P2.pack()

Label(f_start, text='Koliko kartica zelite?').pack()

var = IntVar()
R1 = Radiobutton(f_start, text="4x4", variable=var, value=4, command=sel)
R1.pack()
R2 = Radiobutton(f_start, text="8x8", variable=var, value=8, command=sel)
R2.pack()
R3 = Radiobutton(f_start, text="16x16", variable=var, value=16, command=sel)
R3.pack()

raise_frame(f_start)
root.mainloop()
