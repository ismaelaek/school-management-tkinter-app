from tkinter import *
from tkinter import ttk,messagebox
from Classes import *
from Functions import *
from datetime import *
from InterfaceFuncs import *

fen=Tk()
fen.title("Gestion De Scolarité")
x=(fen.winfo_screenwidth()-800)/2
y=(fen.winfo_screenheight()-600)/2
fen.geometry('%dx%d+%d+%d'%(800,600,x,y))
LabTitre    =Label(fen,text="Gestion de scolarité", font="Times 24 bold italic", fg="blue", bg="#FCFCFC", width=100)
LabTitre.pack(padx=0,pady=0)

MenuPrincipale(fen)

fen.mainloop()

