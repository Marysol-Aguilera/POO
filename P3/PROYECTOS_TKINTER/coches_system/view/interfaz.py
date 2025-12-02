from tkinter import *
#from controller import controlador
from tkinter import messagebox

class Vista:
    def __init__(self,ventana):
        ventana.title("Coches")
        ventana.geometry("1024x768")
        #ventana.resizable(False,False)         #para que la pantalla este fija
        self.menu_principal(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".:: Menu principal ::. ")
        lbl_titulo.pack(pady=10)

        btn_auto=Button(ventana,text="1.- Autos", command=lambda: self.menu_acciones(ventana))
        btn_auto.pack()

        btn_cam=Button(ventana,text="2.- Camionetas",command=lambda: "")
        btn_cam.pack()

        btn_camiones=Button(ventana,text="3.- Camiones",command=lambda: "")
        btn_camiones.pack()

        btn_salir=Button(ventana,text="4.- Salir", command=ventana.quit)
        btn_salir.pack()

    def menu_acciones(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Menu Acciones {tipo} ::. ")
        lbl_titulo.pack(pady=10)

        btn_inse=Button(ventana,text="1.- Insertar",command=lambda: self.insertar(ventana))
        btn_inse.pack()

        btn_consu=Button(ventana,text="2.- Consultar",command=lambda: self.consultar(ventana))
        btn_consu.pack()

        btn_actu=Button(ventana,text="3.- Actualizar",command=lambda: self.actualizar(ventana))
        btn_actu.pack()

        btn_elim=Button(ventana,text="4.- Eliminar",command=lambda: self.eliminar(ventana))
        btn_elim.pack()

        btn_regre=Button(ventana,text="5.- Regresar", command=lambda: self.menu_principal(ventana))
        btn_regre.pack()

    def insertar(self,ventana):
        self.borrarPantalla(ventana)   

        lbl_titulo=Label(ventana, text=".:: Datos del vehiculo: ::. ")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca:")
        lbl_marca.pack(pady=5)

        txt_marca=Entry(ventana,width=20,justify="right")
        txt_marca.focus()
        txt_marca.pack(side="top", anchor="center")

        lbl_color=Label(ventana,text="Color:")
        lbl_color.pack(pady=5)

        txt_color=Entry(ventana,width=20,justify="right")
        txt_color.pack(side="top", anchor="center")

        lbl_modelo=Label(ventana,text="Modelo:")
        lbl_modelo.pack(pady=5)

        txt_modelo=Entry(ventana,width=20,justify="right")
        txt_modelo.pack(side="top", anchor="center")

        lbl_velo=Label(ventana,text="Velocidad:")
        lbl_velo.pack(pady=5)

        txt_velo=Entry(ventana,width=20,justify="right")
        txt_velo.pack(side="top", anchor="center")

        lbl_caba=Label(ventana,text="Cabajalle:")
        lbl_caba.pack(pady=5)

        txt_caba=Entry(ventana,width=20,justify="right")
        txt_caba.pack(side="top", anchor="center")

        lbl_plaz=Label(ventana,text="Plazas:")
        lbl_plaz.pack(pady=5)

        txt_plaz=Entry(ventana,width=20,justify="right")
        txt_plaz.pack(side="top", anchor="center")

        btn_guar=Button(ventana,text="Guardar", command=lambda: "")
        btn_guar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones(ventana))
        btn_regre.pack()

    def eliminar(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Eliminar {tipo}::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_eliminar=Button(ventana,text="Eliminar", command=lambda: "")
        btn_eliminar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones(ventana))
        btn_regre.pack()

    def consultar(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Listado de vehiculos ::. ")
        lbl_titulo.pack(pady=10)
        
        registros=[]#[("1","nose","faak","nose","nose","faak","nose")]
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+(f"Auto: {num_operaciones} ID:{fila[0]}\n Marca: {fila[1]}\n Color:{fila[2]}\n Velocidad: {fila[3]}\n Potencia:{fila[4]}\n Plazas: {fila[5]}")
                num_operaciones+=1
        else:
            messagebox.showinfo(icon="info",message=".. No existen operaciones en el Sistema ... agrega operaciones ...")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones(ventana))
        btn_regre.pack()

    def actualizar(self,ventana):
        self.borrarPantalla(ventana)   

        lbl_titulo=Label(ventana, text=".:: Datos del vehiculo: ::. ")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        lbl_marca=Label(ventana,text="Marca:")
        lbl_marca.pack(pady=5)

        txt_marca=Entry(ventana,width=20,justify="right")
        txt_marca.pack(side="top", anchor="center")

        lbl_color=Label(ventana,text="Color:")
        lbl_color.pack(pady=5)

        txt_color=Entry(ventana,width=20,justify="right")
        txt_color.pack(side="top", anchor="center")

        lbl_modelo=Label(ventana,text="Modelo:")
        lbl_modelo.pack(pady=5)

        txt_modelo=Entry(ventana,width=20,justify="right")
        txt_modelo.pack(side="top", anchor="center")

        lbl_velo=Label(ventana,text="Velocidad:")
        lbl_velo.pack(pady=5)

        txt_velo=Entry(ventana,width=20,justify="right")
        txt_velo.pack(side="top", anchor="center")

        lbl_caba=Label(ventana,text="Cabajalle:")
        lbl_caba.pack(pady=5)

        txt_caba=Entry(ventana,width=20,justify="right")
        txt_caba.pack(side="top", anchor="center")

        lbl_plaz=Label(ventana,text="Plazas:")
        lbl_plaz.pack(pady=5)

        txt_plaz=Entry(ventana,width=20,justify="right")
        txt_plaz.pack(side="top", anchor="center")

        btn_guar=Button(ventana,text="Guardar", command=lambda: "")
        btn_guar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones(ventana))
        btn_regre.pack()