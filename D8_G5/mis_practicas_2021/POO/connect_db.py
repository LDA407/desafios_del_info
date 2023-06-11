from POO.logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'amdlk'
    _USERNAME = 'askdmlak'
    _PASSWORD = 'asldkmalskdm'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON=1
    _MAX_CON=5
    _pool = None
    # _conexion = None
    # _cursor = None

    @classmethod
    def obtenerPool(self):
        if self._pool is None:
            try:
                self._pool = pool.SimpleConnectionPool(
                    self._MIN_CON,
                    self._MAX_CON,
                    host=self._HOST,
                    user=self._USERNAME,
                    password=self._PASSWORD,                    
                    port=self._DB_PORT,
                    database=self._DATABASE
                )
                log.debug(f"conexion completa: {self._pool}")
                return self._pool
            except Exception as e:
                log.debug(e); sys.exit()
        else:
            return self._pool

    @classmethod
    def obtenerConexionDelPool(self):
        conexion = self.obtenerPool().getconn()
        log.debug(conexion)
        return conexion

    @classmethod
    def liberarConexion(self, conexion):
        self.obtenerPool().putconn(conexion)

    @classmethod
    def cerrarPool(self):
        self.obtenerPool().closeall()


    # @classmethod
    # def obtenerConexion(self):
    #     if self._conexion is None:
    #         try:
    #             self._conexion = db.connect(
    #                 host=self._HOST,
    #                 user=self._USERNAME,
    #                 password=self._PASSWORD,                    
    #                 port=self._DB_PORT,
    #                 database=self._DATABASE
    #             )
    #             log.debug(f"conexion completa: {self._conexion}")
    #             return self._conexion
    #         except Exception as e:
    #             log.debug(e); sys.exit()
    #     else:
    #         return self._conexion

    # @classmethod
    # def obtenerCursor(self):
    #     if self._cursor is None:
    #         try:
    #             self._cursor = self.obtenerConexion().cursor()
    #             log.debug("se abrio el cursor")
    #             return self._cursor
    #         except Exception as e:
    #             log.error(e); sys.exit()
    #     else:
    #         return self._cursor

if __name__ == '__main__':
    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()
    con1 = Conexion.obtenerConexionDelPool()
    con2 = Conexion.obtenerConexionDelPool()