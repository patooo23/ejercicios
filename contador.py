
from tkinter import *
from turtle import right


ventana = Tk()
ventana.title("Contador")
ventana.config(bg="black", padx=200, pady= 50)

def count_up():
    valor = int(numero["text"])
    numero["text"] = f"{valor +1}"

def count_down():
    valor = int(numero["text"])
    numero["text"] = f"{valor -1}"

def reset():
    valor = int(numero["text"])
    numero["text"] = f"{valor - valor}"


NombreN = Label (ventana, text="Contador", font= "arial 9", background="black", foreground="white")
NombreN.grid(row=0, column=0,padx= 10)


numero = Label(ventana, text="0")
numero.config(bg= "white", padx= 10, pady= 0, width= 10, height=1)
numero.grid(row= 0, column=1, padx= 10)

boton1= Button(ventana, text="count up", width= 8, height=1, command= count_up)
boton1.grid(row=0, column= 2, padx= 10)

boton2= Button(ventana, text="count down", width= 8, height=1, command= count_down)
boton2.grid(row=0, column= 3, padx= 10)

boton3= Button(ventana, text="reset", width= 8, height=1, command= reset)
boton3.grid(row=0, column= 4, padx= 10)



ventana.mainloop()