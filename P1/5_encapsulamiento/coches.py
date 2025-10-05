import os 
os.system("clear ")

class Coches():

    #Metodo constructor. con este metodo se inicializa un objeto cuando es creado con valores iniciales

    def __init__(self,marca,color, modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

#Crear los metodos setters y getters estos metodos cson importantes y necesarios en tosas las clases 
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
        return "Estoy acelerando el coche"
    
    def frenar(self):
        return "Estoy frenando el coche"

#crear un objeto o instanciar una clase 