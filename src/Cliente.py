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
from src.Masaje import Masaje #se importa la clase Masaje
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
        while not self.nombre.strip():
            print('\n----------------------------\nNombre no puede estar vacío.\nIntentalo nuevamente...\n----------------------------')
            self._nombre = input("\nIngresá tu nombre: ")
            
        while not self.apellido.strip():
            print('\n---------------------------\nApellido no puede estar vacío.\nIntentalo nuevamente...\n---------------------------')
            self._apellido = input("\nIngresá tu apellido: ")
            
    def clienteNuevo(self):
        #Solicito los datos
        nombre = input("---------------------\nIngresa tu nombre : ")
        apellido = input("Ingresa tu apellido : ")
        #los establezco en su respectiva variable/atributo
        self._nombre = nombre
        self._apellido = apellido

    
    def mostrarDatos(self):
        #se muestran los datos
        print('')
        print('Datos ingresados'.center(28,'-'))
        print("Nombre: ", self._nombre)
        print("Apellido: ", self._apellido)
        #print("Género: ", cliente.genero)
        print("----------------------------")


    def editarDatos(self): #permite al cliente asegurarse de ingresar al sistema de turnos con sus datos correctos
        datos_correctos = False #bandera para que el cliente pueda editar sus cambios hasta que sea True
    
        while not datos_correctos:
            self.validar()
            print('¿Los datos ingresados son correctos?')
            print('----------------------------\nIngresá 1 para guardar\nIngresá 2 para editar\n----------------------------')
        
            opcion = int(input('Ingresá el número de la opción: '))

            if opcion == 1: #ingresa satisfactoriamente al sistema
                print('------------------------------------\nLos datos se guardaron satisfactoriamente\n------------------------------------')
                self.mostrarDatos()
                datos_correctos = True #recién cuando el ingrese la opción 1 es que se lo ingresa al sistema
                
            elif opcion == 2: #se le muestran las opciones para editar su nombre o su apellido las veces que necesite
                print(f'\n-------------------------------\nIngresá 1 para editar el nombre -> ({self._nombre})\nIngresá 2 para editar el apellido -> ({self._apellido}): ')
                print('-------------------------------\n¿Qué dato querés corregir?')
                opcion = int(input('Ingresá el número de la opción: '))

                if opcion == 1: #se setea el nombre con valor que coloque
                    self._nombre = input('\n----------------------------\nIngresá nuevamente el nombre: ')
                elif opcion == 2: #se setea el apellido con el valor que coloque
                    self._apellido = input('\n-------------------------------\nIngresá nuevamente el apellido: ')
                
                self.validar() #no se le van a permitir ingresar campos en blanco, por eso se llama a la función validar
                print('------------------------------------')
                self.mostrarDatos() #se le vuelven a mostrar los datos para que verifique si están correctos después de los cambios




    def saludar(self): # Dá un saludo personalizado al cliente dependiendo si es mujer, hombre o género no binario
        #cliente.validar()
        print(f'\n----------Hola, {self._nombre}----------')

        opcion_valida = False #bandera, flag

        while not opcion_valida:
            self._genero = input("Ingresá tu género:\n      <F> -> si sos mujer\n      <M> -> Si sos hombre\n      <O>--< Para otro género\n------------------------------\nIngresá un caracter: ")
            hombre = 'M'
            mujer = 'F'
            otro = 'O'

            if (self._genero) == hombre:
                print('\n***********************************************************')
                print(f'¡Hola {self._nombre}, Bienvenido a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif (self._genero) == mujer:
                print('\n***********************************************************')
                print(f'¡Hola {self._nombre}, Bienvenida a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif self._genero == otro:
                print('\n***********************************************************')
                print(f'¡Hola {self._nombre}, Bienvenide a nuestro centro de belleza y spa!')
                opcion_valida = True
            elif self._genero != hombre or self._genero != mujer or self._genero != otro:
                #llama de nuevo a la función
                print('Opción no valida intentalo de nuevo')
                print('-'.center(32,'-'))
        print('**'.center(59,'*'))


    """
    CargarMasaje : deberá contar con un método propio que ejecute el método de la clase Masaje, masajes().
    """

    def masajes(self):
        masaje = Masaje()
        masaje.masajes()
        self._masaje = masaje.masaje


    def cargarTurno(self):
        # Establecer conexión con la base de datos
        conn = psycopg2.connect(
            user="perricornios",
            password="perricornios_pfinal",
            host="localhost",
            port="5432",
            database="tienda",
        )

        turno_valido = False  # <---Bandera
        mes = ' '
        dia = ' '
        numeroTurno = ' '
        turno = ' '
        print("Ingresá el mes de tu turno:(1 al 12)")
        mes = str(input())
        print("Ingresá el dia de tu turno(1 al 31)")
        dia = str(input())

        while not turno_valido:
            print("Ingresá el turno en qué querés atenderte:")
            print("Podes elegir 'M' -> para el turno mañana o")
            print("'T' -> para el turno tarde")
            
            turno = input()[0].lower()

            if turno == 'm':
                print("Elegiste el turno MAÑANA, tenes tres opciones para atenderte..")
                print("Ingresá 1 para el primer turno")
                print("Ingresá 2 para el segundo turno")
                print("Ingresá 3 para el tercer turno")
                
                numeroTurno = int(input())

                if numeroTurno == 1:
                    print("Felicitaciones, tenés el " + str(numeroTurno) + "° turno el día: " + str(dia) + " del mes: " + str(mes))
                    turno_valido = True
                elif numeroTurno == 2:
                    print("Felicitaciones, tenés el " + str(numeroTurno) + "° turno el día: " + str(dia) + " del mes: " + str(mes))
                    turno_valido = True
                elif numeroTurno == 3:
                    turno_valido = True
                    print("Felicitaciones, tenés el " + str(numeroTurno) + "° turno el día: " + str(dia) + " del mes: " + str(mes))

            elif turno == 't':
                print("Elegiste el turno TARDE, tenés tres opciones para atenderte..")
                print("Ingresá 4 para el primer turno")
                print("Ingresá 5 para el segundo turno")
                print("Ingresá 6 para el tercer turno")
                
                numeroTurno = str(input())

                if numeroTurno == 4:
                    print("------------------------------------------------------------------------------")
                    print("Felicitaciones, tenés el " + str(numeroTurno) + "° turno el día: " + str(dia) + " del mes: " + str(mes))
                    print("------------------------------------------------------------------------------")
                    turno_valido = True
                elif numeroTurno == 5:
                    print("------------------------------------------------------------------------------")
                    print("Felicitaciones, tenés el " + str(numeroTurno) + "° turno el día: " + str(dia) + " del mes: " + str(mes))
                    print("------------------------------------------------------------------------------")
                    turno_valido = True
                elif numeroTurno == 6:
                    print("------------------------------------------------------------------------------")
                    print("Felicitaciones, tenés el " + str(numeroTurno) + "° turno el día: " + str(dia) + " del mes: " + str(mes))
                    print("------------------------------------------------------------------------------")
                    turno_valido = True
                else:
                    print("ERROR! Ingresaste mal la opción, no se pudo elegir turno.")
                    print("Intentalo nuevamente en unos minutos..")
                turno_valido = True     
         
            # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

            #Consulta para verificar si el turno está ocupado
        columna_turno = f"Turno{numeroTurno}"
        cursor.execute(f'SELECT "{columna_turno}" FROM "Perri_Centro_Spa"."Turnos" WHERE "Dia"=%s AND "Mes"=%s',
                        (dia, mes))
        resultado = cursor.fetchone()
        id_cliente = ' '
        if resultado[0] is not None:
            print("El turno seleccionado está ocupado. Por favor, elija otro turno.")
        else:
                # Realizar la asignación del turno en la base de datos
            id_cliente = self._id_cliente
            cursor.execute(f'UPDATE "Perri_Centro_Spa"."Turnos" SET "{columna_turno}"=%s WHERE "Dia"=%s AND "Mes"=%s',
                            (id_cliente, dia, mes))
            conn.commit()
            print("Carga exitosa de turno.")
                
            '''
            if id_cliente is not None:
                id_cliente = self._id_cliente
                cursor.execute(f'UPDATE "Perri_Centro_Spa"."Turnos" SET "{columna_turno}"=%s WHERE "Dia"=%s AND "Mes"=%s',
                               (id_cliente, dia, mes))
                conn.commit()
                print("Carga exitosa de turno.")
                turno_valido = True
            else:
                print("Cliente no encontrado. Intente nuevamente.")   '''

            # Cerrar la conexión con la base de datos
        conn.close()

        
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
        cursor.execute('SELECT * FROM "Perri_Centro_Spa"."Clientes" WHERE id=%s', (id,))
        
        # Obtener los resultados de la consulta
        resultado = cursor.fetchone()
        
        if resultado:
            # Asignar los datos del cliente encontrado a variables
            self._nombre = resultado[1]
            self._genero = resultado[2]
            self._masaje = resultado[3]
            self._id_cliente = resultado[0]
            
            # Mostrar los datos del cliente encontrado
            print("Los datos del Cliente ID ", resultado[0])
            print("Nombre: ", self._nombre)
            print("Genero: ", self._genero)
            print("Masaje: ", self._masaje)

        else:
            print("Cliente no encontrado")
        
        # Cerrar la conexión con la base de datos
        conn.close()

    def cargarCliente(self):
        # Establecemos conexión con la base de datos
        conn = psycopg2.connect(
            user="perricornios",
            password="perricornios_pfinal",
            host="localhost",
            port="5432",
            database="tienda"
        )

        # Cursor para ejecutar consultas
        cursor = conn.cursor()

        # INSERT en la base de datos sin la ID
        cursor.execute(
            'INSERT INTO "Perri_Centro_Spa"."Clientes" ("Nombre", "Genero", "Masaje") VALUES (%s, %s, %s) RETURNING id',
            (self._nombre, self._genero, self._masaje)
        )
        id_cliente = cursor.fetchone()[0]
        conn.commit()
        self._id_cliente = id_cliente

        # Mostrar mensaje de carga exitosa y el ID asignado al cliente
        print("************")
        print("Carga de datos correcta.")
        print("ID asignado al cliente:", self._id_cliente)
        print("************")
        # Cerrar la conexión con la base de datos
        conn.close()
    
