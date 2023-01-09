from tkinter import *

def send_data():
    Nombre_data = Nombre.get()
    password_data =str(password.get()) 
    InicioEstacionamiento_data = InicioEstacionamiento.get()
    años_data = str(años.get())

    print(Nombre_data, "\t", password_data, "\t", InicioEstacionamiento_data, "\t", años_data, "\t")

    newfile = open("registratation.txt", "w")
    newfile.write(Nombre_data)
    newfile.write("\t")
    newfile.write(password_data)
    newfile.write("\t")
    newfile.write(InicioEstacionamiento_data)
    newfile.write("\t")
    newfile.write(años_data)
    newfile.write("\t")
    newfile.close()
    print("New user registered. Nombre: {} | InicioEstacionamiento: {} ".format(Nombre_data, InicioEstacionamiento_data))

    Nombre_entry.delete(0,END)
    password_entry.delete(0,END)
    InicioEstacionamiento_entry.delete(0,END)
    años_entry.delete(0,END)


mywindow = Tk()
mywindow.geometry("400x450")
mywindow.title("Formulario de Registro S.E.C")
mywindow.resizable(False, False)
mywindow.config(background="#213141")
main_title =Label(text="<No_Code/> Soluciones Informaticas", font=("Cambria", 13), bg="#0000FF", fg="white", width="550", height="2")
main_title.pack()

Nombre_label = Label(text="Nombre", bg="#FFEEDD")
Nombre_label.place(x=22, y=70)
password_label = Label(text="Contraseña", bg="#FFEEDD")
password_label.place(x=22, y=130)
InicioEstacionamiento_label = Label(text="Patente del Vehiculo", bg="#FFEEDD")
InicioEstacionamiento_label.place(x=22, y=190)
años_label = Label(text="Telefono", bg="#FFEEDD")
años_label.place(x=22, y=250)

Nombre = StringVar()
password = StringVar()
InicioEstacionamiento = StringVar()
años = StringVar()

Nombre_entry = Entry(textvariable=Nombre, width="40")
password_entry = Entry(textvariable=password, width="40", show="*")
InicioEstacionamiento_entry = Entry(textvariable=InicioEstacionamiento, width="40")
años_entry = Entry(textvariable=años, width="40")

Nombre_entry.place(x=22 , y=100)
password_entry.place(x=22, y=160)
InicioEstacionamiento_entry.place(x=22, y=220)
años_entry.place(x=22, y=280)

submit_btn = Button(mywindow, text="Enviar Formulario", command=send_data, width="30", height="2", bg="#00CD63")
submit_btn.place(x=22, y=320)

mywindow.mainloop()









