class Admin:
    def __init__(self, user, password):
        self._user = user
        self._password = password

    def validar_user(self):
        datos_correctos = False #bandera

        while not datos_correctos:
            self._user = input('Ingresá nombre de usuario o correo: ')
            self._password = input('Ingresá la contraseña: ')
            
            if self._user == 'admin' and self._password == '12345':
                datos_correctos = True
                print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario administrador--\n------------------------------------------')
            else:
                print('------------------------------------\n--Usuario o contraseña incorrectos--\n--------Intentalo nuevamente--------\n------------------------------------')

admin = Admin('admin', '12345')
admin.validar_user()