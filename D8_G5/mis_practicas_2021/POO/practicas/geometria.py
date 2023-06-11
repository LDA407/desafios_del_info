from abc import ABC, abstractmethod


# EJERCICIOS DE HERENCIA MULTIPLE
class FiguraGeometrica(ABC):
    # FiguraGeometrica.variable_de_clase
    variable_de_clase = None

    def validar_v(self, v):
        return True if 0 < v < 10 else False

    def __init__(self, alto, ancho):
        if self.validar_v(alto):
            self._alto = alto
        if self.validar_v(ancho):
            self._ancho = ancho

    def __str__(self):
        return vars(self)

    @property
    def alto(self):
        return self._alto

    # eliminar los metodos setter para que los valores sean de solo lectura
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @abstractmethod
    def calcular_area(self):
        # no se declara ninguna funcion pero se obiga a las clases hijas a implementar la funcion
        pass
    
    # no recibe self ni parametros
    # no accede a las variables de instancia, solo accede a las variables de clase
    @staticmethod
    def static_method():
        print(FiguraGeometrica.variable_de_clase)

    # metodo de case recibe la referencia de la clase
    @classmethod
    def method_class(cls):
        print(cls.variable_de_clase)



class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color



# herencia multiple
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"""
            {FiguraGeometrica.__str__(self)}
            {Color.__str__(self)}
        """


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"""
            {FiguraGeometrica.__str__(self)}
            {Color.__str__(self)}
        """