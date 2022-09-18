from cProfile import label
from cgitb import text
from distutils.cmd import Command
from logging import root
from tkinter import *
import tkinter as tk
from tkinter import ttk

def disminuir():
    valor = int(numero["text"])
    numero["text"] = f"{valor - 1}"
    
    

ventana = Tk()
ventana.title("contador decreciente")
ventana.config(bg="black", padx=80, pady= 150)


Nombre = Label (ventana, text="Contador", font= "arial 9", background="black", foreground="white")
Nombre.grid(row=0, column=0)


numero = Label(ventana, text="88")
numero.config(bg= "white", padx= 100, pady= 0)
numero.grid(row= 0, column=1, padx= 10)


boton1= Button(ventana, text="-", width= 4, height=1, command= disminuir)
boton1.grid(row=0, column= 2)


ventana.mainloop()