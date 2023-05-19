import sys
from fernando_maciel import funcion_de_fernando_para_eliminar
from david_lencina import imprimir_la_bienvenida
#y as con los todos


"""
    ejemplo para nuestro flujo de trabajo:
        from martin_ismael import validador_de_campos

        en la carpeta de ismael
            validador_de_campos(input):
                input = input()

                if input tatata: hace la validación y retorna el valor

        obtener_la_informacion():
            obtiene el valor y lo retorna
            input = validador_de_campos()
            return input
            
"""


def imprimir_la_binvenida():
    print('WELCOME TO PLATZI VENTAS\n','*' * 50,'\n What would you like to do today? \n [C]reate user \n [D]elete user \n [U]pdate user \n [S]earch user \n [L]ist user\n','*' * 50)


def crar_un_inmueble(data):
    pass 


def listar_los_inmuebles():
    pass


def actualziar_un_estado(id, nuevo_estado):
    pass


def eliminar_un_inmueble(le_pasamos_el_id):
    funcion_de_fernando_para_eliminar(le_pasamos_el_id)


def obtener_la_informacion():
    pass


def filtrar_por_zona(zona):
    pass


def filtrar_por_esatdo(estado):
    pass


def validar_el_campo(campo):
    pass


def obtener_el_precio(nose_cuantos_parametros_llevaria_jajaja):
    pass


def eliminar_un_inmueble():
    pass


def obrener_el_id():
    pass




if __name__ == '__main__':
    imprimir_la_binvenida(); command = input(); command = command.upper()
    if command == 'C':
        crar_un_inmueble()
        listar_los_inmuebles()

    if command == 'L':
        listar_los_inmuebles()

    if command == 'D':
        eliminar_un_inmueble(obrener_el_id())
        listar_los_inmuebles()

    if command == 'U':
        usuario_id = obrener_el_id()
        actualziar_un_estado(usuario_id)
        listar_los_inmuebles()
    
    #seria lo mismmo con las otra funciones, para buscar y demas

    print('invalid command'); sys.exit()