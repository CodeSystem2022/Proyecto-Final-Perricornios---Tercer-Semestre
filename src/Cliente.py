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
        self._nombre = input("\nIngresá tu nombre: ")
        self._apellido = input("Ingresá tu apellido: ")
        self._genero = None #se lo instancia en None para validarla después
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

    def saludar(cliente):
        print(f'\n-----------Hola, {cliente._nombre}-----------')

        opcion_valida = False #bandera, flag

        while not opcion_valida:
            cliente._genero = input("Ingresá tu género:\n      <F> -> si sos mujer\n      <M> -> Si sos hombre\n      <O>--< Para otro género\nIngresá un caracter: ")

            hombre = 'M'
            mujer = 'F'
            otro = 'O'

            if (cliente._genero) == hombre:
                print('\n***********************************************************')
                print(f'¡Hola {cliente._nombre} Bienvenido a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif (cliente._genero) == mujer:
                print('\n***********************************************************')
                print(f'¡Hola {cliente._nombre} Bienvenida a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif cliente._genero == otro:
                print('\n***********************************************************')
                print(f'¡Hola {cliente._nombre} Bienvenide a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif cliente._genero != hombre or cliente._genero != mujer or cliente._genero != otro:
                #llama de nuevo a la función
                print('Opción no valida intentalo de nuevo')
                print(''.center(32,'-'))
        print('**'.center(59,'*'))


    """
    CargarMasaje : deberá contar con un método propio que ejecute el método de la clase Masaje, masajes().
    """
    

# se instancia un objeto de la clase Cliente
cliente = Cliente("", "", "", "")
#se llama al método para que se instancien los atributos
cliente.saludar() #primero se le dá la bienvenida
cliente.clienteNuevo()#después se le muestra los datos

