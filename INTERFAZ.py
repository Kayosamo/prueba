from tkinter import *

def mifuncion():
    print("Oprimio el boton")

ventana=Tk()
ventana.title("MI PRIMERA INTERFAZ")
ventana.geometry("400x200")


etiqueta1=Label(ventana,text="Esto es un ejemplo",fg="black",bg="yellow", font=("verdana",20))
etiqueta1.pack()

boton1=Button(ventana,text="Presione", command=mifuncion)
boton1.pack()

texto1=Entry(ventana, bg="pink")
texto1.place(x=145,y=70,width=100,height=30)

ventana.mainloop()