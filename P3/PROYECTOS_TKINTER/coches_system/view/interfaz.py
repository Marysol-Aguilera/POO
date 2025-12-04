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

        btn_auto=Button(ventana,text="1.- Autos", command=lambda: self.menu_acciones_a(ventana))
        btn_auto.pack()

        btn_cam=Button(ventana,text="2.- Camionetas",command=lambda: self.menu_acciones_c(ventana))
        btn_cam.pack()

        btn_camiones=Button(ventana,text="3.- Camiones",command=lambda: self.menu_acciones_ca(ventana))
        btn_camiones.pack()

        btn_salir=Button(ventana,text="4.- Salir", command=ventana.quit)
        btn_salir.pack()

    def menu_acciones_a(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Menu Acciones {tipo} ::. ")
        lbl_titulo.pack(pady=10)

        btn_inse=Button(ventana,text="1.- Insertar",command=lambda: self.insertar_autos(ventana))
        btn_inse.pack()

        btn_consu=Button(ventana,text="2.- Consultar",command=lambda: self.consultar_autos(ventana))
        btn_consu.pack()

        btn_actu=Button(ventana,text="3.- Actualizar",command=lambda: self.cambiar_autos(ventana))
        btn_actu.pack()

        btn_elim=Button(ventana,text="4.- Eliminar",command=lambda: self.borrar_autos(ventana))
        btn_elim.pack()

        btn_regre=Button(ventana,text="5.- Regresar", command=lambda: self.menu_principal(ventana))
        btn_regre.pack()    

    def menu_acciones_c(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Menu Acciones {tipo} ::. ")
        lbl_titulo.pack(pady=10)

        btn_inse=Button(ventana,text="1.- Insertar",command=lambda: self.insertar_camionetas(ventana))
        btn_inse.pack()

        btn_consu=Button(ventana,text="2.- Consultar",command=lambda: self.consultar_camionetas(ventana))
        btn_consu.pack()

        btn_actu=Button(ventana,text="3.- Actualizar",command=lambda: self.cambiar_camionetas(ventana))
        btn_actu.pack()

        btn_elim=Button(ventana,text="4.- Eliminar",command=lambda: self.borrar_camionetas(ventana))
        btn_elim.pack()

        btn_regre=Button(ventana,text="5.- Regresar", command=lambda: self.menu_principal(ventana))
        btn_regre.pack()

    def menu_acciones_ca(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Menu Acciones {tipo} ::. ")
        lbl_titulo.pack(pady=10)

        btn_inse=Button(ventana,text="1.- Insertar",command=lambda: self.insertar_camiones(ventana))
        btn_inse.pack()

        btn_consu=Button(ventana,text="2.- Consultar",command=lambda: self.consultar_camiones(ventana))
        btn_consu.pack()

        btn_actu=Button(ventana,text="3.- Actualizar",command=lambda: self.cambiar_camiones(ventana))
        btn_actu.pack()

        btn_elim=Button(ventana,text="4.- Eliminar",command=lambda: self.borrar_camiones(ventana))
        btn_elim.pack()

        btn_regre=Button(ventana,text="5.- Regresar", command=lambda: self.menu_principal(ventana))
        btn_regre.pack()

    def insertar_autos(self,ventana):
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

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_a(ventana))
        btn_regre.pack()

    def borrar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Eliminar Auto::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_eliminar=Button(ventana,text="Eliminar", command=lambda: "")
        btn_eliminar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_a(ventana))
        btn_regre.pack()

    def consultar_autos(self,ventana):
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
        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_a(ventana))
        btn_regre.pack()

    def cambiar_autos(self,ventana):
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

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_a(ventana))
        btn_regre.pack()

        #buscar
    
    def insertar_camionetas(self, ventana):
        self.borrarPantalla(ventana)   

        lbl_titulo=Label(ventana, text=".:: Datos de la Camioneta: ::. ")
        lbl_titulo.pack(pady=10)
        
        self.datos(ventana) 

        lbl_tra=Label(ventana,text="Traccion:")
        lbl_tra.pack(pady=5)

        txt_tra=Entry(ventana,width=20,justify="right")
        txt_tra.pack(side="top", anchor="center")

        lbl_cer=Label(ventana,text="Cerrada:")
        lbl_cer.pack(pady=5)

        txt_cer=Entry(ventana,width=20,justify="right")
        txt_cer.pack(side="top", anchor="center")

        btn_guar=Button(ventana,text="Guardar", command=lambda: "")
        btn_guar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_c(ventana))
        btn_regre.pack()

    def consultar_camionetas(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Listado de camionetas ::. ")
        lbl_titulo.pack(pady=10)
        
        registros=[]#[("1","nose","faak","nose","nose","faak","nose")]
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+(f"Camioneta: {num_operaciones} ID:{fila[0]}\n Marca: {fila[1]}\n Color:{fila[2]}\n Velocidad: {fila[3]}\n Potencia:{fila[4]}\n Plazas: {fila[5]}\n Traccion:{fila[6]}\n Cerrada:{fila[7]}")
                num_operaciones+=1
        else:
            messagebox.showinfo(icon="info",message=".. No existen operaciones en el Sistema ... agrega operaciones ...")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_c(ventana))
        btn_regre.pack()

    def cambiar_camionetas(self,ventana):
        self.borrarPantalla(ventana)   

        lbl_titulo=Label(ventana, text=".:: Datos de la camioneta: ::. ")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        self.datos(ventana)

        lbl_tra=Label(ventana,text="Traccion:")
        lbl_tra.pack(pady=5)

        txt_tra=Entry(ventana,width=20,justify="right")
        txt_tra.pack(side="top", anchor="center")

        lbl_cer=Label(ventana,text="Cerrada:")
        lbl_cer.pack(pady=5)

        txt_cer=Entry(ventana,width=20,justify="right")
        txt_cer.pack(side="top", anchor="center")

        txt_plaz=Entry(ventana,width=20,justify="right")
        txt_plaz.pack(side="top", anchor="center")

        btn_guar=Button(ventana,text="Guardar", command=lambda: "")
        btn_guar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_c(ventana))
        btn_regre.pack()

    def borrar_camionetas(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Eliminar camioneta::.")
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

    def insertar_camiones(self,ventana):
        self.borrarPantalla(ventana)   

        lbl_titulo=Label(ventana, text=".:: Datos del Camion: ::. ")
        lbl_titulo.pack(pady=10)
        
        self.datos(ventana) 

        lbl_eje=Label(ventana,text="Eje :")
        lbl_eje.pack(pady=5)

        txt_eje=Entry(ventana,width=20,justify="right")
        txt_eje.pack(side="top", anchor="center")

        lbl_carga=Label(ventana,text="Capacidad de carga:")
        lbl_carga.pack(pady=5)

        txt_carga=Entry(ventana,width=20,justify="right")
        txt_carga.pack(side="top", anchor="center")

        btn_guar=Button(ventana,text="Guardar", command=lambda: "")
        btn_guar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_ca(ventana))
        btn_regre.pack()

    def consultar_camiones(self,ventana):
        self.borrarPantalla(ventana)

        lbl_titulo=Label(ventana, text=".:: Listado de camiones ::. ")
        lbl_titulo.pack(pady=10)
        
        registros=[]#[("1","nose","faak","nose","nose","faak","nose")]
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+(f"Camion: {num_operaciones} ID:{fila[0]}\n Marca: {fila[1]}\n Color:{fila[2]}\n Velocidad: {fila[3]}\n Potencia:{fila[4]}\n Plazas: {fila[5]}\n Eje:{fila[6]}\n Capacidad Carga:{fila[7]}")
                num_operaciones+=1
        else:
            messagebox.showinfo(icon="info",message=".. No existen operaciones en el Sistema ... agrega operaciones ...")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_ca(ventana))
        btn_regre.pack()

    def cambiar_camiones(self,ventana):
        self.borrarPantalla(ventana)   

        lbl_titulo=Label(ventana, text=".:: Datos de la camioneta: ::. ")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        self.datos(ventana)

        lbl_eje=Label(ventana,text="Eje:")
        lbl_eje.pack(pady=5)

        txt_eje=Entry(ventana,width=20,justify="right")
        txt_eje.pack(side="top", anchor="center")

        lbl_carga=Label(ventana,text="Capacidad de carga:")
        lbl_carga.pack(pady=5)

        txt_carga=Entry(ventana,width=20,justify="right")
        txt_carga.pack(side="top", anchor="center")

        btn_guar=Button(ventana,text="Guardar", command=lambda: "")
        btn_guar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_c(ventana))
        btn_regre.pack()

    def borrar_camiones(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Eliminar Camiones ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_eliminar=Button(ventana,text="Eliminar", command=lambda: "")
        btn_eliminar.pack()

        btn_regre=Button(ventana,text="Regresar", command=lambda: self.menu_acciones_ca(ventana))
        btn_regre.pack()

    def datos(self,ventana):
        lbl_modelo=Label(ventana,text="Modelo:")
        lbl_modelo.pack(pady=5)

        txt_modelo=Entry(ventana,width=20,justify="right")
        txt_modelo.focus()
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