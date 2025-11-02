from conexionBD import *
import hashlib
import datetime

class Usuario:
    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasena = hashlib.sha256(password.encode()).hexdigest()

    #def hash_password(self,contrasena):
     #   return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrar(nombre,apellidos,email,contrasena):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre,apellidos,email,contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None         
        

