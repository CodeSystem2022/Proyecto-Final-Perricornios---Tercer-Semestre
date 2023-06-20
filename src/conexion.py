import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'tienda'
    _USERNAME = 'perricornios'
    _PASSWORD = 'perricornios_pfinal'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                print(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió un error al conectarse: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió un error al obtener el cursor: {e}')
        else:
            return cls._cursor
        
    @classmethod
    def listarTurnos(cls):
         with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                sql = 'SELECT * FROM tienda.turnos'
                cursor.execute(cls, sql)
                registros = cursor.fetchall()
                return (registros)

    @classmethod
    def eliminarTurnos(cls):
         with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls, sql)
                sql = 'DELETE FROM tienda.turnos'
                registros = cursor.fetchall()
            return (registros)

    @classmethod
    def consultarClientes(cls):
         with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                sql = 'SELECT * FROM tienda.clientes'
                cursor.execute(cls, sql)
                registros = cursor.fetchall()
            return (registros)

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
#    Conexion.realizarConsulta()
