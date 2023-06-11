from POO.cursorpool import CursorDelPool
from POO.logger_base import log
from persona import Persona


class PersonaDao:
    ''' DAO = DATA ACCSES OBJECT '''
    _SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s, WHERE id_persona=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def select(self):
        with CursorDelPool() as cursor:
            cursor.execute(self._SELECT)
            return [Persona(id_persona=p[0], nombre=p[1], apellido=p[2], email=p[3]) for p in cursor.fetchall()]

    @classmethod
    def insert(self, per):
        with CursorDelPool() as cursor:
            cursor.execute(self._INSERT, tuple((per.nombre, per.apellido, per.email)))
            log.debug(f'insert persona > {per}')
            return cursor.rowcount

    @classmethod
    def update(self, per):
        with CursorDelPool() as cursor:
            cursor.execute(self._UPDATE, tuple((per.nombre, per.apellido, per.email, per.id_persona)))
            return cursor.rowcount

    @classmethod
    def delete(self, per):
        with CursorDelPool() as cursor:
            cursor.execute(self._DELETE, tuple((per.id_persona,)))
            return cursor.rowcount


if __name__ == '__main__':
    p1 = Persona(1, nombre="askudh", apellido="asodlji", email="asiudh")
    p2 = Persona(2, nombre="askudh", apellido="asodlji", email="asiudh")
    p3 = Persona(3, nombre="askudh", apellido="asodlji", email="asiudh")
    # p2 = Persona(1, nombre="askudh", apellido="asodlji", email="asiudh")
    p_insert = PersonaDao.insert(p1)
    p_insert1 =PersonaDao.insert(p2)
    p_insert2 =PersonaDao.insert(p3)
    # p_update = PersonaDao.update(p2)
    p_select = PersonaDao.select()
    print("SE EJECUTO EL METODO P_SELECT")
    # p = PersonaDao.update()
    # p = PersonaDao.delete()
    log.debug(f'{p_insert}')
    log.debug(f'{p_insert1}')
    log.debug(f'{p_insert2}')