from tkinter import *
import tkinter as tk
import os
import random

class MatrixOfButtons:
    #master je root
    def __init__(self,master,frame,n):
        self.b=[[0 for x in range(0,n)] for x in range(0,n)]
        self.frames=[[0 for x in range(0,n)] for x in range(0,n)]
        photo_matrix=[[0 for x in range(0,n)] for x in range(0,n)]

        photo_list=[1,2,3,4,5,6,7,8,9,10,11]#11 broj slika
        list_pair=[]
        #formiramo listu parova        
        for i in range(0,n):
            for j in range(0,n):
                list_pair.append((i,j))
                photo_matrix[i][j]=" " 

        while list_pair!=[]:
            broj_slike=random.choice(photo_list)
            photo_list.remove(broj_slike)
            
            pair=random.choice(list_pair)
            list_pair.remove(pair)
            pair1=random.choice(list_pair)
            list_pair.remove(pair1)
        
            photo_matrix[pair[0]][pair[1]]="slike1\\"+str(broj_slike)+".gif"
            photo_matrix[pair1[0]][pair1[1]]="slike1\\"+str(broj_slike)+".gif"
            
        for i in range(0,n):
            for j in range(0,n):
                path=os.path.join(photo_matrix[i][j])
                photo=PhotoImage(file=path)
                #da li stavljati u ove nove frejmove??
                self.frames[i][j]=Frame(frame)
                self.b[i][j] = Button(self.frames[i][j],image=photo,text = str(i)+''+str(j),command=lambda x1=i, y1=j: self.funkcija(x1,y1))
                self.b[i][j].image=photo
                self.frames[i][j].grid(row = i,column = j,sticky='nsew')
                self.b[i][j].pack(fill='both',anchor='center',expand=True)
                
    def funkcija(self,i,j):
        print (str(i))
        #OVO NE RADI, NISMO URADILI
        self.b[i][j].config(image=photo_matrix[i][j])


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
        self.f_start.grid(column=1, row=1)
        #cemu ovo sluzi??
        #self.f_start.columnconfigure(1, weight=1)
        #self.f_start.rowconfigure(1, weight=1)
       
        Label(self.f_start, text='Izaberite opciju:').grid(column = 1,row =1)    
        rb1=tk.Radiobutton(self.f_start, text="1 vs rac", variable=var1, value=1,indicatoron=0).grid(column = 1,row =2)
        rb2=tk.Radiobutton(self.f_start, text="1 vs 1", variable=var1, value=2,indicatoron=0).grid(column =2,row =2)
        

        Label(self.f_start, text='Izaberite kartice:').grid(column = 1,row =3)
        tk.Radiobutton(self.f_start,image = photo, text="opcija 1", variable=var2, value=1,indicatoron = 0).grid(column =1,row =4)
        tk.Radiobutton(self.f_start,image = photo2, text="opcija 2", variable=var2, value=2,indicatoron = 0).grid(column =2,row =4)
        tk.Radiobutton(self.f_start,image = photo3 ,text="opcija 3", variable=var2, value=3,indicatoron = 0).grid(column =3,row =4)

        Label(self.f_start, text='Koliko kartica zelite?').grid(column = 1,row =5)
        tk.Radiobutton(self.f_start, text="4x4", variable=var3, value=4,command = sel,indicatoron = 0).grid(column =1,row =6)
        tk.Radiobutton(self.f_start, text="8x8", variable=var3, value=8,command = sel,indicatoron = 0).grid(column =2,row =6)
        tk.Radiobutton(self.f_start, text="16x16", variable=var3, value=16,command = sel,indicatoron = 0).grid(column =3,row =6)
        
        raise_frame(self.f_start)


root = Tk()
root.title('Memory game')
root.geometry('800x600') # Size 200, 200

f_one_player = Frame(root)
f_two_players = Frame(root)

f_one_player.grid(row=1, column=1,sticky="nsew",padx=100,pady=100)
f_two_players.grid(row=1, column=1,sticky="nsew")
photo=PhotoImage(file='slike1/1.gif')
photo2 = PhotoImage(file ='slike1/2.gif')
photo3 = PhotoImage(file = 'slike1/3.gif')
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
MainGUI(root,photo,photo2,photo3,var1,var2,var3)
root.mainloop()
