from tkinter import *
from controller import controlador
#from model import operaciones
from tkinter import messagebox

#interfaz o view
class View:
    def __init__(self,ventana):
        ventana.title("Gestion de notas")
        ventana.geometry("1024x768")
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text= ".:: Menu principal ::.", justify="center")
        lbl_titulo.pack(pady=10)

        btn_registro=Button(ventana,text="1.- Registro",justify="center",command=lambda: View.registro(ventana))
        btn_registro.pack(pady=10)

        btn_login=Button(ventana,text="2.- Login", justify="center",command=lambda: View.login(ventana))
        btn_login.pack(pady=10)

        btn_salir=Button(ventana, text="3.- Salir", justify="center" ,command=lambda: ventana.quit())
        btn_salir.pack(pady=10)

    @staticmethod
    def registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text= ".:: Registro ::.", justify="center")
        lbl_titulo.pack(pady=10)

        lbl_nombre=Label(ventana,text="Cual es tu nombre?",justify="center")
        lbl_nombre.pack(pady=10)

        txt_nombre=Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=10)

        lbl_apellidos=Label(ventana,text="Cuales son tus apellidos?",justify="center")
        lbl_apellidos.pack(pady=10)

        txt_apellidos=Entry(ventana)
        txt_apellidos.pack(pady=10)

        lbl_email=Label(ventana,text="Ingresa tu email ",justify="center")
        lbl_email.pack(pady=10)

        txt_email=Entry(ventana)
        txt_email.pack(pady=10)

        lbl_password=Label(ventana,text="Ingresa tu password ",justify="center")
        lbl_password.pack(pady=10)

        txt_password=Entry(ventana,show="*")
        txt_password.pack(pady=10)

        btn_registrar=Button(ventana,text="Registrar ", justify="center",command=lambda:{controlador.Controlador.registrar(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_password.get()), View.login(ventana)})
        btn_registrar.pack(pady=10)

        btn_regresar=Button(ventana, text="Volver", justify="center" ,command=lambda: View.menu_principal(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def login(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text= ".:: Registro en el sistema ::.", justify="center")
        lbl_titulo.pack(pady=10)

        lbl_email=Label(ventana,text="Ingresa tu email ",justify="center")
        lbl_email.pack(pady=10)

        txt_email=Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=10)

        lbl_password=Label(ventana,text="Ingresa tu password ",justify="center")
        lbl_password.pack(pady=10)

        txt_password=Entry(ventana,show="*")
        txt_password.pack(pady=10)

        btn_entrar=Button(ventana,text="Entrar ", justify="center",command=lambda: controlador.Controlador.login(txt_email.get(),txt_password.get(),ventana))
        btn_entrar.pack(pady=10)

        btn_regresar=Button(ventana, text="Volver", justify="center" ,command=lambda: View.menu_principal(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        View.borrarPantalla(ventana)

        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        lbl_titulo=Label(ventana,text= f".:: Bienvenido {nombre} {apellidos}, has iniciado sesion ::.", justify="center")
        lbl_titulo.pack(pady=5)

        btn_crear=Button(ventana,text="1.- Crear",justify="center",command=lambda: View.crear_nota(ventana))
        btn_crear.pack(pady=10)

        btn_mostrar=Button(ventana,text="2.- Mostrar", justify="center",command=lambda: View.mostrar_nota(ventana))
        btn_mostrar.pack(pady=10)

        btn_cambiar=Button(ventana, text="3.- Cambiar ", justify="center" ,command=lambda: View.cambiar_nota(ventana))
        btn_cambiar.pack(pady=10)

        btn_eliminar=Button(ventana, text="4.- Eliminar ", justify="center" ,command=lambda: View.borrar_nota(ventana))
        btn_eliminar.pack(pady=10)

        btn_regresar=Button(ventana, text="5.- Regresar ", justify="center" ,command=lambda: View.login(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def crear_nota( ventana):
        View.borrarPantalla(ventana)
        lbl_titulo0=Label(ventana,text= ".:: Crear nota ::.", justify="center")
        lbl_titulo0.pack(pady=5)

        lbl_titulo=Label(ventana,text= "Titulo:", justify="center")
        lbl_titulo.pack(pady=5)

        txt_titulo=Entry(ventana)
        txt_titulo.focus()
        txt_titulo.pack(pady=15)

        lbl_descripcion=Label(ventana,text= "Descripcion:", justify="center")
        lbl_descripcion.pack(pady=5)

        txt_descripcion=Entry(ventana)
        txt_descripcion.pack(pady=15)

        btn_guardar=Button(ventana,text="Guardar", justify="center",command=lambda: controlador.Controlador.crear_nota(id_user,txt_titulo.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=15)

        btn_regresar=Button(ventana, text="Regresar", justify="center" ,command=lambda: View.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_regresar.pack(pady=15)


    @staticmethod
    def mostrar_nota(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text= f"{nom_user} {ape_user} tus notas son:", justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=controlador.Controlador.mostrar_nota(id_user)

        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"Nota: {num_notas}\n ID:{fila[0]}.- Titulo {fila[2]} Fecha de creacion: {fila[4]} \n Descripcion:{fila[3]}"
                num_notas+=1

            
        else:
            messagebox.showinfo(icon="info",message="..::No existen notas para este usuario")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana, text="Volver", justify="center" ,command=lambda: View.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_nota(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo0=Label(ventana,text= f"{nom_user} {ape_user}, vamos a modificar una nota", justify="center")
        lbl_titulo0.pack(pady=10)

        lbl_id=Label(ventana,text= "ID de la nota :", justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana)
        txt_id.focus()
        txt_id.pack(pady=15)

        lbl_titulo=Label(ventana,text= "Nuevo titulo:", justify="center")
        lbl_titulo.pack(pady=5)

        txt_titulo=Entry(ventana)
        txt_titulo.pack(pady=15)

        lbl_descripcion=Label(ventana,text= "Nueva Descripcion:", justify="center")
        lbl_descripcion.pack(pady=5)

        txt_descripcion=Entry(ventana)
        txt_descripcion.pack(pady=15)

        btn_guardar=Button(ventana,text="Guardar", justify="center",command=lambda: controlador.Controlador.modificar_nota(txt_id.get(),txt_titulo.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=10)

        btn_regresar=Button(ventana, text="Volver", justify="center" ,command=lambda: View.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_regresar.pack(pady=10)

    @staticmethod
    def borrar_nota(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo0=Label(ventana,text= f"{nom_user} {ape_user}, vamos a eliminar una nota", justify="center")
        lbl_titulo0.pack(pady=10)

        lbl_id=Label(ventana,text= "ID de la nota :", justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana)
        txt_id.focus()
        txt_id.pack(pady=15)

        btn_eliminar=Button(ventana,text="Eliminar ", justify="center",command=lambda: controlador.Controlador.eliminar_nota(txt_id.get()))
        btn_eliminar.pack(pady=10)

        btn_regresar=Button(ventana, text="Volver", justify="center" ,command=lambda: View.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_regresar.pack(pady=10)




