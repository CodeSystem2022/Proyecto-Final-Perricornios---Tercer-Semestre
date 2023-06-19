import psycopg2
from Cliente import Cliente

class Menu_Admin:

    def menu_admin(self):  # se presenta el menu de opciones de administrador
        print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario Administrador--\n------------------------------------------')
        print('Por favor digite la opcion a realizar:')
        print('Operacion 1: Listar Turnos')        
        print('Operacion 2: Eliminar Turnos')
        print('Operacion 3: Consultar Clientes')
        Operacion = int(input('Digite el numero de la opcion: '))
        while Operacion < 1 or Operacion > 3:
            Operacion = int(input('Opcion incorrecta, por favor intente de nuevo: '))
        if Operacion == 1:
            self.listar_turno()
        elif Operacion == 2:
            self.eliminar_turno()
        elif Operacion == 3:
            Cliente.buscarCliente(self)


    def listar_turno(self):
        return()
    
    def eliminar_turno(self):
        return
    
# Crear una instancia de la clase Menu_Admin
menu = Menu_Admin()

if __name__ == "__main__":
    menu.menu_admin()