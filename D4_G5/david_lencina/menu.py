from models.inmobiliario import Inmueble
from validadores import validar_campos

libro = []


def bienvenida():
    print(f"""
        BIENVENIDO
        {'*' * 50}\n
        [C]reate user
        [D]elete user
        [U]pdate user
        [S]earch user
        [L]ist user\n
        {'*' * 50}
        """
    )


def crear_inmueble(data):
    libro.append(Inmueble(**data))
    mostrar_los_registros()


def mostrar_los_registros():
    print([i.__dict__ for i in libro])


def buscar_por_estado(estado):
    print([i.__dict__ for i in libro if i.estado == estado])


def buscar_por_zona(zona):
    print([i.__dict__ for i in libro if i.zona == zona])


def buscar_los_que_tengan_garage(garage):
    print([i.__dict__ for i in libro if i.garage == garage])


def modificar_el_estado(id, nuevo_estado):
    pass


def obtener_la_info(nombre_del_campo):
    valor = None
    while not valor:
        valor = validar_campos(nombre_del_campo)
    return valor


if __name__ == '__main__':
    bienvenida()
    comando = input()
    comando = comando.upper()


    if comando == 'C':
        data = {
            'año': obtener_la_info('año'),
            'metros': obtener_la_info('metros'),
            'habitaciones': obtener_la_info('habitaciones'),
            'garage': obtener_la_info('garage'),
            'zona': obtener_la_info('zona'),
            'estado': obtener_la_info('estado')
        }
        crear_inmueble(data)
    
    p1 = Inmueble(año=2010, metros=255, habitaciones=6, garage=True, zona="A", estado="Disponible")
    p2 = Inmueble(año=2000, metros=40, habitaciones=3, garage=False, zona="B", estado="Disponible")
    libro.append(p1)
    libro.append(p2)
    mostrar_los_registros()
    print("\nubicacion?")
    buscar_por_zona("A")
    print("\nesta disponible?")
    buscar_por_estado("Disponible")
    print("\ntiene garage?")
    buscar_los_que_tengan_garage(False)