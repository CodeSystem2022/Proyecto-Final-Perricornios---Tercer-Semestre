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
        datos_correctos = False #bandera
        self._user = input('Ingrese el nombre de usuario o correo: ')
        
        while not datos_correctos:
            
            if self._user == 'admin' :
                self._password = input('Ingrese la contraseña: ')
                if self._password == '12345':
                    datos_correctos = True
                    print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario administrador--\n------------------------------------------')

                else:
                    print('------------------------------------\n--------Contraseña incorrecta-------\n--------Intentalo nuevamente--------\n------------------------------------')

            else:
                print('------------------------------------\n---------Usuario incorrecto---------\n--------Intentalo nuevamente--------\n------------------------------------')
                self._user = input('Ingrese el nombre de usuario: ')

admin = Admin('', '') #se instancia un objeto vacío de la clase para validar
admin.validar_user() #se llama al método para validar el usuario