import psycopg2 as bd
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'proyecto-final'
    _USERNAME = 'postgres'
    _PASSWORD = '1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _curson = None


    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(hots=cls._HOST,
                                          user=cls._USERNAME,
                                          password=cls._PASSWORD,
                                          port=cls._DB_PORT,
                                          database=cls._DATABASE)
                log.debug(f'Conexion Exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._conexion
            
@classmethod
def obtenerCursor(cls):
    if cls._cursor is None:
        try:
            cls._cursor = cls.obtenerConexion().cursor()
            log.debug(f'Se abrio correcatamente el cursor: {cls._cursor}')
            return cls._cursor
        except Exception as e:
            log.error(f'Ocurrio un error: {e}')
    else:
        return cls._cursor
    
if __name__ == '__main__':
    Conexion.obetenerConexion()
    Conexion.obtenerCursor()