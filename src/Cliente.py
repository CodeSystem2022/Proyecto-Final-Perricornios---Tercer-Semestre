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
import Masaje #se importa la clase

class Cliente:

    def __init__(self, nombre, apellido, genero, masaje): #constructor
        self._nombre = input("\nIngresá tu nombre: ")
        self._apellido = input("Ingresá tu apellido: ")
        self._genero = input("Ingresá tu género: ")
        self._masaje = Masaje
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero


    def clienteNuevo(self):
        #se muestran los datos
        print('')
        print('Datos ingresados'.center(28,'-'))
        print("Nombre: ", cliente.nombre)
        print("Apellido: ", cliente.apellido)
        print("Género: ", cliente.genero)
        print("----------------------------")
            

# se instancia un objeto de la clase Cliente
cliente = Cliente("", "", "", "")
#se llama al método para que se instancien los atributos
cliente.clienteNuevo()

