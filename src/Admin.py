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


    print('\nElegiste la opción ingresar al sistema modo Administrador..\n---------------------------------------------------------')

    def validar_user(self):
        intentos_login = 4
        datos_correctos = False #bandera o flag
        self._user = input('Ingresá el nombre de usuario o correo: ')
        self._password = input('Ingresá la contraseña: ')
        while not datos_correctos and intentos_login > 0:
            intentos_login -= 1
            if self._user == 'admin' and self._password == '12345':
                datos_correctos = True
                self.menu_admin()#se presenta el menu de opciones de administrador
            elif intentos_login < 4 and intentos_login > 0:
                print('Nombre de usuario o contraseña incorrecta. Intentalo nuevamente')
                print(f'Te quedan {intentos_login} intentos restantes.')
                self._user = input('----------------------------------------------\nIngresá tu nombre de usuario o correo: ')
                self._password = input('----------------------------------------------\nIngresá la contraseña: ')
            else: print('\n---------------------------------\nAgotaste todos los intentos..\n       Acceso denegado...\n')


    def menu_admin(self):#se presenta el menu de opciones de administrador
        print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario Administrador--\n------------------------------------------')
        print('Por favor digite la opcion a realizar:')
        print('Operacion 1: Listar Turnos')        
        print('Operacion 2: Eliminar Turnos')
        print('Operacion 3: Consultar Clientes')
        Operacion = int(input('Digite el numero de la opcion: '))
        while Operacion < 1 or Operacion > 3:
            if Operacion == 1:
                admin.validar_user
            elif Operacion == 2:
                admin.validar_user
            elif Operacion == 3:
                admin.validar_user
            else: print('Opcion incorrecta, por favor intente de nuevo')

            
admin = Admin('', '') #se instancia un objeto vacío de la clase para validar
admin.validar_user() #se llama al método para validar el usuario
