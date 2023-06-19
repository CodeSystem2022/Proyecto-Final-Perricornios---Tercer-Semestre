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
import psycopg2

class Cliente:

    def __init__(self, nombre, apellido, genero, masaje): #constructor
        #Los atributos tienen que ir vacios para que puedan ser llenados al lanzar la funcion clienteNuevo
        self._nombre = None
        self._apellido = None
        self._genero = None #se lo instancia en None para validarla después
        self._masaje = None
        
        
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


    def validar(self):
        while not cliente.nombre.strip():
            print('\n----------------------------\nNombre no puede estar vacío.\nIntentalo nuevamente...\n----------------------------')
            cliente._nombre = input("\nIngresá tu nombre: ")
            
        while not cliente.apellido.strip():
            print('\n---------------------------\nApellido no puede estar vacío.\nIntentalo nuevamente...\n---------------------------')
            cliente._apellido = input("\nIngresá tu apellido: ")
            
    def clienteNuevo(self):
        #Solicito los datos
        nombre = input("Ingresa tu nombre : ")
        apellido = input("Ingresa tu apellido : ")
        #los establezco en su respectiva variable/atributo
        self._nombre = nombre
        self._apellido = apellido

    
    def mostrarDatos(cliente):
        #se muestran los datos
        print('')
        print('Datos ingresados'.center(28,'-'))
        print("Nombre: ", cliente._nombre)
        print("Apellido: ", cliente._apellido)
        #print("Género: ", cliente.genero)
        print("----------------------------")


    def editarDatos(cliente): #permite al cliente asegurarse de ingresar al sistema de turnos con sus datos correctos
        datos_correctos = False #bandera para que el cliente pueda editar sus cambios hasta que sea True
    
        while not datos_correctos:
            cliente.validar()
            print('¿Los datos ingresados son correctos?')
            print('----------------------------\nIngresá 1 para guardar\nIngresá 2 para editar\n----------------------------')
        
            opcion = int(input('Ingresá el número de la opción: '))

            if opcion == 1: #ingresa satisfactoriamente al sistema
                print('------------------------------------\nLos datos se guardaron satisfactoriamente\n------------------------------------')
                cliente.mostrarDatos()
                datos_correctos = True #recién cuando el ingrese la opción 1 es que se lo ingresa al sistema
                
            elif opcion == 2: #se le muestran las opciones para editar su nombre o su apellido las veces que necesite
                print(f'\n-------------------------------\nIngresá 1 para editar el nombre -> ({cliente._nombre})\nIngresá 2 para editar el apellido -> ({cliente._apellido}): ')
                print('-------------------------------\n¿Qué dato querés corregir?')
                opcion = int(input('Ingresá el número de la opción: '))

                if opcion == 1: #se setea el nombre con valor que coloque
                    cliente._nombre = input('\n----------------------------\nIngresá nuevamente el nombre: ')
                elif opcion == 2: #se setea el apellido con el valor que coloque
                    cliente._apellido = input('\n-------------------------------\nIngresá nuevamente el apellido: ')
                
                cliente.validar() #no se le van a permitir ingresar campos en blanco, por eso se llama a la función validar
                print('------------------------------------')
                cliente.mostrarDatos() #se le vuelven a mostrar los datos para que verifique si están correctos después de los cambios




    def saludar(cliente): # Dá un saludo personalizado al cliente dependiendo si es mujer, hombre o género no binario
        #cliente.validar()
        print(f'\n----------Hola, {cliente._nombre}----------')

        opcion_valida = False #bandera, flag

        while not opcion_valida:
            cliente._genero = input("Ingresá tu género:\n      <F> -> si sos mujer\n      <M> -> Si sos hombre\n      <O>--< Para otro género\n------------------------------\nIngresá un caracter: ")
            hombre = 'M'
            mujer = 'F'
            otro = 'O'

            if (cliente._genero) == hombre:
                print('\n***********************************************************')
                print(f'¡Hola {cliente._nombre}, Bienvenido a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif (cliente._genero) == mujer:
                print('\n***********************************************************')
                print(f'¡Hola {cliente._nombre}, Bienvenida a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif cliente._genero == otro:
                print('\n***********************************************************')
                print(f'¡Hola {cliente._nombre}, Bienvenide a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif cliente._genero != hombre or cliente._genero != mujer or cliente._genero != otro:
                #llama de nuevo a la función
                print('Opción no valida intentalo de nuevo')
                print('-'.center(32,'-'))
        print('**'.center(59,'*'))


    """
    CargarMasaje : deberá contar con un método propio que ejecute el método de la clase Masaje, masajes().
    """
    def buscarCliente(self):
        
        #Solicitamos el ID del cliente
        id = input("\nIngresá el ID de Cliente a buscar: ")

        # Establecer conexión con la base de datos
        conn = psycopg2.connect(
            user="perricornios",
            password="perricornios_pfinal",
            host="localhost",
            port="5432",
            database="tienda",

        )
        
        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()
        
        # Realizar la consulta para buscar el cliente por ID
        cursor.execute("SELECT * FROM tienda.clientes WHERE ID=%s", (id,))
        
        # Obtener los resultados de la consulta
        resultado = cursor.fetchone()
        
        if resultado:
            # Asignar los datos del cliente encontrado a variables
            self._nombre = resultado[1]
            self._genero = resultado[2]
            self._masaje = resultado[3]
            
            # Mostrar los datos del cliente encontrado
            print("Los datos del Cliente ID ", resultado[0])
            print("Nombre: ", self._nombre)
            print("Genero: ", self._genero)
            print("Masaje: ", self._masaje)

        else:
            print("Cliente no encontrado")
        
        # Cerrar la conexión con la base de datos
        conn.close()
    
if __name__ == "__main__":
    # se instancia un objeto de la clase Cliente
    cliente = Cliente("", "", "", "")
    #cliente.buscarCliente()
    cliente.clienteNuevo() # Se llama al método para que se instancien los atributos
    ##después se le muestra los datos
    #cliente.validar()
    cliente.mostrarDatos() #Le mostramos los datos para que chequee si están correctos
    cliente.editarDatos() #Le ofrecemos la opción de editar su nombre y apellido
    cliente.saludar() #primero se le dá la bienvenida
    #cliente.buscarCliente()
