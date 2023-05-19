def agregar_casa(lista_casas, casas):
    if verificacion_casa(casas):
        lista_casas.append(casas)
        print(f"La casa {casas} se agrego correctamente")
    else:
        print(f"Error al agregar la casa: {casas}, verifique los datos.")

def suprimir_casa(lista_casas, serie):
    if serie < len(lista_casas):
        del lista_casas[serie]

        print("Se  elimino de manera correcta la casa.")
    else:
        print("Hubo un error al querer eliminar la casa.")

def modificar_casa(lista_casas, serie, nueva_casa):
    if verificacion_casa(nueva_casa):
        lista_casas[serie] = nueva_casa
        print(f"La casa {nueva_casa} se agrego correctamente a la lista.")
    else:
        print(f"Se detectaron errores al querer agregar la nueva casa: {nueva_casa} a la lista.")

