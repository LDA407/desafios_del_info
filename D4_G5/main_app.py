import sys
from usuario import Usuario
from usuarioDao import UsuarioDao

"""
    import de ejemplo:
        from martin_ismael import validador_de_campos

        en la carpeta de ismael
            validador_de_campos(input):
                input = input()

                if inpu tatata: hace la validacio y retorna el varlor

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


def eliminar_un_inmueble(delete_user):
    pass


def obtener_la_informacion():
    pass


def filtrar_por_zona(zona):
    pass


def filtrar_por_esatdo(estado):
    pass


def validar_el_campo(campo):
    pass


def obtener_el_precio():
    pass




if __name__ == '__main__':
    imprimir_la_binvenida(); command = input(); command = command.upper()
    if command == 'C':
        create_user()
        list_users()
    if command == 'L':
        list_users()
    if command == 'D':
        delete_user(_get_user_id())
        list_users()
    if command == 'U':
        usuario_id = _get_user_id()
        update_user(usuario_id)
        list_users()

    print('invalid command'); sys.exit()