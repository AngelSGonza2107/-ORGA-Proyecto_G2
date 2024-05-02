import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from Lienzo import PixelArtEditor
from Analizador import Analizador
import serial
import time


ser = serial.Serial('COM5', 9600)
time.sleep(2)  # Espera a que se establezca la conexión serial


#------------------------------------------------
def CodificarLista(Lista):
    Ram = []
    for i in Lista:
        # Forma
        if str(i.figura) == "triangulo":
            Datos = ['0','0']
            Ram.append(Datos)
        elif str(i.figura) == "x":
            Datos = ['0','1']
            Ram.append(Datos)
        elif str(i.figura) == "estrella":
            Datos = ['1','0']
            Ram.append(Datos)
        elif str(i.figura) == "o":
            Datos = ['1','0']
            Ram.append(Datos)

        # color
        if str(i.color) == "cyan":
            Datos = ['0','0']
            Ram.append(Datos)
        elif str(i.color) == "magenta":
            Datos = ['0','1']
            Ram.append(Datos)
        elif str(i.color) == "amarillo":
            Datos = ['1','0']
            Ram.append(Datos)
        elif str(i.color) == "negro":
            Datos = ['1','0']
            Ram.append(Datos)

        # coordenada x
        if str(i.x) == "0":
            Datos = ['0','0']
            Ram.append(Datos)
        elif str(i.x) == "1":
            Datos = ['0','1']
            Ram.append(Datos)
        elif str(i.x) == "2":
            Datos = ['1','0']
            Ram.append(Datos)

        # coordenada y
        if str(i.y) == "0":
            Datos = ['0','0']
            Ram.append(Datos)
        elif str(i.y) == "1":
            Datos = ['0','1']
            Ram.append(Datos)
        elif str(i.y) == "2":
            Datos = ['1','0']
            Ram.append(Datos)
        
    return Ram 

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.orga"), ("Todos los archivos", "*.*")])
    if archivo:
        with open(archivo, "r") as f:
            contenido = f.read()
        texto.delete("1.0", "end")
        texto.insert("1.0", contenido)  

def imprimir():
    contenido = texto.get("1.0", "end-1c")
    analizador = Analizador(contenido)
    listmovimiento = analizador.obtener_movimientos() # Lista con todos los movimientos posibles
    
    ListaCodificada = CodificarLista(listmovimiento)
    
    if analizador.obtener_contador_errores() == 0:
        for i in ListaCodificada:
            ser.write(i[0].encode())
            ser.write(i[1].encode())

            #ser.write(b""+str(listmovimiento[0].x)+"\n")
            #ser.write(b""+str(listmovimiento[0].y)+"\n")
            #ser.write(b""+str(listmovimiento[0].color)+"\n")
            #ser.write(b""+str(listmovimiento[0].figura)+"\n")
            
        ser.close()
        '''
            print(f"Set de impresión {i}:")
            print("X:", mov.x)
            print("y:", mov.y)
            print("color:", mov.color)
            print("Figura:", mov.figura)
        '''
    elif analizador.obtener_contador_errores() > 0:
        messagebox.showinfo("Hay errores en el archivo")
    
    print(analizador.obtener_contador_errores())
    


def nuevo_archivo():
    print("Nuevo archivo")

def guardar_como():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.orga")])
    if archivo:
        print("Guardar como:", archivo)

def guardar():
    print("Guardar archivo")

def salir():
    ventana.quit()

def documetacion():
    print("Documentacion")

ventana = tk.Tk()
ventana.title("Plotter Serial")

#menú principal
menu_principal = tk.Menu(ventana, tearoff=0, font=("Arial", 100))
ventana.config(menu=menu_principal)

#menú Archivo y ayuda
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir archivo", command=cargar_archivo)
menu_archivo.add_command(label="Nuevo archivo", command=nuevo_archivo)
menu_archivo.add_command(label="Guardar como", command=guardar_como)
menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_command(label="Imprimir", command=imprimir)
menu_archivo.add_command(label="Salir", command=salir)

menu_principal.add_command(label="Ayuda", command=documetacion)

#área de texto y carga de archivo
label1 = Label(ventana, text="Nombre impresion:", width=15, height=1)
label1.config(fg="#FFEBD2", bg="#273248",font=("Bahnschrift SemiBold", 14))
label1.place(x=20, y=20)

texto = tk.Text(ventana, width=60, height=40)
texto.place(x= 20, y=70) 

app = PixelArtEditor(ventana)

#text de figuras y colores
label2 = Label(ventana, text="FIGURAS", width=15, height=1)
label2.config(fg="#FFEBD2", bg="#273248",font=("Bahnschrift SemiBold", 20))
label2.place(x=660, y=45)

label3 = Label(ventana, text="COLORES", width=15, height=1)
label3.config(fg="#FFEBD2", bg="#273248",font=("Bahnschrift SemiBold", 20))
label3.place(x=1150, y=45)

ventana.config(bg="#273248")
#dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry("{}x{}+0+0".format(ancho_pantalla, alto_pantalla))
ventana.mainloop()