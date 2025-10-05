"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando
el metodo __init__.Calcular despues la suma, resta, multiplicacion y division.
Utilizar un metodo para cada una e imprimir los resultados obtenidos.
llamar a la clase calculadora 
"""

"""
class Calculadora():
    def __init__(self,num1,num2):
        self._num1=num1
        self._num2=num2

    @property
    def num1(self,num1):
        return self._num1
    
    @num1.setter
    def num1(self,num1):
        self._num1=num1

    @property
    def num2(self,num2):
        return self._num2
    
    @num2.setter
    def num2(self,num2):
        self._num2=num2

    def suma(num1,num2):
        suma=num1+num2
        return suma
    
    def resta(num1,num2):
        resta=num1-num2
        return resta
    
    def multi(num1,num2):
        multi=(num1)(num2)
        return multi
    
    def division(num1,num2):
        division=num1/num2
        return division
    
print("Calculadora")
num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))

"""

class Calculadora:
    def __init__(self):
        self._numero1=int(input("Numero #1:"))
        self._numero2=int(input("Numero #2:"))

    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self,numero1):
        self._numero1=numero1

    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self,numero2):
        self._numero2=numero2
        
    def sumar(self,):
        return self._numero1+self._numero2
    
    def restar(self,):
        return self._numero1-self._numero2
    
    def multiplicar(self,):
        return self._numero1*self._numero2
    
    def dividir(self,):
        return self._numero1/self._numero2
    
operacion=Calculadora()
print(f"{operacion.numero1}+{operacion._numero2}={operacion.sumar()}")
print(f"{operacion.numero1}-{operacion._numero2}={operacion.restar()}")
print(f"{operacion.numero1}*{operacion._numero2}={operacion.multiplicar()}")
print(f"{operacion.numero1}/{operacion._numero2}={operacion.dividir()}")

        