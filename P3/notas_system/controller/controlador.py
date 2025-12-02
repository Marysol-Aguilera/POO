
from tkinter import messagebox
from model import usuario, nota
from view import vista



class Controlador:
    @staticmethod
    def registrar(nombre, apellidos, email, password):
        resultado=usuario.Usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registro correctamente, con el email:{email}")

        else:
            messagebox.showinfo(icon="info",message=f"Por favor intentelo de nuevo, no fue posible insertar el registro")

    @staticmethod
    def login(email, password,ventana):
        registro=usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(icon="info",message=f"{registro[1]} {registro[2]}, se registro correctamente") 
            vista.View.menu_notas(ventana,registro[0],registro[1],registro[2])

        else:
            messagebox.showinfo(icon="info",message=f"Credenciales incorrectas vuelva a intentarlo, por favor ")
        
    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear Notas", respuesta)

    @staticmethod
    def mostrar_nota(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros

    @staticmethod
    def eliminar_nota(id):
        respuesta=nota.Nota.eliminar(id)
        Controlador.respuesta_sql("Borrar Notas", respuesta)

    @staticmethod
    def modificar_nota(id, titulo, descripcion):
        respuesta=nota.Nota.actualizar(id ,titulo,descripcion)
        Controlador.respuesta_sql("Modificar Notas", respuesta)

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info", title=titulo, message="... ¡ Accion realizada con Éxito !...")

        else:
            messagebox.showinfo(icon="info", title=titulo, message="... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...")
    
