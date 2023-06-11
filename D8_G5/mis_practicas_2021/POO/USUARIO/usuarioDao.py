from POO.cursorpool import CursorDelPool
from POO.logger_base import log
from usuario import Usuario


class UsuarioDao:
    ''' DAO = DATA ACCSES OBJECT '''
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username, password) VALUES(%s,%s)'
    _UPDATE = 'UPDATE usuario SET username=%s, password=%s, WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def select(self):
        with CursorDelPool() as cursor:
            cursor.execute(self._SELECT)
            return [[Usuario(**u), u.__str__()] for u in cursor.fetchall()]

    @classmethod
    def insert(self, user):
        with CursorDelPool() as cursor:
            cursor.execute(self._INSERT, (user.username, user.password))
            log.debug(f'insert usuario > {user}')
            return cursor.rowcount

    @classmethod
    def update(self, user):
        with CursorDelPool() as cursor:
            cursor.execute(self._UPDATE, (user.username, user.password, user.id_usuario))
            return cursor.rowcount

    @classmethod
    def delete(self, user):
        with CursorDelPool() as cursor:
            cursor.execute(self._DELETE, (user.id_usuario,))
            return cursor.rowcount
