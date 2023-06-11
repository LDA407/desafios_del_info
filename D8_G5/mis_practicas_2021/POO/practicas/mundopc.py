from POO.logger_base import log

# agregacion de dispositivos de entrada
class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras+=1
        
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = str(nombre)
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def __str__(self):
        return f"""
            id: {self.__id_computadora}
            computadora: {self.__nombre}
            monitor: {self.__monitor}
            teclado: {self.__teclado}
            raton: {self.__raton}
        """

    @property
    def id_computadora(self):
        return self.__id_computadora

    # @id_computadora.setter
    # def id_computadora(self, id_computadora):
    #     self.__id_computadora = id_computadora

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


class Monitor:
    contador_monitor = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitor+=1
        self.__id_monitor = Monitor.contador_monitor
        self.__marca = str(marca)
        self.__tamanio = str(tamanio)

    def __str__(self):
        return f"id: {self.__id_monitor}, marca: {self.__marca}, tamaño: {self.__tamanio}"

    @property
    def id_monitor(self):
        return self.__id_monitor

    # @id_monitor.setter
    # def id_monitor(self, id_monitor):
    #     self.__id_monitor = id_monitor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio


class DispositivoEentrada:
    def __init__(self, tipo_entrada, marca):
        self.__tipo_entrada = str(tipo_entrada)
        self.__marca = str(marca)

    def __str__(self):
        return f"tipo de entrada: {self.__tipo_entrada}, marca: {self.__marca}"

    @property
    def tipo_entrada(self):
        return self.__tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self.__tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca


class Teclado(DispositivoEentrada):
    contador_raton = 0
    def __init__(self, tipo_entrada, marca):
        Teclado.contador_raton+=1
        self.__id_teclado = Teclado.contador_raton
        super().__init__(tipo_entrada, marca)


    def __str__(self):
        return f"id: {self.__id_teclado}, dispositivo: {super().__str__()}"

    @property
    def id_teclado(self):
        return self.__id_teclado

    @id_teclado.setter
    def id_teclado(self, id_teclado):
        self.__id_teclado = id_teclado


class Raton(DispositivoEentrada):
    contador_peronas = 0
    def __init__(self, tipo_entrada, marca):
        Raton.contador_peronas+=1
        self.__id_raton = Raton.contador_peronas
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f"id: {self.__id_raton}, raton: {super().__str__()}"

    @property
    def id_raton(self):
        return self.__id_raton

    @id_raton.setter
    def id_raton(self, id_raton):
        self.__id_raton = id_raton


class Orden:
    contador_ordenes = 0
    def __init__(self, computadoras):
        Orden.contador_ordenes+=1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = list(computadoras)

    def __add__(self, other):
        return self.__computadoras + other

    def agregar(self, compu):
        self.__computadoras.append(compu)

    def __str__(self):
        return f"""
            id de la orden: {self.__id_orden}
            computadoras: {[[c.__str__()] for c in self.__computadoras]}
        """


if __name__ == '__main__':
    t = Raton("cable", "logitech")
    r = Teclado("cable", "noga")
    m = Monitor("samsung", "24")
    c = Computadora("Pavilion", m, t, r)

    t1 = Raton("cable", "giniatec")
    r1 = Teclado("cable", "electrolux")
    m1 = Monitor("HP", "24")
    c1 = Computadora("Comodore", m1, t1, r1)

    o1 = Orden([c,c1])
    print(o1)
