import os 
os.system("clear ")

class Coches():

    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0


    #Metodos o acciones
    def acelerar(self):
        pass
    
    def frenar(self):
        pass


coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"Datos del vehiculo:\n Marca: {coche1.marca} \n Color: {coche1.color}\n Modelo: {coche1.modelo} \n Velocidad: {coche1.velocidad} \n Caballaje: {coche1.caballaje} \n Plazas: {coche1.plazas}")

coche2=Coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=50
coche2.velocidad=6

print(f"Datos del vehiculo:\n Marca: {coche2.marca} \n Color: {coche2.color}\n Modelo: {coche2.modelo} \n Velocidad: {coche2.velocidad} \n Caballaje: {coche2.caballaje} \n Plazas: {coche2.plazas}")


#print(coche1.acelerar(50))
#print(coche2.frenar(100))