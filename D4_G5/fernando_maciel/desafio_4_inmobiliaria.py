def agregar_inmueble(lista):
    inmueble = {}
    inmueble['año'] = int(input("Año: "))
    inmueble['metros'] = int(input("Metros cuadrados: "))
    inmueble['habitaciones'] = int(input("Número de habitaciones: "))
    inmueble['garaje'] = bool(input("¿Tiene garaje? (True/False): "))
    inmueble['zona'] = input("Zona (A, B, C): ").upper()
    inmueble['estado'] = input("Estado (Disponible, Reservado, Vendido): ").capitalize()

    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("Inmueble agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    return True


def editar_inmueble(lista):
    indice = int(input("Índice del inmueble a editar: "))
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        inmueble_backup = dict(inmueble)
        print(inmueble)
        print(inmueble_backup)
        print("Editar inmueble:")
        print("1. Año (", inmueble['año'], ")")
        print("2. Metros cuadrados (", inmueble['metros'], ")")
        print("3. Número de habitaciones (", inmueble['habitaciones'], ")")
        print("4. Garaje (", inmueble['garaje'], ")")
        print("5. Zona (", inmueble['zona'], ")")
        print("6. Estado (", inmueble['estado'], ")")
        opcion = int(input("Opción a editar: "))
        if opcion == 1:
            inmueble['año'] = int(input("Nuevo año: "))
        elif opcion == 2:
            inmueble['metros'] = int(input("Nuevos metros cuadrados: "))
        elif opcion == 3:
            inmueble['habitaciones'] = int(input("Nuevo número de habitaciones: "))
        elif opcion == 4:
            inmueble['garaje'] = bool(input("¿Tiene garaje? (True/False): "))
        elif opcion == 5:
            inmueble['zona'] = input("Nueva zona (A, B, C): ").upper()
        elif opcion == 6:
            inmueble['estado'] = input("Nuevo estado (Disponible, Reservado, Vendido): ").capitalize()
        else:
            print("Opción inválida.")
            
        if validar_inmueble(inmueble):
            print("Inmueble editado correctamente.")
        else:
            deshacer_cambios(inmueble, inmueble_backup)
            print("El inmueble no cumple con las reglas de validación.")
    else:
        print("Índice inválido")

def deshacer_cambios(inmueble, inmueble_backup):
    # Deshacer cambios asignando valores anteriores
    inmueble['año'] = inmueble_backup['año']
    inmueble['metros'] = inmueble_backup['metros']
    inmueble['habitaciones'] = inmueble_backup['habitaciones']
    inmueble['garaje'] = inmueble_backup['garaje']
    inmueble['zona'] = inmueble_backup['zona']
    inmueble['estado'] = inmueble_backup['estado']

def listar_inmuebles(lista):
    for elemento in lista:
        print(elemento)


def eliminar_inmueble(lista):
    indice = int(input("Índice del inmueble a eliminar: "))
    if indice >= 0 and indice < len(lista):
        del lista[indice]
        print("Inmueble eliminado correctamente.")
    else:
        print("Índice inválido.")


def cambiar_estado_inmueble(lista):
    indice = int(input("Índice del inmueble a cambiar de estado: "))
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        print("Estado actual:", inmueble['estado'])
        nuevo_estado = input("Nuevo estado (Disponible, Reservado, Vendido): ").capitalize()
        inmueble['estado'] = nuevo_estado
        print("Estado cambiado correctamente.")
    else:
        print("Índice inválido.")


def buscar_inmuebles_por_presupuesto(lista):
    presupuesto = float(input("Presupuesto máximo: "))
    resultados = []
    for inmueble in lista:
        if inmueble['estado'] in ['Disponible', 'Reservado']:
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio['precio'] = precio
                resultados.append(inmueble_con_precio)
    return resultados


def calcular_precio(inmueble):
    base = inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500
    antiguedad = 2023 - inmueble['año']
    if inmueble['zona'] == 'A':
        precio = base * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = base * (1 - antiguedad / 100) * 1.5
    else:
        precio = base * (1 - antiguedad / 100) * 2
    return precio


# Lista inicial de inmuebles
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
             {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
             {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
             {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
             {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar inmueble")
        print("2. Editar inmueble")
        print("3. Eliminar inmueble")
        print("4. Cambiar estado de inmueble")
        print("5. Buscar inmuebles por presupuesto")
        print("6. Listar inmuebles")
        print("7. Salir")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_inmueble(inmuebles)
        elif opcion == 2:
            editar_inmueble(inmuebles)
        elif opcion == 3:
            eliminar_inmueble(inmuebles)
        elif opcion == 4:
            cambiar_estado_inmueble(inmuebles)
        elif opcion == 5:
            resultados = buscar_inmuebles_por_presupuesto(inmuebles)
            print("\nResultados de búsqueda:")
            if len(resultados) > 0:
                for inmueble in resultados:
                    print(inmueble)
            else:
                print('No se encontraron resultados para su búsqueda.')
        elif opcion == 6:
            listar_inmuebles(inmuebles)
        elif opcion == 7:
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el menú principal
menu()
