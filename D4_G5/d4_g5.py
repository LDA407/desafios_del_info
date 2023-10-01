from os import system
import datetime

libro = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garage': True, 'zona': 'C', 'estado': 'Disponible'}, 
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garage': False, 'zona': 'B', 'estado': 'Reservado'}, 
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garage': True, 'zona': 'A', 'estado': 'Disponible'}, 
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garage': True, 'zona': 'B', 'estado': 'Vendido'}, 
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garage': False, 'zona': 'C', 'estado': 'Disponible'}
]


def imprimir_la_binvenida():
    print(f'''
        BIENVENIDO
        {'*' * 75}\n
        [I]ngresar nueva propiedad
        [M]odificar estado
        [D]Eliminar una propiedad
        [B]uscar por presupuesto
        [L]istar las propiedades
        [Z] Filtrar por la zona
        [E] Filtrar por el estado
        [S]alir\n
        {'*' * 75}
        '''+
        f'''
        No operamos con inmuebles:\n
        - Anteriores al año 2000. 
        - Menores de 60 metros cuadrados. 
        - Menores de 2 habitaciones.\n
        {'*' * 75}
        '''
    )


def texto_de_ayuda(nombre_del_campo):
    texto_de_ayuda = {
        'id': 'Ingrese el id: ',
        'monto': 'Introdusca tu presupuesto: ',
        'año': 'Año de construcción: ',
        'metros': 'Cantidad de metros cuadrados: ',
        'habitaciones': 'Cantidad de habitacione: ',
        'zona': 'Elija la zona (A, B, C): ',
        'estado': 'Seleccione estado (Disponible, Reservado, Vendido): ',
        'nuevo estado': 'Ingrese el nuevo estado (Disponible-Reservado-Vendido): ',
    }

    return texto_de_ayuda[nombre_del_campo]


def _input(nombre_del_campo):
    valor = None

    while not valor:
        system('cls')
        valor = input(texto_de_ayuda(nombre_del_campo))
    return valor


def comprobar_digito(nombre_del_campo):
    valor = None

    while not valor or not valor.isdigit():
        system('cls')
        print("Solo se admiten numeros enteros")
        valor = input(texto_de_ayuda(nombre_del_campo))
    return valor


def crar_un_inmueble():
    data = {
        'año': int(comprobar_digito('año')),
        'metros': int(comprobar_digito('metros')),
        'habitaciones': int(comprobar_digito('habitaciones')),
        'garage': ' ',
        'zona': _input('zona').upper(),
        'estado': _input('estado').capitalize()
    }
    data['garage'] = True if data['zona'] in 'AB' else False

    if validaParametros(data):
        return data
    else:
        return False


def validaParametros(data):

    if data['año'] < 2000:
        print('Solo captamos desde el 2000 en adelante.')
        return False
        
    if data['metros'] < 60:
        print('La superficie debe superar los 60,00 m2.')
        return False
        
    if data['habitaciones'] < 2:
        print('Debe tener un mínimo de 2 habitaciones.')
        return False
        
    if data['zona'] not in 'ABC':
        print("La propiedad debe pertenecer a los Sectores 'A', 'B' o 'C'.")
        return False
        
    if data['estado'] in 'Disponible, Reservado, Vendido':
        return True
    else:
        print('La propiedad debe estar Disponible, Reservada o Vendido.')
        return False


def listar_los_inmuebles():
    for i in libro:
        print(f"{libro.index(i)}:", i)


def actualziar_un_estado(id, nuevo_estado):
    listar_los_inmuebles()
    registro = libro[id]
    print(registro)

    registro['estado'] = nuevo_estado.capitalize()
    print(registro)


def eliminar_un_inmueble(id):
    listar_los_inmuebles()
    registro = libro[id]
    libro.remove(registro)


def filtrar_por_zona(zona):
    for i in libro:
        if i['zona'] == zona.upper():
            print(i)


def filtrar_por_esatdo(estado):
    for i in libro:
        if i['estado'] == estado.capitalize():
            print(i)


def antiguedad():
    fecha_actual= datetime.datetime.now()
    anio_hoy=fecha_actual.year
    return anio_hoy


def buscar_por_presupuesto(lista):
    def asigna_precios(p):
        p['precio'] = calculaPrecio(
            p['año'],
            p['metros'],
            p['habitaciones'],
            p['garage'],
            p['zona']
        )
        return p
    return [asigna_precios(p) for p in lista]


def calculaPrecio(anio,sup,habit,garage,sector):
    parcial=(
        sup*100 + habit*500 + buscar_los_que_tengan_garage(garage)*1500
    ) * (1-(antiguedad()-anio)//100)

    if sector.lower()=="a":
        precio=parcial
        return precio
    
    elif sector.lower()=="b":
        precio=parcial*1.5
        return precio
    
    elif sector.lower()=='c':
        precio=parcial*2
        return precio


def lista_final(lista, presupuesto):
    listado_final = [i for i in lista if i['precio'] <= int(presupuesto)]
    return listado_final


def buscar_los_que_tengan_garage(garage):
    val_garage = 1 if garage else 0
    return val_garage


while True:
    imprimir_la_binvenida()
    comando = input()
    comando = comando.upper()

    if comando == 'I':
        system("cls")
        ret = crar_un_inmueble()
        if type(ret)==dict:
            libro.append(ret)    
            input('La Propiedad fue Registrada.  <<Presiones ENTER>>')
        else:
            input('<<ENTER>>')

    if comando == 'M':
        system("cls")
        listar_los_inmuebles()
        actualziar_un_estado(
            int(comprobar_digito('id')),
            _input('nuevo estado')
        )
        listar_los_inmuebles()

    if comando == 'D':
        system("cls")
        listar_los_inmuebles()
        eliminar_un_inmueble(int(comprobar_digito('id')))

    if comando == 'Z':
        system("cls")
        filtrar_por_zona(_input('zona'))

    if comando == 'E':
        system("cls")
        filtrar_por_esatdo(_input('estado'))

    if comando == 'L':
        system("cls")
        listar_los_inmuebles()

    if comando == 'B':
        system("cls")
        monto = comprobar_digito('monto')
        prop_listadas = buscar_por_presupuesto(libro)
        prop_finales = lista_final(prop_listadas, monto)

        for p in prop_finales:
            print(p)
        
        input("<<ENTER>>") 

    if comando == 'S':
        system("cls")
        print('SESION FINALIZADA!!')
        break



""""
david lencina
hector larre
miguel ivanoff
martin ismael
nicolas dellama
fernando maciel
miriam fernandez
gomez maria raquel
maria jose gonsalez
"""