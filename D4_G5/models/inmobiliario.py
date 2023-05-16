class Inmueble:

    contador_de_inmuebles = 0
    
    def __init__(self, año, metros, habitaciones, garage, zona, estado):
        self.id = Inmueble.contador_de_inmuebles = 1
        self.año = año 
        self.metros = metros 
        self.habitaciones = habitaciones 
        self.garage:bool = garage
        self.zona = zona
        self.estado = estado

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        return self.estado

    def __str__(self):
        return self.__dict__