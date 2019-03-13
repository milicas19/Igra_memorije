from Tkinter import *

def raise_frame(frame):
    frame.tkraise()

root = Tk()

f_pocetni = Frame(root)
f_jedan_igrac = Frame(root)
f_dva_igraca = Frame(root)

f_jedan_igrac.grid(row=0, column=0, sticky='news')
f_dva_igraca.grid(row=0, column=0, sticky='news')
f_pocetni.grid(row=0, column=0, sticky='news')

Button(f_pocetni, text='Jedan igrac', command=lambda:raise_frame(f_jedan_igrac)).pack()
Button(f_pocetni, text='Dva igraca', command=lambda:raise_frame(f_dva_igraca)).pack()
Label(f_pocetni, text='Koliko kartica zelite?').pack()

label=Label(f_jedan_igrac)
label.pack()

def sel():
   selection = "You selected the option " + str(var.get())
   i=0
   j=0
   for i in range(0,var.get()):
      for j in range(0,var.get()):
         Button(f_jedan_igrac, text=str(i)+" "+str(j)).pack()
   label.config(text = selection)

   
def sel3():
   selection = "You selected the option " + str(var.get())
   Button(f_jedan_igrac, text='3').pack()
   Button(f_jedan_igrac, text='4').pack()
   label.config(text = selection)


var = IntVar()
R1 = Radiobutton(f_pocetni, text="4x4", variable=var, value=4, command=sel)
R1.pack()
R2 = Radiobutton(f_pocetni, text="8x8", variable=var, value=8, command=sel)
R2.pack()
R3 = Radiobutton(f_pocetni, text="16x16", variable=var, value=16, command=sel3)
R3.pack()

raise_frame(f_pocetni)
root.mainloop()

