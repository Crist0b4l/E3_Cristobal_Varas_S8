'''Automotora Ruta40'''

import re

vehiculos = []


def validar_tipo(tipo):
    '''Validar que el tipo de vehiculo ingresado sea uno de los 4 posibles'''
    tipo_vehiculo = ["Auto", "Suvs", "Pickups", "Vans"]
    return tipo.title() in tipo_vehiculo


def validar_patente(patente):
    '''Verificar si la patente cumple con el formato de patentes chilenas("AA1111" o "AAAA11")'''
    patente = patente.upper().replace("-", "")
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


def validar_fecha(fecha_registro):
    '''Validar que la fecha esté en el formato DD-MM-AAAA'''
    # Expresión regular para el formato DD-MM-AAAA
    patron = r'^\d{2}-\d{2}-\d{4}$'
    if re.match(patron, fecha_registro):
        return True
    return False


def validar_nom_duenno(nom_duenno):
    return len(nom_duenno) > 0


def validar_campo(mensaje, fx_validar, mensaje_error):
    while True:
        valor = input(mensaje)
        if fx_validar(valor):
            return valor
        print(mensaje_error)


def guardar(tipo, patente, marca, modelo, precio, multas, fecha_registro, nom_duenno):
    vehiculos.append({
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "multas": [
            {"monto": multa["monto"], "fecha": multa["fecha"]} for multa in multas],
        "fecha_registro": fecha_registro,
        "nom_duenno": nom_duenno
    })

    print("Vehículo registrado exitosamente.")


def buscar():
    return


def imprimir_certificados():
    return


def salir():
    autor = "Cristóbal Varas Polanco"
    version = 1.0
    print("Saliendo...")
    print("Gracias por usar nuestro software")
    print(f"Versión {version}")
    print(f"Autor: {autor}")
    return
