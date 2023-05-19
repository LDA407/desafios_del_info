
def agregar():
    libro=[]
    anio=int(input('Año de la Propiedad: '))
    sup=int(input('Metros cuadrados: '))
    habit=int(input('Cant. Habitaciones: '))
    garaje=input('Garaje Si/No : ')
    if garaje.lower()=='si':
        garaje=True
    else:
        garaje=False

    zona=input('Elija la zona (A, B, C): ')
    estado=input('Seleccione estado (Disponible, Reservado, Vendido): ')
   
    if validaParametros(anio,sup,habit,zona,estado):
        propiedad={
            'año':anio,
            'metros': sup,
            'habitaciones': habit,
            'garaje': garaje,
            'zona': zona.upper(),
            'estado': estado
        }
        #libro.append(propiedad)
        return propiedad
    else:
        return False
    


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