

inmuebles = [
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

def agregar_inmueble(inmueble):
    inmuebles.append(inmueble)

def editar_inmueble(id, campo, valor):
    for inmueble in inmuebles:
        if inmueble["id"] == id:
            inmueble[campo] = valor

def eliminar_inmueble(id):
    for inmueble in inmuebles:
        if inmueble["id"] == id:
            inmuebles.remove(inmueble)

def buscar_inmuebles(precio_maximo):
    resultado = []
    for inmueble in inmuebles:
        if (inmueble["precio"] <= precio_maximo) and (inmueble["estado"] == 'Disponible' or inmueble["estado"] == 'Reservado'):
            resultado.append(inmueble)
            inmueble["PRECIO"] = calcular_precio(inmueble)
    return resultado

def calcular_precio(inmueble):
    # Cálculo del precio según la zona
    precio = 0
    if inmueble["zona"] == 'A':
        precio = inmueble["metros" * 100 + "habitaciones" * 500 + "garage" * 1500] * 
    elif inmueble["zona"] == 'B':
        precio = inmueble["metros" * 100 + "habitaciones" * 500 + "garage" * 1500] *
    elif inmueble["zona"] == 'C':
        precio = inmueble["metros" * 100 + "habitaciones" * 500 + "garage" * 1500] *
    return precio

