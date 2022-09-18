from cProfile import label
import math
from tkinter import *
import tkinter as tk
from tkinter import ttk


ventana = Tk()
ventana.title("Factorial")
ventana.config(bg="black", padx=200, pady= 50)

def calcular():
    calc = int(pantalla.get())+1
    resultado.config(text=math.factorial(calc))
    for i in range(calc):
        entryy.set(calc)

    
entryy= IntVar(value=0)

NombreN = Label (ventana, text="n", font= "arial 9", background="black", foreground="white")
NombreN.grid(row=0, column=0,padx= 10)


pantalla = Entry (ventana, bg= "white", justify="center", state= "readonly", text= entryy)
pantalla.grid (row= 0, column= 1, padx= 10)


Nombrefact = Label (ventana, text="Factorial(n)", font= "arial 9", background="black", foreground="white")
Nombrefact.grid(row=0, column=2,padx= 10)


resultado = Label (ventana, text="", font= "arial 9", background="white", foreground="black", width= 10, height=1)
resultado.grid(row=0, column=3, padx= 10)


boton= Button(ventana, text="siguiente", width= 10, height=1, command=calcular) 
boton.grid(row=0, column= 4, padx= 10)




ventana.mainloop()