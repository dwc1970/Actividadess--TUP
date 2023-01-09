from tkinter import *

root=Tk()

root.title = "Dario Walter Carrizo"
root.iconbitmap("Dario.ico")
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="Dario.gif")

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()