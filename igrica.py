from tkinter import *
from tkinter import ttk
import os
import random

class MatrixOfButtons:
    #master je root
    def __init__(self,master,frame,n):
        k = random.randint(1,3)
        path = os.path.join('slike1',str(k)+".gif")
        photo=PhotoImage(file=path)
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
        m = MatrixOfButtons(root,f_one_player,var3.get())
    else:
        print("1 vs 1")
        raise_frame(f_two_players)
        m = MatrixOfButtons(root,f_two_players,var3.get())



class MainGUI:

    def __init__(self, master,photo1,photo2,photo3,var1,var2,var3):
        self.f_start = Frame(master)
        self.f_start.grid(column=0, row=0, sticky=(N, W, E, S))
        self.f_start.columnconfigure(0, weight=1)
        self.f_start.rowconfigure(0, weight=1)
        

       
        Label(self.f_start, text='Izaberite opciju:').grid(column = 1,row =1)
        
        ttk.Radiobutton(self.f_start, text="1 vs rac", variable=var1, value=1).grid(column = 1,row =2)
        ttk.Radiobutton(self.f_start, text="1 vs 1", variable=var1, value=2).grid(column =2,row =2)


        Label(self.f_start, text='Izaberite kartice:').grid(column = 1,row =3)
      
        ttk.Radiobutton(self.f_start,image = photo, text="opcija 1", variable=var2, value=1).grid(column =1,row =4)
        ttk.Radiobutton(self.f_start,image = photo2, text="opcija 2", variable=var2, value=2).grid(column =2,row =4)
        ttk.Radiobutton(self.f_start,image = photo3 ,text="opcija 3", variable=var2, value=3).grid(column =3,row =4)

        Label(self.f_start, text='Koliko kartica zelite?').grid(column = 1,row =5)
     
        ttk.Radiobutton(self.f_start, text="4x4", variable=var3, value=4,command = sel).grid(column =1,row =6)
        ttk.Radiobutton(self.f_start, text="8x8", variable=var3, value=8,command = sel).grid(column =2,row =6)
        ttk.Radiobutton(self.f_start, text="16x16", variable=var3, value=16,command = sel).grid(column =3,row =6)
        
        raise_frame(self.f_start)


root = Tk()
f_one_player = Frame(root)
f_two_players = Frame(root)

f_one_player.grid(row=0, column=0, sticky='news')
f_two_players.grid(row=0, column=0, sticky='news')
photo=PhotoImage(file='slike1/1.gif')
photo2 = PhotoImage(file ='slike1/2.gif')
photo3 = PhotoImage(file = 'slike1/3.gif')
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
MainGUI(root,photo,photo2,photo3,var1,var2,var3)
root.mainloop()