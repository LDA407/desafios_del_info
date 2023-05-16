from models.inmobiliario import Inmueble
from models.libroInmobiliario import LibroDeRegistros
from utils import validate_fields

libro = LibroDeRegistros()


def crear_inmueble(data):
    libro.agregar(Inmueble(**data))
    print(libro)


def get_client_info(field_name):
    field_value = None
    
    while not field_value:
        field_value = validate_fields(field_name)

    return field_value


if __name__ == '__main__':
    command = input()
    command = command.upper()

    if command == 'C':
        data = {
            'año': get_client_info('año'),
            'metros': get_client_info('metros'),
            'habitaciones': get_client_info('habitaciones'),
            'garage': get_client_info('garage'),
            'zona': get_client_info('zona'),
            'estado': get_client_info('estado')
        }
        crear_inmueble(data)
