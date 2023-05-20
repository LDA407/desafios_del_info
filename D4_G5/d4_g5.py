import sys

libro = []

def imprimir_la_binvenida():
    print(f"""
        BIENVENIDO
        {'*' * 75}\n
        [I]ngresar nueva propiedad
        [M]odificar estado
        [D]Eliminar una propiedad
        [B]uscar por presupuesto
        [L]istar las propiedades
        [S]alir\n
        {'*' * 75}
        """
    )


def crar_un_inmueble(data):
    def agregar():
        anio=int(input('Año de la Propiedad: '))
        sup=int(input('Metros cuadrados: '))
        habit=int(input('Cant. Habitaciones: '))
        garaje= input('Garaje Si/No : ')

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
            
            return propiedad
        else:
            return False
        
    agregar()

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


def listar_los_inmuebles():
    print([ 
            {
                'año': i[0],
                'metros': i[1],
                'habitaciones': i[2],
                'garaje': i[3],
                'zona': i[4],
                'estado': i[5]
            }
            for i in libro
        ])


def actualziar_un_estado(id, nuevo_estado):
    registro = libro[id]
    registro.estado = nuevo_estado


#===== Hector larre ======
def eliminar_un_inmueble(id):
    "en este caso no es necesario agregar ids sino el indice"
    def eliminar_inmueble(id):
        for inmueble in inmuebles:
            if inmueble[id] == id:
                inmuebles.remove(inmueble)

    eliminar_inmueble(id)



def filtrar_por_zona(zona):
    print([ 
            {
                'año': i[0],
                'metros': i[1],
                'habitaciones': i[2],
                'garaje': i[3],
                'zona': i[4],
                'estado': i[5]
            }
            for i in libro if i[f"{zona}"] == zona
        ])


def filtrar_por_esatdo(estado):
    print([ 
            {
                'año': i[0],
                'metros': i[1],
                'habitaciones': i[2],
                'garaje': i[3],
                'zona': i[4],
                'estado': i[5]
            }
            for i in libro if i[f"{estado}"] == estado
        ])


def validar_el_campo(campo):



def obtener_el_precio(id):
    registro = libro[id]
    def calcular_precio(id):
        antiguedad = int(input("Introdusca la antiguedad en años: "))
        precio = 0

        if registro["zona"] == 'A':
            precio = registro["metros" * 100 + "habitaciones" * 500 + "garage" * 1500] * (1 - antiguedad / 100)
        
        elif registro["zona"] == 'B':
            precio = registro["metros" * 100 + "habitaciones" * 500 + "garage" * 1500] * (1 - antiguedad / 100) * 1.5
        
        elif registro["zona"] == 'C':
            precio = registro["metros" * 100 + "habitaciones" * 500 + "garage" * 1500] * (1 - antiguedad / 100) * 2
        
        return precio
    
    calcular_precio(id)


def eliminar_un_inmueble(id):
    def eliminar_inmueble(id):
        for inmueble in inmuebles:
            if inmueble["id"] == id:
                inmuebles.remove(inmueble)

    eliminar_inmueble(id)


def obrener_el_id():
    id = input('Ingrese el id: ')
    return id




while True:
    if __name__ == '__main__':
        imprimir_la_binvenida()
        comando = input()
        comando = comando.upper()

        if comando == 'I':
            ret=ingresar.agregar()
            if type(ret)==dict:
                libro.append(ret)    
                input('La Propiedad fue Registrada.  <<Presiones ENTER>>')
            else:
                input('<<ENTER>>')
        
        if comando == 'M':
            id = obrener_el_id()
            nuevo_estado= input('Ingrese el nuevo estado (Disponible-Reservado-Vendido): ')
            actualziar_un_estado(id, nuevo_estado)


        if comando == 'D':
            listar_los_inmuebles()
            id = obrener_el_id()
            eliminar_un_inmueble(id)


        if comando == 'B':
            monto=int(input('\tIngrese su presupuesto: '))
            prop_listadas=buscar_por_estado(libro)
            prop_finales=lista_final(prop_listadas,monto)

            for p in prop_finales:
                print(p)
            input("<<ENTER>>")

    print('invalid command'); sys.exit()