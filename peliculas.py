from cgitb import text
from tkinter import * 


ventana = Tk()
ventana.title("Peliculas")
ventana.config(bg="black", padx=100, pady= 40)
#añadir funcion delete



def añadir():
    lista.insert(END,listaPelis.get())
    borrar()
    
def borrar():
    listaPelis.set("")
    



listaPelis = StringVar()


NombreN = Label (ventana, text="Escribe el titulo de una pelicula", font= "arial 9", background="black", foreground="white")
NombreN.grid(row=1, column=0)

pantalla = Entry (ventana, textvariable= listaPelis, bg= "white", justify="center", width= 50)
pantalla.grid (row= 2, column= 0)

boton1= Button(ventana, text="añadir", width= 8, height=1, command= añadir)
boton1.grid(row=3, column= 0)


NombreP = Label (ventana, text="PELICULAS", font= "arial 9", background="black", foreground="white")
NombreP.grid(row=1, column=2,padx= 10, pady= 15)


lista = Listbox (ventana, font= "arial 9", width= 30, height=9)
lista.grid(row=2, column=2,padx= 50, pady= 0)





ventana.mainloop()