lista_inmuebles = [
    {
        "año" : 2010,
        "metros" : 150,
        "habitaciones" : 4,
        "garage" : True,
        "zona" : "C",
        "estado" : "Disponible",
    },
    {
        "año" : 2016,
        "metros" : 80,
        "habitaciones" : 2,
        "garage" : False,
        "zona" : "B",
        "estado" : "Reservado",
    },
    {
        "año" : 2000,
        "metros" : 180,
        "habitaciones" : 4,
        "garage" : True,
        "zona" : "A",
        "estado" : "Disponible",
    },
    {
        "año" : 2015,
        "metros" : 95,
        "habitaciones" : 3,
        "garage" : True,
        "zona" : "B",
        "estado" : "Vendido",
    },
    {
        "año" : 2008,
        "metros" : 60,
        "habitaciones" : 2,
        "garage" : False,
        "zona" : "C",
        "estado" : "Disponible",
    },
]


metros = int(input("Ingrese los metros cuadrados del inmueble: "))

habitaciones = int(input("Introdusca el numero de habitaciones: "))

garage = int(input("¿Tiene garage? Introdusca 1 si es si, 0 si es no: "))

antiguedad = int(input("Introdusca la antiguedad en años: "))

zona = input("Introduce la zona del inmueble A, B, o C: ")



def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble["año"]
    if inmueble["zona"] == "A":
        precio = (inmueble["metros"] * 100 + inmueble["habitaciones"] * 500 + inmueble["garage"] * 1500) * (1 - antiguedad/100)
    elif inmueble["zona"] == "B":
        precio = (inmueble["metros"] * 100 + inmueble["habitaciones"] * 500 + inmueble["garage"] * 1500) * (1 - antiguedad/100) * 1.5
    elif inmueble["zona"] == "C":
        precio = (inmueble["metros"] * 100 + inmueble["habitaciones"] * 500 + inmueble["garage"] * 1500) * (1 - antiguedad/100) * 2
    return precio

def agregar_inmueble(lista_inmuebles, nuevo_inmueble):
    if nuevo_inmueble["zona"] not in ["A", "B", "C"]:
        print("Error: La zona del nuevo inmueble no es válida.")
        return lista_inmuebles
    elif nuevo_inmueble["año"] < 2000:
        print("Error: El año del nuevo inmueble es anterior a 2000.")
        return lista_inmuebles
    elif nuevo_inmueble["metros"] < 60:
        print("Error: El nuevo inmueble tiene menos de 60 metros cuadrados.")
        return lista_inmuebles
    elif nuevo_inmueble["habitaciones"] < 2:
        print("Error: El nuevo inmueble tiene menos de 2 habitaciones.")
        return lista_inmuebles
    elif nuevo_inmueble["estado"] not in ["Disponible", "Reservado", "Vendido"]:
        print("Error: El estado del nuevo inmueble no es válido.")
        return lista_inmuebles
    else:
        lista_inmuebles.append(nuevo_inmueble)
        print("El nuevo inmueble ha sido agregado a la lista.")
        return lista_inmuebles

def editar_inmueble(lista_inmuebles, indice, nueva_info):
    if nueva_info.get("zona") not in ["A", "B", "C"]:
        print("Error: La zona del nuevo inmueble no es válida.")
        return lista_inmuebles
    elif nueva_info.get("año") and nueva_info.get("año") < 2000:
        print("Error: El año del nuevo inmueble es anterior a 2000.")
        return lista_inmuebles
    elif nueva_info.get("metros") and nueva_info.get("metros") < 60:
        print("Error: El nuevo inmueble tiene menos de 60 metros cuadrados.")
        return lista_inmuebles
    elif nueva_info.get("habitaciones") and nueva_info.get("habitaciones") < 2:
        print("Error: El nuevo inmueble tiene menos de 2 habitaciones.")
        return lista_inmuebles
    elif nueva_info.get("estado") and nueva_info.get("estado") not in ["Disponible", "Reservado", "Vendido"]:
        print("Error: El estado del nuevo inmueble no es válido.")
        return lista_inmuebles
    else:
        for clave, valor in nueva_info.items():
            if valor is not None:
                lista_inmuebles[indice][clave] = valor
        print(f"El inmuble {indice} ha sido actualizado con éxito.")
        return lista_inmuebles

def eliminar_inmueble(lista_inmuebles, indice):
    del lista_inmuebles[indice]
    print(f"El inmueble {indice} ha sido eliminado")