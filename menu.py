from models.inmobiliario import Inmueble
from models.libroInmobiliario import LibroDeRegistros
from utils import validate_fields

def crear_inmueble(client):
    if client:
        libro = LibroDeRegistros()
        libro.agregar(Inmueble(**client))
        print(libro)
    else:
        print('Client already exists')


def get_client_info(field_name):
    field_value = None
    
    while not field_value:
        field_value = validate_fields(field_name)

    return field_value


if __name__ == '__main__':
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'año': get_client_info('año'),
            'metros': get_client_info('metros'),
            'habitaciones': get_client_info('habitaciones'),
            'garage': get_client_info('garage'),
            'zona': get_client_info('zona'),
            'estado': get_client_info('estado')
        }
        crear_inmueble(client)
