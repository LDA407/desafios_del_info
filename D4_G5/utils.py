def help_text(field_name):
    return f"{field_name}"


def validate_fields(field_name):
    field_value = input(help_text(field_name)) 

    if field_name == 'año' and int(field_value) < 2000:
        print("No se acceptan inmuebles anteriores al año 2000")
        return None
    
    if field_name == 'metros' and int(field_value) < 60:
        print("No se acceptan inmuebles de menos 60 metros cuadrados")
        return None
    
    if field_name == 'habitaciones' and int(field_value) < 2:
        print("No se acceptan inmuebles con menos de 2 habitacione")
        return None

    return field_value