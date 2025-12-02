from tkinter import *
from controller import funciones
from tkinter import messagebox

#interfaz o view
class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("1024x768")
        #ventana.resizable(False,False)         #para que la pantalla este fija
        self.interfaz(ventana)

    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1, width=5,justify="right")
        txt_numero1.focus()
        txt_numero1.pack(side="top", anchor="center")

        txt_numero2=Entry(ventana,textvariable=n2, width=5,justify="right")
        txt_numero2.pack(side="top", anchor="center")

        btn_sum=Button(ventana,text="+",command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_sum.pack()

        btn_resta=Button(ventana,text="-", command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multi=Button(ventana, text="*", command=lambda: funciones.Controladores.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
        btn_multi.pack()

        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("Division",n1.get(),n2.get(),"/"))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir", command=ventana.quit)
        btn_salir.pack()

    def menuPrincipal(self,ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar) 
        operaconesMenu=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label="Operaciones ", menu= operaconesMenu)
        operaconesMenu.add_command(label="Agregar", command=lambda: self.interfaz(ventana))
        operaconesMenu.add_command(label="Consultar", command=lambda: self.consultar(ventana))
        operaconesMenu.add_command(label="Cambiar", command=lambda: self.cambiar(ventana))
        operaconesMenu.add_command(label="Borrar", command=lambda: self.buscar(ventana))
        operaconesMenu.add_separator()
        operaconesMenu.add_command(label="Salir", command=ventana.quit)

    def eliminar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=".::Borrar una Operacion::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_eliminar=Button(ventana,text="Eliminar", command=lambda: funciones.Controladores.eliminar(id.get()))
        btn_eliminar.pack()

        btn_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        btn_volver.pack()

    def buscar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=".::Borrar una Operacion::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operacion:")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_buscar=Button(ventana,text="Buscar", command=lambda: {funciones.Controladores.buscar(id.get()),self.eliminar(ventana)})
        btn_buscar.pack()

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def consultar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=".:: Listado de la Operaciones ::. ")
        lbl_titulo.pack(pady=10)
        
        registros=funciones.Controladores.consultar()
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+f"\nOperacion: {num_operaciones} ID:{fila[0]} Fecha de Creación: {fila[1]}\n Operacion: {fila[2]}{fila[4]}{fila[3]}={fila[5]} "
                num_operaciones+=1
        else:
            messagebox.showinfo(icon="info",message=".. No existen operaciones en el Sistema ... agrega operaciones ...")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana) )
        btn_volver.pack(pady=5)

    def cambiar(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo = Label( ventana, text=".:: Listado de las Operaciones ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la Operacion:")
        lbl_id.pack(pady=10)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)
        
        lbl_num1=Label(ventana,text="Nuevo Numero 1:")
        lbl_num1.pack(pady=10)

        num1=IntVar()
        txt_num1=Entry(ventana,textvariable=num1, width=5,justify="right")
        txt_num1.pack(pady=5)
            
        lbl_num2=Label(ventana,text="Nuevo Numero 2:")
        lbl_num2.pack(pady=10)

        num2=IntVar()
        txt_num2=Entry(ventana,textvariable=num2, width=5,justify="right")
        txt_num2.pack(pady=5)

        lbl_signo=Label(ventana,text="Nuevo signo:")
        lbl_signo.pack(pady=10)

        signo=StringVar()
        txt_signo=Entry(ventana,textvariable=signo, width=5,justify="right")
        txt_signo.pack(pady=5)

        lbl_signo=Label(ventana,text="Nuevo resultado:")
        lbl_signo.pack(pady=10)

        resultado=IntVar()
        txt_resultado=Entry(ventana,textvariable=resultado, width=5,justify="right")
        txt_resultado.pack(pady=5)

        btn_guardar=Button(ventana, text="Guardar", command=lambda: funciones.Controladores.cambiar(num1.get(),num2.get(),signo.get(),resultado.get(),id.get()))
        btn_guardar.pack()
        
        btn_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        btn_volver.pack()

