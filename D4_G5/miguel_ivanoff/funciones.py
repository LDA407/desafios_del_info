from datetime import datetime

def calculaPrecio(anio,sup,habit,garaje,sector):
    '''Calcula precio de cada inmueble de acuerdo a características y zona'''         
    parcial=(sup*100+habit*500+verifica_garaje(garaje)*1500)*(1-(antiguedad()-anio)/100)

    if sector.lower()=="a":
        precio=parcial
        return precio
    elif sector.lower()=="b":
        precio=parcial*1.5
        return precio
    elif sector.lower()=='c':
        precio=parcial*2
        return precio
    

def verifica_garaje(garaje):
    ''' Verifica si una propiedad tiene garaje o no
    y asigna valores de 0 o 1 para agregarle o no un valor a la propiedad'''
    val_garaje=0
    if garaje==True:
        val_garaje=1
    return val_garaje


def antiguedad():
    '''Extrae el año de la fecha actual para aplicarlo en la
    determinación de la antiguedad de la propiedad'''
    fecha_actual= datetime.now()
    anio_hoy=fecha_actual.year
    return anio_hoy


def validaParametros(anio,sup,habit,sector,estado):
    '''Hace las validaciones de los datos de cada propiedad ingresados
    a fin de aceptar o no la propiedad ingresada'''
    if anio<2000:
        print('Solo captamos desde el 2000 en adelante.')
        return False
        
    if sup<60:
        print('La superficie debe superar los 60,00 m2.')
        return False
        
    if habit<2:
        print('Debe tener un mínimo de 2 habitaciones.')
        return False
        
    if sector.lower()!="a" and sector.lower()!="b" and sector.lower()!="c":
        print('La propiedad debe pertenecer a los Sectores "A", "B" o "C".')
        return False
        
    if (estado=="Disponible") or (estado=="Reservado") or (estado=="Vendido"):
        return True
        
    else:
        print('La propiedad debe estar Disponible, Reservada o Vendido.')
        return False
    
def extrae_prop(lista):
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


def lista_final(lista,presupuesto):
    '''Obtiene una lista de propiedades cuyos precios son
    menor o igual a un presupuesto ingresado.'''
    listado_final=[]
    cont=-1
    for p in lista:
        if p['precio']<=presupuesto:
            listado_final.append(p)
            
    return listado_final
    