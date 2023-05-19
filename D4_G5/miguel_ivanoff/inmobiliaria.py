from os import system
import funciones
import menu

lista_inmueble=[{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


while True:
    menu.encabezado()
    opcion=menu.verMenu()

    if opcion==5:
        system('cls')
        print('SESION FINALIZADA!!')
        break   

    if opcion==1:
        anio=int(input('Año de la Propiedad: '))
        sup=int(input('Metros cuadrados: '))
        habit=int(input('Cant. Habitaciones: '))
        garaje=input('Garaje Si/No : ')
        if garaje.lower()=='si':
            garaje=True
        else:
            garaje=False
        zona=input('Elija la zona (A, B, C): ')
        estado=input('Seleccione estado (Disponible, Reservado, Vendido): ')
   
        if funciones.validaParametros(anio,sup,habit,zona,estado):
            propiedad={
                'año':anio,
                'metros': sup,
                'habitaciones': habit,
                'garaje': garaje,
                'zona': zona.upper(),
                'estado': estado
            }
            lista_inmueble.append(propiedad)
            input('La Propiedad fue Registrada.  <<Presiones ENTER>>')
            
    if opcion==2:
        menu.encabezado()
        contador=0
        for p in lista_inmueble:
            contador+=1
            print(f"{contador}- Propiedad de {p['metros']}m2, de zona: {p['zona']}, y estado: {p['estado']}.")
        prop=int(input("Seleccione la propiedad a cambiar el estado:"))
        nuevo_estado=input('Ingrese el nuevo estado (Disponible - Reservado - Vendido):')

        op=input('Está seguro de cambiar de estado? S/N').lower()
        
        if op=="s":
            lista_inmueble[prop-1]['estado']=nuevo_estado
            print(f'Se ha modificado correctamente el estado de la propiedad {prop-1}')
            print(lista_inmueble[prop-1])
            input('<<Presiones ENTER>>')
        

    if opcion==3:
        pass
    
    if opcion==4:
        menu.encabezado()
        print('\n =========== Buscar por un Presupuesto ==========')
        monto=int(input('\tIngrese su presupuesto: '))
        
        prop_listadas=funciones.extrae_prop(lista_inmueble)
        prop_finales=funciones.lista_final(prop_listadas,monto)
        
        for p in prop_finales:
            print(p)
        input("<<ENTER>>")
        
