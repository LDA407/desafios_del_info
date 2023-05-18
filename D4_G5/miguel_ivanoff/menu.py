from os import system

def encabezado():
    system('cls')

    print('==================================================================')
    print('                       Gestión Inmobiliaria')
    print('==================================================================')

def verMenu():
    print('\n\t Menu general')
    print('1. Ingresar nueva propiedad.')
    print('2. Modificar Estado de la Propiedad.')
    print('3. Eliminar una Propiedad.')
    print('4. Buscar por Monto.')
    print('5. Salir de la Aplicación.\n')
    opcion=int(input("Ingrese su opción: "))

    if opcion>0 and opcion<5:
         return opcion
    else:
        return 5

