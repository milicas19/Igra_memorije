from tkinter import *
from tkinter import ttk
import os
import random

class MatrixOfButtons:
    #master je root
    def __init__(self,master,frame,n):
        self.b=[[0 for x in range(0,n)] for x in range(0,n)]
        matrica_slika=[[0 for x in range(0,n)] for x in range(0,n)]

        lista_slika=[1,2,3,4,5,6,7,8,9,10,11]#11 broj slika
        lista_parova=[]
        #formiramo listu parova        
        for i in range(0,n):
            for j in range(0,n):
                lista_parova.append((i,j))
                matrica_slika[i][j]=" " 

        while lista_parova!=[]:
            broj_slike=random.choice(lista_slika)
            lista_slika.remove(broj_slike)
            
            par=random.choice(lista_parova)
            lista_parova.remove(par)
            par1=random.choice(lista_parova)
            lista_parova.remove(par1)
        
            matrica_slika[par[0]][par[1]]="slike1\\"+str(broj_slike)+".gif"
            print (matrica_slika[par[0]][par[1]]+"\n")
            matrica_slika[par1[0]][par1[1]]="slike1\\"+str(broj_slike)+".gif"
            
        for i in range(0,n):
            for j in range(0,n):
                #print (matrica_slika[i][j]+"\n")
                path=os.path.join(matrica_slika[i][j])
                photo=PhotoImage(file=path)
                self.b[i][j] = Button(frame,image=photo,text = str(i)+''+str(j),command=lambda x1=i, y1=j: self.funkcija(x1,y1))
                self.b[i][j].image=photo
                self.b[i][j].grid(row = i,column = j)
                
    def funkcija(self,i,j):
        print (str(i))
        #OVO NE RADI, NISMO URADILI
        self.b[i][j].config(image=matrica_slika[i][j])


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
