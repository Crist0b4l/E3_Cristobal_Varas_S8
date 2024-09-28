'''Menú_Automotora_Ruta40'''

import Funciones


def menu():
    '''Definiendo la función que mostrará el menú'''
    print("Menú Automotora Ruta 40 (Región de Los Lagos)")
    print("1. Registrar vehículo")
    print("2. Buscar vehículo")
    print("3. Impresión de certificados")
    print("4. Salir")


while True:
    menu()
    print("Ingrese una opción del menú")
    opcion = int(input())

    if opcion == 1:
        while True:
            tipo = Funciones.validar_campo(
                "Ingrese el tipo de vehículo 'Auto', 'Suvs', 'Pickups', 'Vans': ", Funciones.validar_tipo, "Tipo de vehículo inválido. Debe ser Auto, Suvs, Pickups o Vans.")
            patente = Funciones.validar_campo(
                "Ingrese la patente del vehículo debe contener 2 letras y 4 números ('AA1111') o 4 letras y 2 números ('AAAA11'): ", Funciones.validar_patente, "Formato de patente inválido debe ser 'AA1111' o 'AAAA11'")
            marca = Funciones.validar_campo(
                "Ingrese la marca del vehículo: ", Funciones.validar_marca, "La marca debe contener entre 2 y 12 caractéres")
            modelo = Funciones.validar_campo("Ingrese el modelo del vehículo: ", Funciones.validar_modelo,
                                             "No es posible dejar el campo vacío. Por favor ingrese un valor")
            precio = Funciones.validar_campo(
                "Ingrese el precio del vehículo: ", Funciones.validar_precio, "El valor del vehículo debe ser mayor a $6.880.000")
            multas = []
            while True:
                monto = int(
                    input("Ingrese el monto de la multa (ingrese 0 en caso de no existir multa): "))
                if monto == 0:
                    break
                fecha = input("Ingrese la fecha de la multa (DD-MM-AAAA): ")
                multas.append({"monto": monto, "fecha": fecha})
            fecha_registro = Funciones.validar_campo(
                "Ingrese la fecha de la multa (DD-MM-AAAA): ", Funciones.validar_fecha, "formato inválido. Ingrese una fecha en el formato (DD-MM-AAAA)")
            nom_duenno = input("Ingrese nombre del dueño del vehículo: ")
            Funciones.guardar(tipo, patente, marca, modelo, precio,
                              multas, fecha_registro, nom_duenno)
    elif opcion == 2:
        Funciones.buscar()
    elif opcion == 3:
        Funciones.imprimir_certificados()
    elif opcion == 4:
        Funciones.salir()
        break
    else:
        print("Por favor seleccione una opción válida (1-4)")
