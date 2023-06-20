class Admin:
    def __init__(self, user, password):
        self._user = None
        self._password = None

    #Métodos getters y setters
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password


    def validar_user(self):
        intentos_user = 4
        intentos_password = 4
        datos_correctos = False #bandera o flag
        print("-------------------------------------")
        self._user = input('Ingresá el nombre de usuario o correo: ')
        
        while not datos_correctos and intentos_user > 0:
            
            if self._user == 'admin' :
                while intentos_password > 0:
                    print("-------------------------------------")
                    self._password = input('Ingresá la contraseña: ')
                    if self._password == '12345':
                        datos_correctos = True
                        print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario Administrador--\n------------------------------------------')
                        break #sale del bucle
                        #Derivarlo a las diferentes opciones de menú
                        
                    else:
                        print(f'------------------------------------\n--------Contraseña incorrecta-------\n               {self._password}\n------------------------------------')
                        intentos_password -= 1 #disminuye la cantidad a 3 intentos restantes
                        if intentos_password == 0: #si es cero, lo saca del sistema y lo devuelve al menú
                            print('Agotaste los intentos..\n       Acceso denegado..\n                Saliendo del menú...')
                            break
                        if intentos_password == 1:
                            print(f'Te queda {intentos_password} restante.')
                        else:
                            print('         Intentalo nuevamente           \n------------------------------------')
                            print(f'Te quedan {intentos_password} intentos restantes.')
                break #sale de la ejecución, derivar al menú

            else:           
                intentos_user -=1
                
                if intentos_user == 0: #si es cero, lo saca del sistema y lo devuelve al menú
                    print('\n---------------------------------\nAgotaste todos los intentos..\n       Acceso denegado..\n              ..Saliendo del menú...')
                    break
                if intentos_user == 1:
                    print(f'    Te queda {intentos_user} intento restante.')
                else:
                    print('------------------------------------------------------------')
                    print('Nombre de usuario o correo incorrecto. Intentalo nuevamente')
                    print(f'Te quedan {intentos_user} intentos restantes.')
                self._user = input('----------------------------------------------\nIngresá tu nombre de usuario o correo: ')
    

    @classmethod
    def opcionesAdmin(cls):

        print("..Menú de opciones..\n---------------------------------")
        print("1. Para listar todos los turnos")
        print("2. Para eliminar todos los turnos de la tabla")
        print("3. Consultar un cliente por ID\n---------------------------------")

        opcion = int(input("Ingresá la opción que vas a realizar?: "))

        if opcion == 1:
            print("Se listan todos los turnos asignados..")
            _SELECCIONAR = 'SELECT * FROM "Perri_Centro_Spa"."Turnos"'

        elif opcion == 2:
            print("Se borrarán todos los turnos asignados..")
            print("Esta acción no se puede deshacer.\n------------------------------------------\n¡Se borraran todos los datos de la tabla!\n------------------------------------------")
            _SELECCIONAR = 'DROP * FROM "Perri_Centro_Spa"."Clientes"'

        elif opcion == 3:
            print("Se consulta por la lista de clientes en general")
            _SELECCIONAR = 'SELECT * FROM "Perri_Centro_Spa"."Clientes"'
        
        else:
            print('Opción no valida')
            

if __name__ == '__main__':      
    admin = Admin('', '') #se instancia un objeto vacío de la clase para validar
    admin.validar_user() #se llama al método para validar el usuario
    admin.opcionesAdmin()