from models.inmobiliario import Inmueble


if __name__ == '__main__':
    p1 = Inmueble(año=2010, metros=255, habitaciones=6, garage=True, zona="A", estado="Disponible")
    p2 = Inmueble(año=2000, metros=40, habitaciones=3, garage=False, zona="B", estado="Disponible")
    
    print(p1)
    print(p2.__str__())
