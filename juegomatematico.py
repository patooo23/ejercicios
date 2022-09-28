
from tkinter import  *



ventana = Tk()
# ventana2 = Tk()
# ventana3 = Tk()
ventana.title("adivina adivinador")
ventana.config(bg="violet", padx= 210, pady= 140)
ventana.geometry("800x500")
ventana.resizable(width= False, height= False)#fija el tamaño de la pantalla
variable = StringVar()
esMayor = StringVar()
opcion = IntVar()



def v2():

    def v3():

        def v4():

            def v5():

                    def v6():

                        def v7():
                                ventana6.withdraw()
                                ventana7 = Tk()
                                ventana7.config(bg="violet", padx= 210, pady= 140)
                                ventana7.geometry("800x500")
                                ventana7.resizable(width= False, height= False)

                                L1 = Label (ventana7, text="el numero que pensaste es...", font= "arial 15", background="violet",
                                foreground="black", width= 60, height=1)
                                L1.place(x= -170, y= 60)

                                e1 = Entry(ventana7, justify= "left",width=25, font= ("Stencil",14), textvariable= variable ,state="readonly")
                                e1.place(x=12, y=120)


                                B2 = Button(ventana7, text="presiona\n para verlo", background="white", foreground="black", width= 10, height=2,
                                font= "impact 15")
                                B2.place(x= 450, y= 70)

                                B3 = Button(ventana7, text="salir", background="white", foreground="black", width= 10, height=1,
                                font= "impact 15", command=ventana7.destroy)
                                B3.place(x= 105, y= 160)
#====================================================================================================================================================                                
                        ventana5.withdraw()
                        ventana6 = Tk()
                        ventana6.config(bg="violet", padx= 210, pady= 140)
                        ventana6.geometry("800x500")
                        ventana6.resizable(width= False, height= False)

                        L1 = Label (ventana6, text="Ahora, sumá las cifras del número\n que pensaste al principio y escribi el resultado", font= "arial 15", background="violet",
                        foreground="black", width= 60, height=3)
                        L1.place(x= -210, y= 60)

                        
                        e1 = Entry(ventana6, justify= "left",width=25, font= ("Stencil",14))
                        e1.place(x=-10, y=140)

                        B2 = Button(ventana6, text="siguiente", background="white", foreground="black", width= 10, height=1,
                        font= "impact 15", command= v7)
                        B2.place(x= 450, y= 70)
 #================================================================================================================
                    ventana4.withdraw()
                    ventana5 = Tk()
                    ventana5.config(bg="violet", padx= 210, pady= 140)
                    ventana5.geometry("800x500")
                    ventana5.resizable(width= False, height= False)

                    L1 = Label (ventana5, text="Entonces, restá el número invertido con el número original\n y escribi el resultado", font= "arial 15", background="violet",
                    foreground="black", width= 60, height=3)
                    L1.place(x= -210, y= 60)

                    e1 = Entry(ventana5, justify= "left",width=25, font= ("Stencil",14))
                    e1.place(x=-10, y=120)

                    B2 = Button(ventana5, text="siguiente", background="white", foreground="black", width= 10, height=1,
                    font= "impact 15", command= v6)
                    B2.place(x= 450, y= 90)
#==========================================================================================================================0
            
            ventana3.withdraw()
            ventana4 = Tk()
            ventana4.config(bg="violet", padx= 210, pady= 140)
            ventana4.geometry("800x500")
            ventana4.resizable(width= False, height= False)
            op = IntVar()
            def ValidaRb():
                operacion = op.get()
                if op == 3:
                    #aca metemos bandera por ej  esMayor = 1
                    esMayor = 1
                    return esMayor
                if op == 4:
                    esMayor =0
                    return esMayor
                    
                
                
            L1 = Label (ventana4, text="el nuevo n° es mayor o menor que el anterior?", font= "arial 15", background="violet",
            foreground="black", width= 40, height=1)
            L1.place(x= -62, y= 60)

            RB1 = Radiobutton(ventana4, text= "mayor", value= 3, variable= op, background="white", font= "arial 15",
            foreground="black", width= 10, height=1, command= ValidaRb)
            RB1.place(x= 0, y= 120)

            
            RB2 = Radiobutton(ventana4, text= "menor", value= 4, variable= op, background="white", font= "arial 15",
            foreground="black", width= 10, height=1, command=ValidaRb)
            RB2.place(x= 150, y= 120)

            B2 = Button(ventana4, text="siguiente", background="white", foreground="black", width= 10, height=1,
            font= "impact 15", command= v5)
            B2.place(x= 400, y= 70)

#==============================================================================================================================
        ventana2.withdraw()
        ventana3 = Tk()
        ventana3.config(bg="violet", padx= 210, pady= 140)
        ventana3.geometry("800x500")
        ventana3.resizable(width= False, height= False)

        L1 = Label (ventana3, text="ahora inverti el orden de las cifras,\n despues apreta en siguiente", font= "arial 15", background="violet",
        foreground="black", width= 35, height=3)
        L1.place(x= -62, y=
         60)

        
        B2 = Button(ventana3, text="siguiente", background="white", foreground="black", width= 10, height=1,
        font= "impact 15", command= v4)
        B2.place(x= 400, y= 70)
        
            
#=============================================================================================================================0

    op = opcion.get()
    if op == 1:
        ventana.withdraw()
        ventana2 = Tk()
        ventana2.config(bg="violet", padx= 210, pady= 140)
        ventana2.geometry("800x500")
        ventana2.resizable(width= False, height= False)

        L1 = Label (ventana2, text="pensá en un numero de 2 cifras que NO sean iguales,\n despues apreta en siguiente", font= "arial 15", background="violet",
        foreground="black", width= 45, height=3)
        L1.place(x= -120, y= 60)

        B1 = Button(ventana2, text="siguiente", background="white", foreground="black", width= 10, height=1,
        font= "impact 15", command= v3)
        B1.place(x= 400, y= 70)
#==============================================================================================================================
     


    

    
            



#=============================================================================================================================



idiomaa = Label (ventana, text="elige el idioma", font= "impact 30", background="black", foreground="white", width= 17, height=1)
idiomaa.grid(row=0, column=0,padx= 10, pady= 10)

espaniol= Radiobutton(ventana, text= "español", value= 1, variable= opcion, background="violet", font= "arial 15",
foreground="black", width= 17, height=1)
espaniol.grid(row=2, column=0,padx= 10, pady= 0)


ingles = Radiobutton(ventana, text= "ingles", value= 2, variable= opcion, background="violet", font= "arial 15",
foreground="black", width= 17, height=1)
ingles.grid(row=3, column=0, padx= 10, pady= 0)

boton1= Button(ventana, text="aceptar", background="white", foreground="black", width= 10, height=1, font= "impact 15",
command= v2)
boton1.grid(row=5, column= 0, pady= 10)





ventana.mainloop()


