from models.inmobiliario import Inmueble
from models.libroInmobiliario import LibroDeRegistros


if __name__ == '__main__':
    p1 = Inmueble(año=2010, metros=255, habitaciones=6, garage=True, zona="A", estado="Disponible")
    p2 = Inmueble(año=2000, metros=40, habitaciones=3, garage=False, zona="B", estado="Disponible")
    
    libro = LibroDeRegistros()
    libro.agregar(p1)

    print(p1.__str__())
    print(p2.__str__())
    print(libro.__dict__)
