"""
Se requiere la creacion de una clase Menu.

Objetivo: La misma tiene como objetivo ejecutar las distintas funciones de las otras 
clases y dirigir al cliente por el sistema

Antes de comenzar la clase requiere crear un objeto de tipo Cliente , este objeto es 
el que iremos utilizando a lo largo de la ejecución para lanzar 
los métodos que tiene implementados y guardar los datos introducidos. (Esto no, ya está creado)

Requisitos de Clase :

Deberá presentarse una bienvenida al sistema con un menú de opciones disponibles :
OP 1 Cliente Nuevo
- ejecutar la funcion del cliente : clienteNuevo()
- ejecutar la funcion del cliente : validar()
- ejecutar la funcion del cliente : mostrarDatos()
- ejecutar la funcion del cliente : Saludar()
- ejecutar la funcion del cliente : cargarMasaje()
- ejecutar la funcion del cliente : cargarCliente()
- ejecutar la funcion del cliente : cargarTurno()
OP 2 Cargar Cliente
- ejecutar la funcion del cliente : buscarCliente()
- ejecutar la funcion del cliente : Saludar()
- ejecutar la funcion del cliente : cargarMasaje()
- ejecutar la funcion del cliente : actualizarCliente()
- ejecutar la funcion del cliente : cargarTurno()

OP 3
Debera comprobar si el usuario es administrador utilizando la clase admin
Debera desplegar distintas operaciones para el administrador
Operacion 1 : Listar Turnos
Operacion 2 : Eliminar Turnos
Operacion 3 : Consultar Clientes


"""


#      Ejemplo de clase menu :


from Cliente import Cliente
from Admin import Admin

class Menu:
    def __init__(self):
        self.cliente = None
        self.admin = None
        self.opcion = None

    def mostrar_menu(self):
        while True:
            print("Bienvenido al sistema de masajes\n         Perricornios\n--------------------------------")
            print("Menú de opciones disponibles:")
            print("1. Cliente Nuevo")
            print("2. Cargar Cliente")
            print("3. Modo Administrador")
            print("0. Salir")
            self.opcion = input("Ingrese la opción deseada: ")
    
            if self.opcion == "1": #Ingresa modo Cliente
                self.cliente = Cliente("","","","")
                self.cliente.clienteNuevo()
                self.cliente.editarDatos()
                self.cliente.saludar()
                self.cliente.cargarCliente()
                self.cliente.cargarTurno()
                break
            elif self.opcion == "2":
                self.cliente = Cliente("","","","")
                self.cliente.buscarCliente()
                self.cliente.saludo()
                self.cliente.cargarTurno()
                break
            elif self.opcion == "3": #Ingresa modo Administrador 
                self.admin = Admin("","")
                self.admin.validar_user()
                self.admin.opcionesAdmin()
                break
            elif self.opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida") 
                
menu = Menu()
menu.mostrar_menu()
