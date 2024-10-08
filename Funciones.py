'''Automotora Ruta40'''

import re

vehiculos = []


def menu():
    '''Definiendo la función que mostrará el menú'''
    print("Menú Automotora Ruta 40 (Región de Los Lagos)")
    print("1. Registrar vehículo")
    print("2. Buscar vehículo")
    print("3. Impresión de certificados")
    print("4. Salir")


def validar_tipo(tipo):
    '''Validar que el tipo de vehiculo ingresado sea uno de los 4 posibles'''
    tipo_vehiculo = ["Auto", "Suvs", "Pickups", "Vans"]
    return tipo.title() in tipo_vehiculo


def validar_patente(patente):
    '''Verificar si la patente cumple con el formato de patentes chilenas("AA1111" o "AAAA11") con una expresión regular'''
    patente = patente.upper().replace("-", "")
    '''la expresion regular indica que debe tener 2 caracteres alfabeticos y 4 numericos o o alfabeticos y 2 numericos'''
    if re.match(r"^[A-Z]{2}\d{4}$|^[A-Z]{4}\d{2}$", patente):
        return True
    return False


def validar_marca(marca):
    '''Validar si la marca cumple con la longitud de caracteres'''
    return 2 <= len(marca) <= 12


def validar_modelo(modelo):
    '''Validar que el campo modelo no vaya vacio'''
    return len(modelo) > 0


def validar_precio(precio):
    '''Validar que el precio sea mayor a 6880000'''
    precio = int(precio)
    return precio >= 6880000


def validar_fecha(fecha):
    '''Validar que la fecha esté en el formato DD-MM-AAAA'''
    '''Expresión regular para el formato DD-MM-AAAA'''
    patron = r'^\d{2}-\d{2}-\d{4}$'
    if re.match(patron, fecha):
        return True
    return False


def validar_nom_duenno(nom_duenno):
    '''Validar que el nombre del dueño no vaya vacio'''
    return len(nom_duenno) > 0


def validar_campo(mensaje, fx_validar, mensaje_error):
    '''Función para validar un campo con opción de cancelar'''
    while True:
        '''Se le asigna lo que ingresa el usuario en el input a la variable valor'''
        valor = input(mensaje)
        if valor == "00":
            return "cancelar"
        '''la variable valor es pasada como argumento a la funcion de validacion correspondiente'''
        if fx_validar(valor):
            return valor
        '''Si la funcion de validacion no valida, se imprime un mensaje de error'''
        print(mensaje_error)


def guardar(tipo, patente, marca, modelo, precio, multas, fecha_registro, nom_duenno):
    '''Si la validacion es correcta se guardan los datos del vehiculo en un diccionario'''
    vehiculos.append({
        "tipo": tipo.title(),
        "patente": patente.upper(),
        "marca": marca.title(),
        "modelo": modelo.title(),
        "precio": precio,
        "multas": [
            {"monto": multa["monto"], "fecha": multa["fecha"]} for multa in multas],
        "fecha_registro": fecha_registro,
        "nom_duenno": nom_duenno.title()
    })

    print("Vehículo registrado exitosamente.")
    print()


def registrar_vehiculo():
    '''En esta funcion se ingresan los datos que seran validados en las funciones de validacion, junto con el mensaje de error en caso de ser necesario'''
    while True:
        tipo = validar_campo(
            "Ingrese el tipo de vehículo 'Auto', 'Suvs', 'Pickups', 'Vans' (00 para cancelar): ",
            validar_tipo, "Tipo de vehículo inválido. Debe ser Auto, Suvs, Pickups o Vans.")
        if tipo == "cancelar":
            return

        patente = validar_campo(
            "Ingrese la patente del vehículo ('AA1111' o 'AAAA11') (00 para cancelar): ",
            validar_patente, "Formato de patente inválido debe ser 'AA1111' o 'AAAA11'")
        if patente == "cancelar":
            return

        marca = validar_campo(
            "Ingrese la marca del vehículo (00 para cancelar): ",
            validar_marca, "La marca debe contener entre 2 y 12 caracteres")
        if marca == "cancelar":
            return

        modelo = validar_campo(
            "Ingrese el modelo del vehículo (00 para cancelar): ",
            validar_modelo, "No es posible dejar el campo vacío.")
        if modelo == "cancelar":
            return

        precio = validar_campo(
            "Ingrese el precio del vehículo (00 para cancelar): ",
            validar_precio, "El valor del vehículo debe ser mayor a $6.880.000")
        if precio == "cancelar":
            return

        multas = []
        while True:
            monto = int(
                input("Ingrese el monto de la multa (0 para terminar de ingresar multas): "))
            if monto == 0:
                break
            fecha = validar_campo("Ingrese la fecha de la multa (DD-MM-AAAA) (0 para cancelar): ",
                                  validar_fecha, "Formato inválido. Ingrese una fecha en el formato (DD-MM-AAAA)")
            if fecha == "cancelar":
                return
            multas.append({"monto": monto, "fecha": fecha})

        fecha_registro = validar_campo(
            "Ingrese la fecha del registro (DD-MM-AAAA) (00 para cancelar): ",
            validar_fecha, "Formato inválido. Ingrese una fecha en el formato (DD-MM-AAAA)")
        if fecha_registro == "cancelar":
            return

        nom_duenno = input(
            "Ingrese nombre del dueño del vehículo (00 para cancelar): ")
        if nom_duenno == "cancelar":
            return
        '''Se pasan los valores a la funcion guardar para que esta los añada la lista "vehiculos"'''
        guardar(tipo, patente, marca, modelo, precio,
                multas, fecha_registro, nom_duenno)
        break


def buscar():
    '''Buscar un vehiculo mediante una patente previamente registrada'''
    if not vehiculos:
        print("No hay vehículos registrados")
        print()
        return
    while True:
        print("Ingrese una patente ('AA1111' o 'AAAA11') para consultar los datos de un vehículo o presione 00 para salir: ")
        '''Estandarizar la entrada de la patente'''
        patente_buscada = input().upper().replace("-", "")
        if patente_buscada == "00":
            break

        '''Se crea una variable vacia, se itera sobre la lista vehiculos y si la patente ingresada coincide con alguna de las patentes de un auto de la lista vehiculos se le asigna ese auto a la variable auto_encontrado'''
        auto_encontrado = None
        for auto in vehiculos:
            if auto['patente'] == patente_buscada:
                auto_encontrado = auto
                break

        if auto_encontrado:
            '''Imprimir los datos básicos del vehículo'''
            print(f"Tipo de vehículo: {auto_encontrado['tipo']}")
            print(f"Patente del vehículo: {auto_encontrado['patente']}")
            print(f"Marca del vehículo: {auto_encontrado['marca']}")
            print(f"Modelo del vehículo: {auto_encontrado['modelo']}")
            print(f"Precio del vehículo: ${auto_encontrado['precio']}")
            print(f"Fecha de registro: {auto_encontrado['fecha_registro']}")
            print(f"Nombre dueño del vehículo: {
                  auto_encontrado['nom_duenno']}")

            '''Si tiene multas, imprimirlas'''
            if auto_encontrado["multas"]:
                print("Multas del vehículo:")
                for multa in auto_encontrado["multas"]:
                    print(f"- Monto: {multa['monto']
                                      }, Fecha: {multa['fecha']}")
            else:
                print("El vehículo no tiene multas registradas.")
        else:
            print("No se encontró ningún vehículo con esa patente.")


def imprimir_certificados():
    '''crea un submenu con las opciones para imprimir certificados'''
    if not vehiculos:
        print("No hay vehículos registrados")
        print()
        return

    while True:
        print("Seleccione el tipo de certificado a imprimir")
        print("1. Certificado de emisiones de contaminantes")
        print("2. Certificado de anotaciones vigentes")
        print("3. Certificado de multas")
        print("4. Volver al menú principal")

        opcion_certificado = input("Ingrese una opción (1-4): ")
        if opcion_certificado == "4":
            print("Volviendo al menú principal...")
            print()
            break

        patente = input(
            "Ingrese la patente del vehículo: ").upper().replace("-", "")

        auto_encontrado = None
        for auto in vehiculos:
            if auto['patente'] == patente:
                auto_encontrado = auto
                break

        if not auto_encontrado:
            print("No se encontraron vehículos con esa patente")
            print()
            continue

        import random
        valor_certificado = random.randint(2300, 4500)

        if opcion_certificado == "1":
            print("Certificado de Emisión de Contaminantes")
            print(f"Patente: {patente}")
            print(f"Nombre del dueño: {auto_encontrado['nom_duenno']}")
            print(f"Valor: ${valor_certificado}")
            print()

        elif opcion_certificado == "2":
            print("Certificado de Anotaciones Vigentes")
            print(f"Patente: {patente}")
            print(f"Nombre del dueño: {auto_encontrado['nom_duenno']}")
            print(f"Valor: ${valor_certificado}")
            print()

            '''Si tiene multas se extrae su valor de la lista vehiculos'''
        elif opcion_certificado == "3":
            if auto_encontrado['multas']:
                print("Certificado de Multas")
                print(f"Patente: {patente}")
                print(f"Nombre del dueño: {auto_encontrado['nom_duenno']}")
                for multa in auto_encontrado['multas']:
                    print(
                        f"- Monto de la multa: ${multa['monto']} - Fecha: {multa['fecha']}")
            else:
                print(
                    "El vehículo no tiene multas registradas. No se emitirá ningún certificado.")
                print()
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
            print()


def salir():
    '''Funcion para terminar la ejecucion de la aplicacion'''
    autor = "Cristóbal Varas Polanco"
    version = 1.0
    print("Saliendo...")
    print("Gracias por usar nuestro software")
    print(f"Versión {version}")
    print(f"Autor: {autor}")
    return
