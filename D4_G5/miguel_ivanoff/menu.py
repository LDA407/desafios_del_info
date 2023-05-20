from .models.inmobiliario import Inmueble
from .validadores import validar_campos
from .ingresar import agregar, validaParametros
import datetime

libro = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'}, 
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


def bienvenida():
    print(f"""
        BIENVENIDO
        {'*' * 75}\n
        [I]ngresar nueva propiedad
        [M]odificar estado
        [D]Eliminar una propiedad
        [B]uscar por presupuesto
        [C]rear una propiedad
        [S]alir\n
        {'*' * 75}
        """
    )


def crear_inmueble(data):
    libro.append(Inmueble(**data))
    mostrar_los_registros()


def eliminar_inmueble():
    mostrar_los_registros()
    prop=int(input("Seleccione la propiedad a Eliminar: "))
    op=input('Está seguro de Eliminar? S/N - ').lower()
    if op=="s":
        del libro[prop]
        print('\tSe ha eliminado la propiedad.')
        input('<<Presiones ENTER>>')


def mostrar_los_registros():
    '''Lista y enumera los registros sin asignarle un campo id.'''
    contador=-1
    for p in libro:
        contador+=1
        print(f"{contador}- Propiedad de {p['metros']}m2, de zona: {p['zona']}, y estado: {p['estado']}.")


def buscar_por_estado(lista):
    '''Crea una lista de propiedades que tienen un determinado estado y 
    calcula y agrega su precio como elemento.''' 
    prop_encontradas=[]
    contador=-1
    for p in lista:
        if p['estado']=="Disponible" or p['estado']=="Reservado":
            contador+=1
            valor=calculaPrecio(p['año'], p['metros'], p['habitaciones'], p['garaje'],p['zona'])
            prop_encontradas.append(p)
            prop_encontradas[contador]['precio']=valor
    return prop_encontradas


def calculaPrecio(anio,sup,habit,garaje,sector):
    '''Calcula precio de cada inmueble de acuerdo a características y zona'''         
    parcial=(sup*100+habit*500+buscar_los_que_tengan_garage(garaje)*1500)*(1-(antiguedad()-anio)/100)

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
    '''Extrae el año de la fecha actual para aplicarlo en la
    determinación de la antiguedad de la propiedad'''
    fecha_actual= datetime.datetime.now()
    anio_hoy=fecha_actual.year
    return anio_hoy


def lista_final(lista,presupuesto):
    '''Obtiene una lista de propiedades cuyos precios son
    menor o igual a un presupuesto ingresado.'''
    listado_final=[]
    for p in lista:
        if p['precio']<=presupuesto:
            listado_final.append(p)
    return listado_final


def buscar_por_zona(zona):
    print([i.__dict__ for i in libro if i.zona == zona])


def buscar_los_que_tengan_garage(garage):
    ''' Verifica si una propiedad tiene garaje o no
    y asigna valores de 0 o 1 para agregarle o no un valor a la propiedad'''
    val_garaje=0
    if garage==True:
        val_garaje=1
    return val_garaje


def modificar_el_estado(nuevo_estado):
    mostrar_los_registros()
    prop=int(input("Seleccione la propiedad a cambiar el estado:"))
    op=input('Está seguro de cambiar de estado? S/N - ').lower()
    if op=="s":
        libro[prop]['estado']=nuevo_estado
        print('Se ha modificado correctamente el estado de la propiedad.')
        print(libro[prop])
        input('<<Presiones ENTER>>')


def obtener_la_info(nombre_del_campo):
    valor = None
    while not valor:
        valor = validar_campos(nombre_del_campo)
    return valor


while True:
    if __name__ == '__main__':
        bienvenida()
        comando = input()
        comando = comando.upper()


        if comando == 'S':
            print('SESION FINALIZADA!!')
            break

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
        
        if comando == 'I':
            ret=ingresar.agregar()
            if type(ret)==dict:
                libro.append(ret)    
                input('La Propiedad fue Registrada.  <<Presiones ENTER>>')
            else:
                input('<<ENTER>>')
        
        if comando == 'M':
            nuevo_estado=input('Ingrese el nuevo estado (Disponible-Reservado-Vendido): ')
            modificar_el_estado(nuevo_estado)

        if comando == 'D':
            eliminar_inmueble()

        if comando == 'B':
            monto=int(input('\tIngrese su presupuesto: '))
            prop_listadas=buscar_por_estado(libro)
            prop_finales=lista_final(prop_listadas,monto)
            for p in prop_finales:
                print(p)
            input("<<ENTER>>")

