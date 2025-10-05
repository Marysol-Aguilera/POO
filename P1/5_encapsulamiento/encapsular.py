#Encapsular, es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributosy 
#y metodos de una clase a la hora de usar un objeto o una herencia 

import os 
os.system("clear ")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__(self,color,tamano):
        self._color=color 
        self._tamano=tamano

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color=color  

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self,tamano):
        self._tamano=tamano  

    @property
    def atributopublico(self):
        return self.atributo_publico
    
    @atributopublico.setter
    def atributopublico(self, atributo_publico):
        self.atributo_publico=atributo_publico

    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    
    @atributo_protegido.setter
    def atributo_protegido(self, atributo_protegido):
        self._atributo_protegido=atributo_protegido

    @property
    def atributo_privado(self):
        return self.__atributo_privado
    
    @atributo_privado.setter
    def atributo_privado(self, atributo_privado):
        self.__atributo_privado=atributo_privado

#Ulilizar la calse
objeto=Clase("Rojo","Grande")
print(objeto.color,objeto.tamano)
print(objeto.atributopublico)
print(objeto.atributo_protegido)
print(objeto.atributo_privado)
objeto.color="Amarillo"
print (objeto.color )
