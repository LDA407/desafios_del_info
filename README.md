# Desafío 8: Principios de programación orientada a objetos
## Requisitos técnicos:
    - Herencia
    - Encapsulamiento

## Crear las siguientes clases con sus atributos y métodos.
```python
class Usuario:

    def __init__(self):
        self.id
        self.nombre
        self.apellido
        self.teléfono
        self.username
        self.email
        self.contraseña
        self.fecha_de_registro
        self.avatar
        self.estado

    def __str__(self):
        return self.name
    
    def login(self):
        return self.name
    
    def registrar(self):
        return self.name


class Publico(Usuario):

    def __init__(self):
        self.es_publico
    
    def registrar():
        pass
    
    def comentar():
        pass


class Colaborador(Usuario)
    def __init__(self):
        self.es_colaborador
    
    def registrar():
        pass
    
    def comentar():
        pass
    
    def publicar():
        pass


class Articulo:
    def __init__(self):
        self.id
        self.id_usuario
        self.titulo
        self.resumen
        self.contenido
        self.fecha_publicacion
        self.imagen
        self.estado


class Comentario:
    def __init__(self):
        self.id
        self.id_articulo
        self.id_usuario
        self.contenido
        self.fecha_hora
        self.estado
```

```text
Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y logueado, código que permita comentar al Publico y además publicar al Colaborador
```