from POO.logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario: str = id_usuario
        self._username: str = username
        self._password = password

    def __str__(self):
        return f"Usuario: {self._id_usuario}, {self._username}, {self._password}"

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


if __name__ == '__main__':
    p1 = Usuario("asdh", "aslidj")
    log.debug(p1)
    p2 = Usuario('aijsdia', 'alsdh')
    log.debug(p2)
    a = ",".join("1234")
    print(a)
