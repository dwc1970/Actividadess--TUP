from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

operacion=""

#-------PANTALLA-------------------

numeroPantalla= StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#----------PULSACIONES DE TECLADO---------------------

def numeroPulsado(num):

    global operacion

    if operacion!="":

        numeroPantalla.set(num)

        operacion=""

    else:
        numeroPantalla.set(numeroPantalla.get() + num)

    numeroPantalla.set(numeroPantalla.get() + num)

    #---------- funcion suma ------
    def sumar():
        global operacion

        operacion="sumar"


#---------------------FILA 1 DE BOTONES  DE NUMEROS MAS OPERACION DE DIVIDIR--------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#----------------FILA 2  BOTONES DE NUNEROS MAS OPERADOR DE MULTIPLICAR------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)

#----------------FILA 3  BOTONES DE NUNEROS MAS OPERADOR DE RESTA------------

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=3)
botonResta=Button(miFrame, text="-", width=3)
botonResta.grid(row=4, column=4)

#----------------FILA 45 BOTONES DE NUNERO 0 MAS OPERADOR Y BOTON DE SUMAR------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3)
botonIgual.grid(row=5, column=3)
botonSumar=Button(miFrame, text="+", width=3, command=lambda:sumar())
botonSumar.grid(row=5, column=4)

# los numeos salen duplicados , hay que arreglar -- 
#enlace del cur#so de paython https://www.youtube.com/watch?v=LnO35TiFuQY
# Curso Python. Interfaces gráficas VIII. Vídeo 49



raiz.mainloop()