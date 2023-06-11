from datetime import datetime

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = str(color)
        self.ruedas = int(ruedas)
    
    def __str__(self):
        return vars(self)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = str(tipo)

    def __str__(self):
        return {**vars(super()), **vars(self)}


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = int(velocidad)
        self.fecha = datetime.now

    if isinstance(a, int) and isinstance(b, int):
        return a + b

    def __str__(self) -> str:
        return f"""
            {super().__str__()}\n
            velocidad: {self.velocidad}
        """


b = Bicicleta("ROJO", 2, "MONTAÑA")
c = Coche("blanco"," 4", "350")
print(b)
print(c)