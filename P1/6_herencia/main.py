#instanciar los objetos para posterior implementarlos
import os 
os.system("clear")

from coches import Coches, Camiones, Camionetas

coche=Coches("VW","Blanco","2020",220,200,5)
print(coche.marca,coche.acelerar())

camioneta=Camionetas("Nissan","Amarillo","2025",180,200,4,"trasera",False)
print(coche.marca,coche.acelerar())

camion=Camiones("Volvo","Blanco","2025",180,200,4,2,False)
print(coche.marca,coche.acelerar())

"""
num_coches=int(input("Cuantos coches deseas"))

for i in range(0,num_coches):
    print ("\n\t Datos del coche")
    marca=input("ingresa la marca").upper()
    color=input("ingresa el color").upper()
    modelo=input("ingresa el modelo").upper()
    velocidad=int (input("ingresa la veocidad"))
    potencia=int (input("ingresa la potencia"))
    plazas=int (input("ingresa las plazas"))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    #coche1=Coches("VW","Blanco","2022",220,150,5)
    #coche2=Coches("Nissan","Azul","2020",180,50,6)
    #coche3=Coches("Honda","","",0,0,0)

    print(f"Datos del vehiculo:\n Marca: {coche1.getMarca()} \n Color: {coche1.getColor ()} \n Modelo: {coche1.getModelo()} \n Velocidad: {coche1.getVelocidad ()} \n Caballaje: {coche1.getCaballaje()} \n Plazas: {coche1.getPlazas()}")
    print(f"\n\t {coche1.acelerar}")
    #print(f"Datos del vehiculo:\n Marca: {coche2.getMarca()} \n Color: {coche2.getColor()}\n Modelo: {coche2.getModelo()} \n Velocidad: {coche2.getVelocidad()} \n Caballaje: {coche2.getCaballaje()} \n Plazas: {coche2.getPlazas()}")

    #print(f"Datos del vehiculo:{coche3.marca}")
    """