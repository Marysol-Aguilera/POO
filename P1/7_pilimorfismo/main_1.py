#instanciar los objetos para posterior implementarlos
import os 
from coches import Coches, Camiones, Camionetas

"""
coche=Coches("VW","Blanco","2020",220,200,5)
print(coche.marca,coche.acelerar())

camioneta=Camionetas("Nissan","Amarillo","2025",180,200,4,"trasera",False)
print(camioneta.marca,camioneta.acelerar())

camion=Camiones("Volvo","Blanco","2025",180,200,4,2,False)
print(camion.marca,camion.acelerar())

"""

def datos_autos(tipo):
    print("ingrese los datos del vehiculo {tipo}")
    marca=input("Marca").upper()
    color=input("Color").upper()
    modelo=input("Modelo").upper()
    velocidad=int (input("Veocidad"))
    potencia=int (input("Potencia"))
    plazas=int (input("No.plazas"))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    print(f"Datos del vehiculo:\n Marca: {marca()} \n Color: {color ()} \n Modelo: {modelo()} \n Velocidad: {velocidad ()} \n Potencia: {potencia()} \n Plazas: {plazas()}")

def autos():

    marca,color,modelo,velocidad,potencia,plazas=datos_autos ("Auto")
    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)

    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos ("Camiones")
    eje=int(input("No. de ejes"))
    capacidadCarga=int(input("Capacidad de carga"))

    coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"\n # Ejes: {coche.eje()} \n Capacidad Carga: {coche.capacidadCarga()}")

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos ("Camioneta")
    traccion=input("Traccion").upper()
    cerrada=input("cerrada? (Si/No):").upper()
    if cerrada=="SI":
        cerrada=True

    else:
        cerrada-False
    coche=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"\n Traccion: {coche.traccion ()} \n Cerrada: {coche.cerrada()}")


opcion=True
while opcion:
    os.system("clear")
    opcion=input("\n\t\t...Menu principal...\n1.-Autos \n2.-Camionetas \n3.-Camiones \n4.-Salir \n\tElige una opcion").lower() .strip()
    match opcion:
        case "1":
            os.system("clear")
            print("Auto")
            autos()
            input("oprima tecla para continuar")
        case "2":
            os.system("clear")
            print("Camioneta")
            camionetas()
            input("oprima tecla para continuar")
        case "3":
            os.system("clear")
            print("Camion")
            camiones()
            input("oprima tecla para continuar")
        case "4":
            os.system("clear")
            print("Gracias por utilizar el sw")
            input("oprima tecla para continuar")
            opcion=False
        case _:
            print("opcion no invalida......vuelva a intentarlo....")

