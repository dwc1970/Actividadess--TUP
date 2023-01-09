from  tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=2, column=0)



raiz.mainloop()
