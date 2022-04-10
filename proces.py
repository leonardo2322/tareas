import subprocess

# comand = subprocess.run('cat leo.txt | grep -n "como"',capture_output=True,text=True,shell=True)

""" with open(cl,'w')as f:
    echo = subprocess.run(['echo','hola como estas'],stdout=f,text=True)
 """

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
import sqlite3
window = Tk()
conexion = sqlite3.connect("base_datos_inventario")


def gui(window, conexion):
    win = window
    win.geometry('450x100')
    frma = Frame()
    frma.grid()
    lista = []
    ent1 = IntVar()
    ent2 = StringVar()
    ent3 = IntVar()
    ent4 = IntVar()
    conex = conexion
    """ LABELS DESCRIPTIVOS """
    lbl = Label(frma, text='cant')
    lbl.grid(row=0, column=0, padx=5, pady=5)

    input1 = Entry(frma, width=10, textvariable=ent1)
    input1.grid(row=1, column=0, padx=5, pady=5)

    # fila uno----------------------

    lbl1 = Label(frma, text='especificacion')
    lbl1.grid(row=0, column=1, padx=5, pady=5)

    input2 = Entry(frma, width=20, textvariable=ent2)
    input2.grid(column=1, row=1)

    # fila 2---------------------------
    lbl2 = Label(frma, text='costo')
    lbl2.grid(row=0, column=2, padx=5, pady=5)

    input4 = Entry(frma, width=10, textvariable=ent3)
    input4.grid(row=1, column=2, padx=5, pady=5)

    # finish row 3----------------------

    # fila 4---------------------------
    lbl3 = Label(frma, text='total valor')
    lbl3.grid(row=0, column=3, padx=5, pady=5)

    input3 = Entry(frma, width=10, textvariable=ent4)
    input3.grid(row=1, column=3, padx=5, pady=5)
    botones(win, frma, ent1, ent2, ent3, ent4, conex, lista)
    guardar(ent1, ent2, ent3, ent4, conex, lista)
    limpiar(ent1, ent2, ent3, ent4)


def limpiar(e1, e2, e3, e4):
    en1 = e1
    en2 = e2
    en3 = e3
    en4 = e4
    en1.set("")
    en2.set("")
    en3.set("")
    en4.set("")


def calcular():
    pass


def guardar(e1, e2, e3, e4, base, lista):
    base1 = base
    listado = lista
    ent1 = e1
    ent2 = e2
    ent3 = e3
    ent4 = e4
    print(ent1)
    print(listado)
    # try:
    object1 = ent1.get()
    print(object1)
    object2 = ent2.get()
    object3 = ent3.get()
    object4 = ent4.get()

    if ent1 and ent2 and ent3 and ent4:
        listado.append(object1)
        listado.append(object2)
        listado.append(object3)
        listado.append(object4)

    else:
        mb.showerror("Error", "No Rellenaste todos los campos")

    # except:
        # mb.showerror("Error", "Rellena el campo con un entero")


def botones(win1, frame, e1, e2, e3, e4, conex, lista):
    fram = frame
    win5 = win1
    base = conex
    array = lista
    btn = Button(fram, text="Guardar", command=lambda: guardar(
        e1, e2, e3, e4, base, array))
    btn2 = Button(fram, text="limpiar",
                  command=lambda: limpiar(e1, e2, e3, e4))
    btn2.grid(column=1, row=5)
    btn.grid(column=0, row=5)


def basedata(cone, lista):
    conect = cone
    listado = lista
    try:
        conect.cursor()
        conect.execute("""
                CREATE TABLE ADMINISTRACION(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CANT INTEGER(30),
                ESPECIFICACION VARCHAR(70),
                COSTO INTEGER(30),
                TOTAL INTEGER(30))""")
        conect.close()
        mb.showinfo("base de dato", "creada cone exito")
    except sqlite3.OperationalError:
        mb.showinfo("ALGO", "RESULTO MAL")
    except sqlite3.ProgrammingError:
        con(conect, listado)

    conect.commit()
    conect.close()


def con(cone, lista):
    estlist = lista
    miconexion = sqlite3.connect("base_datos_inventario")
    cursor = miconexion.cursor()
    print(estlist)
    try:
        cursor.execute(
            """INSERT INTO ADMINISTACION VALUES(?,?,?,?)""", estlist)
        miconexion.commit()
        miconexion.close()
    except:
        print("no hay datos")


if __name__ == "__main__":
    api = gui(window, conexion)
    basedata(conexion, list)
    window.mainloop()