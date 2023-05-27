"""
Se requiere la creacion de una clase Cliente, la misma requiere contar con los siguientes
atributos y metodos :
Atributos :
-Nombre
-Apellido
-Genero
-Masaje : objeto de tipo Masaje

Metodos:
+get() y set()
+clienteNuevo() : Deberá contar con un método
que solicite al cliente su nombre, apellido y género,
concatene nombre y apellido con un espacio de por medio,
y asigne sus valores a sus respectivas variables.
"""
import Masaje #se importa la clase Masaje

class Cliente:

    def __init__(self, nombre, apellido, genero, masaje): #constructor
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.masaje = Masaje
        
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def set_genero(self, genero):
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_masaje(self, masaje):
        self.masaje = masaje

    def get_masaje(self):
        return self.masaje

    def clienteNuevo(self):
        nombre = input("\nIngresá tu nombre: ")
        apellido = input("Ingresá tu apellido: ")
        genero = input("Ingresá tu género: ")
    
        print('\nDatos ingresados: \n----------------------------')
        print("Nombre: ", nombre)
        print("Apellido: ", apellido)
        print("Género: ", genero)
        print("----------------------------")
    

# se instancia un objeto de la clase Cliente
cliente = Cliente("", "", "", "")
#se llama al método para que se instancien los atributos
cliente.clienteNuevo()

