import os 
os.system("clear ")

class Profesores ():
    def __init__(self,nombre,experiencia, num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor 

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre  

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self,experiencia):
        self.__experiencia=experiencia  

    @property
    def num_profesor (self):
        return self.__num_profesor 

    @num_profesor.setter
    def num_profesor (self,num_profesor):
        self.__num_profesor=num_profesor      

    #metodos
    def impartir (self):
        pass

    def evaluar(self):
        pass

class Alumnos ():
    def __init__(self,nombre, edad, matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre 

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad=edad 

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula

    def inscribirse (self):
        print("El alumno se ha inscrito")

    def estudiar(self):
        pass    

class Cursos ():
    def __init__(self,nombre, codigo, creditos ):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre 

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo 

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self,creditos):
        self.__creditos=creditos

    def asignar(self):
        pass

#objetos
profesor1=Profesores("Marlene",8, 123)
profesor2=Profesores("Itzel",7 ,126)

alumno1=Alumnos("Marysol",19, 371629)
alumno2=Alumnos("Danna",19, 371728)

curso1=Cursos("Musica",101, 4)
curso2=Cursos("POO",178,6)

print(f"Datos del profesor:\n Nombre: {profesor1.nombre}\n Experiencia: {profesor1.experiencia}\n Numero del profesor: {profesor1.num_profesor}")
print(f"Datos del profesor:\n Nombre: {profesor2.nombre}\n Experiencia: {profesor2.experiencia}\n Numero del profesor: {profesor2.num_profesor}")

print(f"Datos del alumno:\n Nombre: {alumno1.nombre}\n Edad: {alumno1.edad}\n Matricula: {alumno1.matricula}")
print(f"Datos del alumno:\n Nombre: {alumno2.nombre}\n Edad: {alumno2.edad}\n Matricula:{alumno2.matricula}")

print(f"Datos del curso:\n Nombre: {curso1.nombre}\n Codigo: {curso1.codigo}\n Creditos: {curso1.creditos}")
print(f"Datos del curso:\n Nombre: {curso2.nombre}\n codigo: {curso2.codigo}\n Creditos:{curso2.creditos}")

