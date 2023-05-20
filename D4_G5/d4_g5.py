import sys
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
        [P] Lista de precios
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
        'garage': ' ',
        'zona': obtener_la_info('zona'),
        'estado': obtener_la_info('estado').capitalize()
    }

    if data['zona'].lower() in 'ab':
        data['garage']=True
    else:
        data['garage']=False

    if validaParametros(data):
        return data
    else:
        return False


def validaParametros(data):

    if int(data['año']) < 2000:
        print('Solo captamos desde el 2000 en adelante.')
        return False
        
    if int(data['metros']) < 60:
        print('La superficie debe superar los 60,00 m2.')
        return False
        
    if int(data['habitaciones']) < 2:
        print('Debe tener un mínimo de 2 habitaciones.')
        return False
        
    if data['zona'].lower() not in 'abc':
        print("La propiedad debe pertenecer a los Sectores 'A', 'B' o 'C'.")
        return False
        
    if data['estado'].lower() in ['disponible', 'reservado', 'vendido']:
        return True
    else:
        print('La propiedad debe estar Disponible, Reservada o Vendido.')
        return False


def listar_los_inmuebles():
    for i in libro:
        print(i)


def actualziar_un_estado(id, nuevo_estado):
    registro = libro[id]
    registro['estado'] = nuevo_estado.capitalize()


def eliminar_un_inmueble(id):
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
    '''Extrae el año de la fecha actual para aplicarlo en la
    determinación de la antiguedad de la propiedad'''
    fecha_actual= datetime.datetime.now()
    anio_hoy=fecha_actual.year
    return anio_hoy


def buscar_por_estado(lista):
    '''Crea una lista de propiedades que tienen un determinado estado y 
    calcula y agrega su precio como elemento.''' 
    prop_encontradas=[]
    contador=-1
    for p in lista:
        if p['estado']=="Disponible" or p['estado']=="Reservado":
            contador+=1
            valor=calculaPrecio(p['año'], p['metros'], p['habitaciones'], p['garage'],p['zona'])
            prop_encontradas.append(p)
            prop_encontradas[contador]['precio']=valor
    return prop_encontradas


def calculaPrecio(anio,sup,habit,garage,sector):
    '''Calcula precio de cada inmueble de acuerdo a características y zona'''         
    parcial=(sup*100+habit*500+buscar_los_que_tengan_garage(garage)*1500)*(1-(antiguedad()-anio)/100)

    if sector.lower()=="a":
        precio=parcial
        return precio
    elif sector.lower()=="b":
        precio=parcial*1.5
        return precio
    elif sector.lower()=='c':
        precio=parcial*2
        return precio
    

def antiguedad():
    '''
        Extrae el año de la fecha actual para aplicarlo en la
        determinación de la antiguedad de la propiedad
    '''
    fecha_actual= datetime.datetime.now()
    anio_hoy=fecha_actual.year
    return anio_hoy


def lista_final(lista,presupuesto):
    '''
        Obtiene una lista de propiedades cuyos precios son
        menor o igual a un presupuesto ingresado.
    '''
    listado_final=[]
    for p in lista:
        if int(p['precio'])<=int(presupuesto):
            listado_final.append(p)
    return listado_final


def buscar_los_que_tengan_garage(garage):
    '''
        Verifica si una propiedad tiene garage o no
        y asigna valores de 0 o 1 para agregarle o no un valor a la propiedad
    '''
    val_garage = 1 if garage==True else 0
    return val_garage


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
            obtener_la_info('nuevo estado')
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


    if comando == 'B':
        monto = obtener_la_info('monto')
        prop_listadas = buscar_por_estado(libro)
        prop_finales = lista_final(prop_listadas,monto)

        for p in prop_finales:
            print(p)
        
        input("<<ENTER>>")
    

    if comando == 'S':
        print('SESION FINALIZADA!!')
        break
