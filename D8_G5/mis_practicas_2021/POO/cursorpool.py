from POO.logger_base import log
from POO.connect_db import Conexion


# Concept resourse manager
class CursorDelPool:

    def __init__(self):
        self._conexion=None
        self._cursor=None

    def __enter__(self):
        log.debug('inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexionDelPool()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, type_exep, val_exep, traceback_exep):
        log.debug('se ejecuta el metodo __exit__')
        if val_exep:
            self._conexion.rollback()
            log.error(f'error > {val_exep}, {type_exep}, {traceback_exep}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('bloque with')
        # executing queries to create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employee
            (
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                EMAI TEXT NOT NULL
            )
            """
        )
        # commit the changes
        # conn.commit()
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall)