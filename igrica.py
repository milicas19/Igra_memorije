from tkinter import *
import tkinter as tk
from tkinter import ttk # treba nam za lepsi izgled, trenutno koristimo samo kod *** da bi dugmici uvek bili iste velicine pri promeni igraca(PLAVI ZUTI)
import os #**
import random
import time
from tkinter.font import Font
from pathlib import Path #treba nam za putanje za ucitavanje slika, kao i **

#globalne promenljive
count=0
pom_i=-1
pom_j=-1
player = 1 #redni broj igraca 
points_b = 0 #poeni PLAVOG igraca
points_y = 0 #poeni ZUTOG igraca
nonmatched = [] #lista kartica koje nisu match-ovane ili osvojene
#sledeca dva para koristimo kod 1 vs rac
pair1 = (-1,-1) 
pair2 = (-1,-1)
done = 0

class MatrixOfButtons:
    #master je root
    def __init__(self,master,frame,n,f_end,var1):
        #self=root a frame=f_one_player
        #valjda je master root?

        #formiramo listu nonmatched:
        global nonmatched
        for i in range(0,n):
            for j in range(0,n):
                nonmatched.append((i,j)) 

        self.b=[[0 for x in range(0,n)] for x in range(0,n)] #matrica dugmica
        #****
        self.lbl = tk.Label(frame,text="Igra ZUTI igrac") #prvi na potezu je ZUTI igrac
        self.points_yellow = tk.Label(frame,text = "0") #labela za bodove ZUTOG igraca
        self.points_blue = tk.Label(frame,text = "0") #labela za bodove PLAVOG igraca

        photo_matrix=[[0 for x in range(0,n)] for x in range(0,n)] #matrica slika

        photo_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] #broj slika
        list_pair=[] #lista parova=koordinate u matrici (i,j)
        
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

            #na poziciji (i,j) cuvamo naziv slike
            path = os.path.join(Path().absolute(),"slike3/"+str(broj_slike)+".gif")
            photo_matrix[pair[0]][pair[1]]=path
            photo_matrix[pair1[0]][pair1[1]]=path
            
        for i in range(0,n):
            for j in range(0,n):
                path = os.path.join(Path().absolute(),"slike3/blank.gif")
                photo=PhotoImage(file=path)#slika kartica
                self.b[i][j] = ttk.Button(frame,image=photo,command=lambda x1=i, y1=j,n=n,matrica=photo_matrix,frame=frame,card_photo=photo,f_end=f_end,var1=var1: self.funkcija(x1,y1,n,matrica,frame,card_photo,f_end,var1)) #***
                self.b[i][j].image=photo #*
                self.b[i][j].grid(row = i,column = j,sticky='nsew')  
        #stavljamo na frame labele koje smo gore definisali ****
        self.lbl.grid(row = (n+3),column = 0,sticky='nsew')
        self.points_yellow.grid(row = (n+4),column = 0,sticky='nsew')
        self.points_blue.grid(row = (n+5),column = 0,sticky='nsew')
        
                   
    def funkcija(self,i,j,n,photo_matrix,frame,card_photo,f_end,var1):
        global pom_i,pom_j
        global player
        global points_b,points_y
        global nonmatched
        global done
        pathf = os.path.join(Path().absolute(),"slike3/zuti.gif")
        paths = os.path.join(Path().absolute(),"slike3/plavi.gif")
        photo_first = PhotoImage(file=pathf)
        photo_second = PhotoImage(file=paths)

        def open_card(self,i,j,photo_matrix): #prikazuje sta se nalazi na kartici
            photo=PhotoImage(file=photo_matrix[i][j])
            self.b[i][j].config(image=photo)
            #moramo ponovo da postavimo sliku zbog sakupljaca otpadaka, jer ga on pokupi u suprotnom*
            self.b[i][j].image=photo

        def open_random_cards(self,photo_matrix): #prikazuje random izabrane kartice (2 kartice)
            global nonmatched
            global pair1,pair2
            
            #biramo 2 para iz liste neosvojenih(=nonmatched) kartica
            pair1 = random.choice(nonmatched)
            (i1,j1) = pair1
            open_card(self,i1,j1,photo_matrix)
            nonmatched.remove(pair1) #sklonili smo ovaj pair1 da bi nam pair2 bio razliciti od pair1, posle cemo ga vratiti

            pair2 = random.choice(nonmatched)
            (i2,j2) = pair2
            frame.after(500, lambda: open_card(self,i2,j2,photo_matrix))
            nonmatched.append(pair1) #vracamo pair1 u nonmatched listu
    

        def change(photo,i,j):
            global pom_i,pom_j
            self.b[i][j].config(image=photo)
            self.b[i][j].image=photo
            self.b[pom_i][pom_j].config(image=photo)
            self.b[pom_i][pom_j].image=photo
            pom_i = -1
            pom_j = -1
            # vracamo pom_i i pom_j na -1 da nam ne bi doslo do greske pri neparnim koracima
        def change_random_cards(photo,pair1,pair2) :
            (i1,j1) = pair1
            (i2,j2) = pair2
            self.b[i1][j1].config(image=photo)
            self.b[i1][j1].image=photo
            self.b[i2][j2].config(image=photo)
            self.b[i2][j2].image=photo
        def change_of_player(self,boja):
            self.lbl.configure(text= "Igra " + boja + " igrac!")

        def computer_playing(self,frame,photo_matrix,photo_second,card_photo):
            global nonmatched
            global player
            global points_b
            global pair1,pair2
            global done #sluzi nam da ne ispisemo 2x ko je pobednik na f_end
            if len(nonmatched) is 0 : 
                frame.after(1200,lambda : winner(points_b,points_y))
                done = 1
                return False
            open_random_cards(self,photo_matrix)
            (i1,j1) = pair1
            (i2,j2) = pair2
            if photo_matrix[i1][j1]==photo_matrix[i2][j2]:
                nonmatched.remove(pair1)
                nonmatched.remove(pair2)
                points_b += 1
                self.points_blue.configure(text = str(points_b))
                frame.after(800,lambda: change_random_cards(photo_second,pair1,pair2))
                frame.after(1200,lambda: computer_playing(self,frame,photo_matrix,photo_second,card_photo))
            else:
                player = 1
                frame.after(800, lambda: change_random_cards(card_photo,pair1,pair2))
                
                frame.after(700, lambda: change_of_player(self,"ZUTI"))

        def winner(points_b,points_y):
            myFont = Font(family="Segoe Print", size=14)
            if points_y > points_b: 
                lbly = tk.Label(f_end,text="Pobednik je ZUTI!",font=myFont)
                lbly.pack()
            elif points_y < points_b:
                lblb = tk.Label(f_end,text="Pobednik je PLAVI!",font=myFont)
                lblb.pack()
            else:
                lble = tk.Label(f_end,text="Nereseno je!",font=myFont)
                lble.pack()
            raise_frame(f_end)

        # zapravo program, posle gomile fja :D
        if (pom_i!=i or pom_j!=j) and ((i,j) in nonmatched): #da ne bi nastao problem ako neko klikne dva puta na isto dugme i ne mozemo ponovo otvarati osvojene kartice
        
            global count
            count += 1
        
            open_card(self,i,j,photo_matrix)
         
            #proveravamo da li su otvorene 2 kartice, ako jesu radimo sledece:
            if count % 2 == 0:
                if photo_matrix[i][j]==photo_matrix[pom_i][pom_j]:
                    if player == 1:
                        nonmatched.remove((i,j))
                        nonmatched.remove((pom_i,pom_j))
                        points_y += 1
                        self.points_yellow.configure(text = str(points_y))
                        frame.after(700, lambda: change(photo_first,i,j))
                    else:
                        nonmatched.remove((i,j))
                        nonmatched.remove((pom_i,pom_j))
                        points_b += 1
                        self.points_blue.configure(text = str(points_b))
                        frame.after(700, lambda: change(photo_second,i,j))
                #sklanjaju se slike
                else:
                    frame.after(700, lambda: change(card_photo,i,j))
                    if player == 1:
                        player = 2
                        frame.after(700, lambda: change_of_player(self,"PLAVI"))
                        
                        if var1 ==1: # u ovo ulazi samo ako smo uzeli opciju 1 vs rac
                            frame.after(750, lambda: computer_playing(self,frame,photo_matrix,photo_second,card_photo))

                    else:
                        player = 1
                        frame.after(500, lambda: change_of_player(self,"ZUTI"))
            # ako nisu, to znaci da imamo jednu otvorenu i zelimo da zapamtimo njenu poziciju
            else:
                pom_i=i
                pom_j=j  

        
        if points_b + points_y == n*n/2 and done ==0: #ako je done=1 onda smo presli na f_end u fji computer_playing
            frame.after(1200,lambda : winner(points_b,points_y))
        
        
def raise_frame(frame):
    frame.tkraise()

def sel(f_start):
    
    if var1.get()==1:
        print("1 vs rac")
        f_start.destroy()
        raise_frame(f_one_player)
        m = MatrixOfButtons(root,f_one_player,var3.get(),f_end,var1.get())
    else:
        print("1 vs 1")
        raise_frame(f_two_players)
        m = MatrixOfButtons(root,f_two_players,var3.get(),f_end,var1.get())

class MainGUI:

    def __init__(self, master,photo1,photo2,photo3,var1,var2,var3):
        self.f_start = Frame(master)
        self.f_start.grid(column=1, row=1)
        #cemu ovo sluzi??
        self.f_start.columnconfigure(1, weight=1)
        self.f_start.rowconfigure(1, weight=1)
        myFont = Font(family="Segoe Print", size=14)
        tk.Label(self.f_start, text='Izaberite opciju:', font=myFont).grid(column = 1,row =1)    
        tk.Radiobutton(self.f_start, text="1 vs rac", variable=var1, value=1,indicatoron=0).grid(column = 1,row =2)
        tk.Radiobutton(self.f_start, text="1 vs 1", variable=var1, value=2,indicatoron=0).grid(column =2,row =2)
        
        tk.Label(self.f_start, text='Izaberite kartice:',font=myFont).grid(column = 1,row =3)
        tk.Radiobutton(self.f_start,image = photo1, text="opcija 1", variable=var2, value=1,indicatoron = 0).grid(column =1,row =4)
        tk.Radiobutton(self.f_start,image = photo2, text="opcija 2", variable=var2, value=2,indicatoron = 0).grid(column =2,row =4)
        tk.Radiobutton(self.f_start,image = photo3 ,text="opcija 3", variable=var2, value=3,indicatoron = 0).grid(column =3,row =4)

        tk.Label(self.f_start, text='Koliko kartica zelite?',font=myFont).grid(column = 1,row =5)
        #prosledjujemo pocetni frejm (f_start)
        tk.Radiobutton(self.f_start, text="4x4", variable=var3, value=4,command=lambda frame=self.f_start: sel(frame),indicatoron = 0).grid(column =1,row =6)
        tk.Radiobutton(self.f_start, text="8x8", variable=var3, value=8,command=lambda frame=self.f_start: sel(frame),indicatoron = 0).grid(column =2,row =6)
        tk.Radiobutton(self.f_start, text="16x16", variable=var3, value=16,command=lambda frame=self.f_start: sel(frame),indicatoron = 0).grid(column =3,row =6)
        
        raise_frame(self.f_start)

root = Tk()
root.title('Memory game')
#root.geometry('800x600') # Size 200, 200

f_one_player = Frame(root)
f_two_players = Frame(root)
f_end = Frame(root)

f_one_player.grid(row=1, column=1,sticky="nsew",padx=20,pady=20)
f_two_players.grid(row=1, column=1,sticky="nsew",padx=20,pady=20)
f_end.grid(row=1, column=1,sticky="nsew",padx=20,pady=20)
path1 = os.path.join(Path().absolute(),"slike3/1.gif")
path2= os.path.join(Path().absolute(),"slike3/2.gif")
path3 = os.path.join(Path().absolute(),"slike3/3.gif")
photo=PhotoImage(file=path1)
photo2 = PhotoImage(file =path2)
photo3 = PhotoImage(file = path3)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
MainGUI(root,photo,photo2,photo3,var1,var2,var3)
root.mainloop()
