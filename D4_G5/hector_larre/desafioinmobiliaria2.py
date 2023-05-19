def calcular_precio(metros, habitaciones, garaje, antiguedad, zona):
    if zona == "A":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == "B":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == "C":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    return precio

def agregar_inmueble(lista_inmuebles):
    inmueble = {}
    inmueble['año'] = int(input("Introduce el año del inmueble: "))
    inmueble['metros'] = int(input("Introduce los metros cuadrados del inmueble: "))
    inmueble['habitaciones'] = int(input("Introduce el número de habitaciones: "))
    inmueble['garaje'] = bool(int(input("¿Tiene garaje? Introduce 1 si sí y 0 si no: ")))
    inmueble['zona'] = input("Introduce la zona del inmueble (A, B o C): ")
    inmueble['estado'] = input("Introduce el estado del inmueble (Disponible, Reservado o Vendido): ")
    
    if validar_inmueble(inmueble):
        lista_inmuebles.append(inmueble)
        print("Inmueble agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def editar_inmueble(lista_inmuebles):
    indice = int(input("Introduce el índice del inmueble que quieres editar: "))
    
    if indice >= len(lista_inmuebles):
        print("El índice es inválido.")
        return
    
    inmueble = lista_inmuebles[indice]
    
    print("Inmueble seleccionado:")
    print(inmueble)
    
    opcion = input("¿Qué campo quieres editar? ")
    
    if opcion not in inmueble:
        print("La opción es inválida.")
        return
    
    valor = input(f"Introduce el nuevo valor para {opcion}: ")
    
    if opcion == 'garaje':
        valor = bool(int(valor))
        
    inmueble[opcion] = valor
    
    if validar_inmueble(inmueble):
        print("Inmueble editado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def eliminar_inmueble(lista_inmuebles):
    indice = int(input("Introduce el índice del inmueble que quieres eliminar: "))
    
    if indice >= len(lista_inmuebles):
        print("El índice es inválido.")
        return
    
    lista_inmuebles.pop(indice)
    
    print("Inmueble eliminado correctamente.")

def cambiar_estado(lista_inmuebles):
    indice = int(input("Introduce el índice del inmueble que quieres cambiar de estado: "))
    
    if indice >= len(lista_inmuebles):
        print("El índice es inválido.")
        return
    
    estado_actual = lista_inmuebles[indice]['estado']
    
    print(f"Estado actual del inmueble: {estado_actual}")
    
    nuevo_estado = input("Introduce el nuevo estado del inmueble (Disponible, Reservado o Vendido): ")
    
    if nuevo_estado not in ['Disponible', 'Reservado', 'Vendido']:
        print("El estado es inválido.")
        return
    
    lista_inmuebles[indice]['estado'] = nuevo_estado
    
    print(f"Estado del inmueble cambiado de {estado_actual} a {nuevo_estado}.")

def buscar_inmuebles(lista_inmuebles, presupuesto):
    resultados_busqueda = []
    
    for i, inm in enumerate(lista_inmuebles):
        if validar_inmueble(inm) and calcular_precio(inm['metros'], inm['habitaciones'],)
