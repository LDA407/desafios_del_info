import sys
import datetime

libro = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'}, 
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]


def imprimir_la_binvenida():
    print(f"""
        BIENVENIDO
        {'*' * 75}\n
        [I]ngresar nueva propiedad
        [M]odificar estado
        [D]Eliminar una propiedad
        [B]uscar por presupuesto
        [L]istar las propiedades
        [P] Lista de precios
        [Z] Filtrar por la zona
        [E] Filtrar por el estado
        [C]calcular el precio
        [S]alir\n
        {'*' * 75}
        """
    )


def texto_de_ayuda(nombre_del_campo):
    texto_de_ayuda = {
        'id': 'Ingrese el id: ',
        'año': "Año de construcción: ",
        'metros': "Cantidad de metros cuadrados: ",
        'habitaciones': "Cantidad de habitacione: ",
        'garage': "Tiene garage, op[True, False]: ",
        'zona': 'Elija la zona (A, B, C): ',
        'estado': 'Seleccione estado (Disponible, Reservado, Vendido): ',
        'nuevo_estado': 'Ingrese el nuevo estado (Disponible-Reservado-Vendido): ',
    }

    return texto_de_ayuda[nombre_del_campo]


def obtener_la_info(nombre_del_campo):
    valor = None
    while not valor:
        valor = input(texto_de_ayuda(nombre_del_campo))
    return valor


def crar_un_inmueble():
    data = {
        'año': obtener_la_info('año'),
        'metros': obtener_la_info('metros'),
        'habitaciones': obtener_la_info('habitaciones'),
        'garage': obtener_la_info('garage'),
        'zona': obtener_la_info('zona'),
        'estado': obtener_la_info('estado')
    }

    if data["garage"].lower()=='si':
        data["garage"]=True
    else:
        data["garage"]=False

    if validaParametros(data):
        return data
    else:
        return False


def validaParametros(data):
    '''Hace las validaciones de los datos de cada propiedad ingresados
        a fin de aceptar o no la propiedad ingresada'''

    if int(data["año"]) < 2000:
        print('Solo captamos desde el 2000 en adelante.')
        return False
        
    if int(data["metros"]) < 60:
        print('La superficie debe superar los 60,00 m2.')
        return False
        
    if int(data["habitaciones"]) < 2:
        print('Debe tener un mínimo de 2 habitaciones.')
        return False
        
    if data["zona"].lower() != "a" and data["zona"].lower()!="b" and data["zona"].lower()!="c":
        print('La propiedad debe pertenecer a los Sectores "A", "B" o "C".')
        return False
        
    if (data["estado"].lower() == "disponible") or (data["estado"].lower() == "reservado") or (data["estado"].lower() == "vendido"):
        return True
        
    else:
        print('La propiedad debe estar Disponible, Reservada o Vendido.')
        return False


def listar_los_inmuebles():
    print([ i for i in libro ])


def actualziar_un_estado(id, nuevo_estado):
    registro = libro[id]
    registro["estado"] = nuevo_estado


def eliminar_un_inmueble(id):
    registro = libro[id]
    libro.remove(registro)


def filtrar_por_zona(zona):
    print([ i for i in libro if i["zona"] == zona.upper() ])


def filtrar_por_esatdo(estado):
    print([ i for i in libro if i["estado"] == estado.upper() ])

def antiguedad():
    '''Extrae el año de la fecha actual para aplicarlo en la
    determinación de la antiguedad de la propiedad'''
    fecha_actual= datetime.datetime.now()
    anio_hoy=fecha_actual.year
    return anio_hoy

def calcular_precio(id):
    antiguedad = int(input("Introdusca la antiguedad en años: "))
    registro = libro[id] if libro[id] and libro["año"] == antiguedad else "no hay registros"

    precio = 0  

    if registro["zona"] == 'A':
        precio = (
            registro["metros"] * 100 + registro["habitaciones"] * 500 + registro["garage"] * 1500) * (1-(antiguedad()-registro["año"] )/100)
    
    elif registro["zona"] == 'B':
        precio = (
            registro["metros"] * 100 + registro["habitaciones"] * 500 + registro["garage"] * 1500) * (1-(antiguedad()-registro["año"] )/100) * 1.5
    
    elif registro["zona"] == 'C':
        precio = (
            registro["metros"] * 100 + registro["habitaciones"] * 500 + registro["garage"] * 1500) * (1-(antiguedad()-registro["año"] )/100) * 2
    
    return precio


while True:
    imprimir_la_binvenida()
    comando = input()
    comando = comando.upper()

    if comando == 'I':
        ret = crar_un_inmueble()
        if type(ret)==dict:
            libro.append(ret)    
            input('La Propiedad fue Registrada.  <<Presiones ENTER>>')
        else:
            input('<<ENTER>>')


    if comando == 'M':
        actualziar_un_estado(
            int(obtener_la_info('id')),
            obtener_la_info('nuevo_estado')
        )
        listar_los_inmuebles()


    if comando == 'D':
        listar_los_inmuebles()
        eliminar_un_inmueble(int(obtener_la_info('id')))


    # if comando == 'B':
    #     filtrar_por_esatdo(obtener_la_info('estado'))


    if comando == 'Z':
        filtrar_por_zona(obtener_la_info('zona'))
    

    if comando == 'E':
        filtrar_por_esatdo(obtener_la_info('estado'))
    

    if comando == 'L':
        listar_los_inmuebles()


    if comando == 'P':
        calcular_precio(int(obtener_la_info('id')))
