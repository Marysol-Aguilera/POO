from estudiante import estudiante
import os 

class App:
    def __init__(self):
        pass

    def borrarPantalla(self):
        os.system("clear")

    def esperarTecla(self):
        print("\n \t \tOprima cualquier tecla para continuar ...")
        input() 

    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresa los siguientes datos del : '{tipo}' ...")
        nombre=input("Nombre: ").upper()
        calificacion=int(input("Calificacion:"))
        return nombre,calificacion
    
    def menu_acciones(self,tipo):
        print(f"\n\t\t.::  Menu de {tipo} ::.\n\t1.- Insertar \n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar ")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion

    def respuesta_sql(self,respuesta):
        if respuesta:
            print("\n\t... ¡ Accion realizada con Éxito !...")
        else:
            print("\n\t... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...") 
  
    def menu_estudiante(self,tipo):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Autos")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla()
                marca,color,modelo,velocidad,caballaje,plazas=self.autos()
                #Agregar a BD
                auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
                respuesta=auto.insertar()
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla()  
                registros=cochesBD.Autos.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}") 
                        num_autos+=1    
                    self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                print(f"\n \t .:: Actualizar Auto ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas=self.autos() 
                respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla()
                print(f"\n \t .:: Eliminar Auto ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Autos.eliminar(id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def main(self):
        opcion=1
        while opcion!="2":
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Estudiante \n\t2.- Salir \n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_estudiante()
                case "2":
                    self.borrarPantalla()
                    print("\n\t\t¡Gracias por utilizar el sistema!")
                    self.esperarTecla()    
                case _:
                    input("\nOpcion invalida ... vuelva a intertarlo ... ") 


if __name__=="__main__":
    app=App()