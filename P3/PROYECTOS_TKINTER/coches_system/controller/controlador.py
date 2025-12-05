from tkinter import messagebox
from model import cochesBD

class Controlador:

    @staticmethod
    def insertar_autos(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            auto = cochesBD.Autos(marca, color, modelo, velocidad, caballaje, plazas)
            respuesta = auto.insertar()
            Controlador.respuesta_sql("Crear Auto", respuesta)
        except Exception as e:
            Controlador.respuesta_sql("Crear Auto", False)


    @staticmethod
    def consultar_autos():
        # Autos.consultar() es un método estático y no toma argumentos
        registros = cochesBD.Autos.consultar()
        return registros

    @staticmethod
    def eliminar_autos(id):
        respuesta = cochesBD.Autos.eliminar(id)
        Controlador.respuesta_sql("Borrar Auto", respuesta)

    @staticmethod
    def actualizar_autos(id, marca, color, modelo, velocidad, caballaje, plazas):
        respuesta = cochesBD.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas, id)
        Controlador.respuesta_sql("Modificar Auto", respuesta)


