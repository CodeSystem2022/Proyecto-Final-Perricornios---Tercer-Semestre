class Admin:
    def __init__(self, user, password):
        self._user = input('Ingresá nombre de usuario o correo: ')
        self._password = input('Ingresá la contraseña: ')

    def validar_user(self):
        if self._user == 'admin' and self._password == '12345':
            print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario administrador--\n------------------------------------------')
        else:
            print('------------------------------------\n--Usuario o contraseña incorrectos--\n--------Intentalo nuevamente--------\n------------------------------------')

admin = Admin('admin', '12345')
admin.validar_user()