"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 Botones para las operaciones 
3.- Mostrar el resultado en una alerta
4.- Programacion Estructurada
5.- Implementar el MVC
"""

from view import interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        view=interfaz.Vistas(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
