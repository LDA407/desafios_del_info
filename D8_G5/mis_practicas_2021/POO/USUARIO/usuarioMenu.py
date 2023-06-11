import sys
from usuario import Usuario
from usuarioDao import UsuarioDao


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS\n','*' * 50,'\n What would you like to do today? \n [C]reate user \n [D]elete user \n [U]pdate user \n [S]earch user \n [L]ist user\n','*' * 50)


def create_user():
    UsuarioDao.insert(
        Usuario(
            id_usuario=None,
            username = _get_user_field('username'),
            password = _get_user_field('password')
        ))

def list_users():
    print(UsuarioDao.select())

def update_user(u):
    UsuarioDao.update(
        Usuario(
            username=_get_user_field('username'),
            password=_get_user_field('password'),
            id_usuario=u
        ))

def delete_user(delete_user):
    UsuarioDao.delete(Usuario(id_usuario=delete_user))

def _get_user_id():
    user_id = None
    while not user_id:
        user_id = int(input('What is the user id?'))
    return user_id


def _get_user_field(field_name):
    field = None
    while not field:
        field = input(f'Yuor {field_name}?: ')
    return field


if __name__ == '__main__':
    _print_welcome(); command = input(); command = command.upper()
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