# no necesariamente tiene que haber una herencia directa
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = str(nombre)
        self.sueldo = int(sueldo)

    def __str__(self):
        return f"nombre: {self.nombre}, sueldo: {self.sueldo}"


class Gerente(Empleado):
    def __init__(self,nombre, sueldo, departamento):
        super()._init__(nombre, sueldo)
        self.departamento = str(departamento)

    def __str__(self):
        return f"{super().__str__()}, departamento {self.departamento}"


if __name__ == '__main__':
    def imprimir_detalle(a):
        print(a)
        print(type(a))
    
    imprimir_detalle((Gerente("juan", 5000, "sistemas")))