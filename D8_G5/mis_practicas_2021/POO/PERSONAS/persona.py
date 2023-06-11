# from POO.logger_base import log

class Persona:

    contador_peronas = 0
    @classmethod
    def generate_id(cls):
        cls.contador_peronas+=1
        return cls.contador_peronas

    def __init__(self, id_persona, nombre, apellido, email):
        # Persona.contador_peronas+=1
        self.__id_persona = Persona.generate_id()
        self.set_nombre(nombre)
        self.set_apellido(apellido)
        self.__email = email

    def info(self):
        return self.__dict__

    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self.__id_persona = id_persona

    # @property
    # def nombre(self):
    #     return self.__nombre

    # @nombre.setter
    def set_nombre(self, nombre):
        self.__nombre = str(nombre)

    # @property
    # def apellido(self):
    #     return self.__apellido

    # @apellido.setter
    def set_apellido(self, apellido):
        if not apellido:
            print("zexrectvybu")
        self.__apellido = str(apellido)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = str(email)


# ejemplo de herencia
class Empleado(Persona):
    def __init__(self, id_persona, nombre, apellido, email, sueldo, id_empleado):
        super().__init__(id_persona, nombre, apellido, email)
        self.__id_empleado = int(id_empleado)
        self.__sueldo = int(sueldo)

    # def __str__(self):
    #     return {**super().__dict__, **self.__dict__}.items()

    def __str__(self):
        return {**vars(self), **vars(super())}.items()


if __name__ == '__main__':
    p1 = Persona(1, "asdh", "aslidj", "aslid")
    # log.debug(p1)
    p2 = Persona(2, nombre = 'aijsdia', apellido = "34", email = 'aslodh')
    # log.debug(p2)
    e1 = Empleado(2, "OIDJ", "OQIDJ", "OIDJKOID", 24334, 3)
    print(e1.__str__())
    # print(e1.mostrar_datos())

    # print(e1.___subclasses__())

    # def broadcast_message(
    #     message: str,
    #     servers: tuple[tuple[str, int], dict[str, str]]) -> None:
    
    # vector = list[float]
    # connectionOptions = dict[str, str]
    # address = tuple[str, int]
    # server = tuple[address, connectionOptions]

    # print(broadcast_message())




# def mi_funcion():
#     for i in listar_diccionarios
#         print(vars(i)) 