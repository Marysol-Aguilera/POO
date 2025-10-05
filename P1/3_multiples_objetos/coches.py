import os 
os.system("clear ")

class Coches():

    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0

#crear los metodos setters y getters estos metodos cson importantes y necesarios en tosas las clases 
#para que el programador interactue con los valores de los atributos a traves de estosmetodos,
#digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para 
#ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto

#en teoria se deberia de crear un metodo getters y setters por cada atributo que contenga la clase

#Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del retun 
# por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor dek atributo
# o propiedad en cuestion 


    #1 forma 
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca


    #2 forma     
    @property
    def marca(self):         #
        return self.__marca  # 
    
    @marca.setter
    def marca(self,marca):
        self.__marca=marca 
    ##########################    

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color=color   
        
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo=modelo  

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad  

    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje  

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self,plazas):
        self.__plazas=plazas              

    
    #Metodos o acciones
    def acelerar(self):
        pass
    
    def frenar(self):
        pass


#Multiples objetos
coche1=Coches()
coche2=Coches()
coche3=Coches()


coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie="8u2uwyw7w"

print(f"Datos del vehiculo:\n Marca: {coche1.getMarca() } \n Color: {coche1.getColor ()} \n Modelo: {coche1.getModelo()} \n Velocidad: {coche1.getVelocidad ()} \n Caballaje: {coche1.getCaballaje()} \n Plazas: {coche1.getPlazas()}")


coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(50)
coche2.setPlazas(6)

print(f"Datos del vehiculo:\n Marca: {coche2.getMarca()} \n Color: {coche2.getColor()}\n Modelo: {coche2.getModelo()} \n Velocidad: {coche2.getVelocidad()} \n Caballaje: {coche2.getCaballaje()} \n Plazas: {coche2.getPlazas()}")

coche3=Coches()
coche3.marca="honda"
print(f"Datos del vehiculo:{coche3.marca}")