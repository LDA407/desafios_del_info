from datetime import datetime

def calculaPrecio(anio,sup,habit,garaje,sector):
    fecha_actual= datetime.now()
    anio_hoy=fecha_actual.year
    parcial=(sup*100+habit*500+garaje*1500)*(1-(anio_hoy-anio)/100)
    if sector.lower()=="a":
        precio=parcial
        return precio
    elif sector.lower()=="b":
        precio=parcial*1.5
        return precio
    elif sector.lower()=='c':
        precio=parcial*2
        return precio
    
    
def validaParametros(anio,sup,habit,sector,estado):
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
    
