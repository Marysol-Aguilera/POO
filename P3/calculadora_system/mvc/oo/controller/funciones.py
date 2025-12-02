from tkinter import *
from tkinter import messagebox
from model import operaciones

class Controladores:
    @staticmethod
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
        resul=messagebox.askquestion(title= titulo, message=f"{numero1}{signo}{numero2}={resultado}\n ¿Quires guardar la operacion en la base de datos?",icon="question")
        if resul=="yes":
            respuesta=operaciones.Operaciones.insertar(numero1,numero2,signo,resultado)
            Controladores.respuesta_sql("Agregar Registro",respuesta)

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info", title=titulo, message="... ¡ Accion realizada con Éxito !...")

        else:
            messagebox.showinfo(icon="info", title=titulo, message="... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...")
    
    @staticmethod
    def eliminar(id):
        respuesta=operaciones.Operaciones.eliminar(id)
        Controladores.respuesta_sql("Borrar Registro",respuesta)

    @staticmethod
    def cambiar(n1,n2,sig,resul,id):
        respuesta=operaciones.Operaciones.actualizar(n1,n2,sig,resul,id)
        Controladores.respuesta_sql("Cambiar Registro",respuesta)

    @staticmethod
    def consultar():
        registros=operaciones.Operaciones.consultar()
        return registros
    
    @staticmethod
    def buscar(id):
        respuesta=operaciones.Operaciones.buscar(id)
        if respuesta:
            messagebox.showinfo(icon="info",message="hay registro ")

        else:
                        messagebox.showinfo(icon="info",  message="noo")

    
    


