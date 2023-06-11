class Producto:

    contador_productos = 0
    @classmethod
    def generate_id(cls):
        cls.contador_productos+=1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        # Producto.contador_ordenes+=1
        self.__id_producto = Producto.generate_id()
        self.__nombre = str(nombre)
        self.__precio = float(precio)

    @property
    def get_precio(self):
        return self.__precio

    def __str__(self):
        return f"id producto: {self.__id_producto}, nombre: {self.__nombre}, precio: {self.__precio}"


class Orden:

    contador_ordenes = 0
    @classmethod
    def generate_id(cls):
        cls.contador_ordenes+=1
        return cls.contador_ordenes

    def __init__(self, productos):
        # Producto.contador_ordenes+=1
        # especificar los tipos de datos para robustecer la clase
        self__id_orden = Producto.generate_id()
        self__productos = list(productos)
    
    # sobrecargar la clase all para unir objetos con +
    def __add__(self, other):
        return self__productos + other

    def agregar(self, producto):
        self__productos.append(producto)

    def total_price(self):
        a = [p.get_precio for p in self__productos]
        return sum(a)

    def __str__(self):
        return f"""
            id de la orden: {self__id_orden}
            productos: {[[p.__str__()] for p in self__productos]}
        """

if __name__ == '__main__':
    a = Producto('ashd', 100.00)
    b = Producto('aisjd', 30000.00)
    # agregacion de productos
    p = Orden([a,b])
    print(p.total_price())
