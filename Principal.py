'''Menú_Automotora_Ruta40'''

import Funciones

while True:
    Funciones.menu()
    print("Ingrese una opción del menú")
    opcion = int(input())

    if opcion == 1:
        Funciones.registrar_vehiculo()
    elif opcion == 2:
        Funciones.buscar()
    elif opcion == 3:
        Funciones.imprimir_certificados()
    elif opcion == 4:
        Funciones.salir()
        break
    else:
        print("Por favor seleccione una opción válida (1-4)")
