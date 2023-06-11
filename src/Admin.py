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
        intentos = 4
        datos_correctos = False #bandera o flag
        self._user = input('Ingresá el nombre de usuario o correo: ')
        
        while not datos_correctos and intentos > 0:
            
            if self._user == 'admin' :
                self._password = input('Ingresá la contraseña: ')
                if self._password == '12345':
                    datos_correctos = True
                    print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario administrador--\n------------------------------------------')

                else:
                    intentos -= 1 #disminuye la cantidad a 3 intentos restantes
                    print('------------------------------------\n--------Contraseña incorrecta-------\n--------Intentalo nuevamente--------\n------------------------------------')

                    if intentos == 0: #si es cero, lo saca del sistema y lo devuelve al menú
                        print('Demasiados intentos..\n       Acceso denegado..\n              ..Saliendo del menú...')
                        break

                    if intentos == 1:
                        print(f'Te queda {intentos} restante.')
                    else:
                        print(f'Te quedan {intentos} intentos restantes.')
    
            else:
                print('------------------------------------\n---------Usuario incorrecto---------\n--------Intentalo nuevamente--------\n------------------------------------')
                self._user = input('Ingrese el nombre de usuario: ')
            
admin = Admin('', '') #se instancia un objeto vacío de la clase para validar
admin.validar_user() #se llama al método para validar el usuario