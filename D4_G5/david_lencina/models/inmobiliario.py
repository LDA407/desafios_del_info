class Inmueble:

    contador_de_inmuebles = 0

    @classmethod
    def generate_id(cls):
        cls.contador_de_inmuebles+=1
        return cls.contador_de_inmuebles
    
    def __init__(self, año, metros, habitaciones, garage, zona, estado):
        self.id = self.generate_id()
        self.año = año 
        self.metros = metros 
        self.habitaciones = habitaciones 
        self.garage:bool = garage
        self.zona = zona
        self.estado = estado

    # def set_estado(self, nuevo_estado):
    #     self.estado = nuevo_estado
    #     return self.estado

    def __str__(self):
        return self.__dict__