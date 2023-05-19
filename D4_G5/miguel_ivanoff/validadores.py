def texto_de_ayuda(nombre_del_campo):
    texto_de_ayuda = {
        'año': "Año de construcción: ",
        'metros': "Cantidad de metros cuadrados: ",
        'habitaciones': "Cantidad de habitacione: ",
        'garage': "Tiene garage, op[True, False]: ",
        'zona': "Ubicación, op['A', 'B', 'C']: ",
        'estado': "Disponibilidad, op['Disponible', 'Reservado', 'Vendido']: "
    }

    return texto_de_ayuda[nombre_del_campo]


def validar_campos(nombre_del_campo):
    valor = input(texto_de_ayuda(nombre_del_campo)) 

    if nombre_del_campo == 'año' and int(valor) < 2000:
        print("No se acceptan inmuebles anteriores al año 2000")
        return None
    
    if nombre_del_campo == 'metros' and int(valor) < 60:
        print("No se acceptan inmuebles de menos 60 metros cuadrados")
        return None
    
    if nombre_del_campo == 'habitaciones' and int(valor) < 2:
        print("No se acceptan inmuebles con menos de 2 habitacione")
        return None

    return valor