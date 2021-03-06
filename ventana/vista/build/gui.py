
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# https://docs.python.org/3/library/tkinter.html

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import psycopg2 as pg

ubicacion = ""

registros = []

registro = [0,"","",""]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("512x243")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 243,
    width = 512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



def insertar_en_bbdd():
    
    try:
        connection = pg.connect("host=localhost dbname=python_test user=postgres password=amigous")
    except:
        print("Unable to connect")
        
    with open(ubicacion) as fichero:
        for linea in fichero:
            registro[0] = int(linea[:5])
            registro[1] = str(linea[5:29])
            registro[2] = str(linea[29:85])
            registro[3] = str(linea[85:94])
            # tengo que declarar estas variables porque no me deja usar los indices de registro, por problemas de set
            #! Investigar creacion de objetos de tipo cliente, DAO no existe en Python...
            
            id_cliente = registro[0]
            nombre_cliente = registro[1]
            direccion_cliente = registro[2]
            telefono_cliente = registro[3]
            
            registros.append(registro)
            
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO cliente (id_cliente, nombre, direccion, telefono) VALUES (%s, %s, %s, %s);", (id_cliente,nombre_cliente,direccion_cliente,telefono_cliente))
            cursor.close()
            connection.commit()
    connection.close()
    print("Incorporacion Completada")
    print(registros)


canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertar_en_bbdd(),
    relief="flat"
)

button_1.place(
    x=32.0,
    y=184.0,
    width=443.0,
    height=42.0
)
# https://pythonspot.com/tk-file-dialogs/

def seleccionar_fichero():
    # para modificar el valor de una global dentro de una funcion, se usa la keyword global dentro de la funcion
    global ubicacion
    ubicacion = filedialog.askopenfilename()
    # Eliminamos texto, si lo hubiera
    ubicacion_fichero.delete(0)
    # Le metemos el texto nuevo
    ubicacion_fichero.insert(0, ubicacion)
    

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_seleccion_fichero = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: seleccionar_fichero(),
    relief="flat"
)
button_seleccion_fichero.place(
    x=427.0,
    y=97.0,
    width=48.0,
    height=48.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    213.5,
    121.0,
    image=entry_image_1
)
ubicacion_fichero = Entry(
    bd=0,
    bg="#F2F2F2",
    highlightthickness=0,
    font = "Helvetica 14 bold",
    justify="center"
)
ubicacion_fichero.place(
    x=37.0,
    y=97.0,
    width=353.0,
    height=46.0
)

canvas.create_text(
    143.0,
    13.0,
    anchor="nw",
    text="Incorporar Clientes",
    fill="#848080",
    font=("Varela", 24 * -1)
)

canvas.create_text(
    32.0,
    75.0,
    anchor="nw",
    text="ubicacion del fichero",
    fill="#848080",
    font=("Varela", 14 * -1)
)


window.resizable(False, False)
window.mainloop()
