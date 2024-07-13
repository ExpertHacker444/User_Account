from colorama import init, Fore, Style

init() # Inicializar colorama

def menu():
    print(Fore.YELLOW + "*--------Bienvenido al Menu Superkey--------*")
    print("1. Descuento")
    print("2. Pagar")
    print("3. Ver dinero disponible")
    print("4. Agregar dinero a la cuenta")
    print("5. Retirar dinero de la cuenta")
    print("6. Salir al menu")
    print("*-----------------------------*")

    while True:
        opcion = int(input(Fore.CYAN + "Elige una opción: "))

        if opcion == 1:
            print("Descuento Solicitado")
            break
        
        elif opcion == 2:
            print("Pagar")
            pagar()
        
        elif opcion == 3:
            print(f"Dinero disponible: {dinero_disponible}")
        
        elif opcion == 4:
            agregar_dinero()
        
        elif opcion == 5:
            retirar_dinero()
        
        elif opcion == 6:
            print("Saliendo, gracias por operar con Superkey")
            break

        else:
            print(Fore.RED + "Opción no válida, inténtelo de nuevo")


dinero_disponible = 0
dinero_necesario = 1000000

def pagar():
    global dinero_disponible

    print("¿Cuánto dinero desea pagar?")
    dinero_pagado = float(input("Ingrese el monto: "))

    if dinero_pagado > dinero_disponible:
        print(Fore.RED + "No tienes suficiente dinero en la cuenta.")
    else:
        if dinero_disponible >= 1000000:
            porcentaje_descuento = round(0.3 + (dinero_disponible // 1000000) * 0.05, 2)
            descuento = dinero_pagado * porcentaje_descuento
            print(f"Se ha aplicado un descuento del {porcentaje_descuento}% en tu próxima compra, por un monto de {dinero_pagado}. Gracias por su compra.")
        else:
            print(Fore.RED + "No tienes suficiente dinero en la cuenta. Por favor, agrega dinero.")


def agregar_dinero():
    global dinero_disponible

    print("¿Cuánto dinero desea agregar a su cuenta?")
    dinero_agregado = float(input("Ingrese el monto: "))
    dinero_disponible += dinero_agregado
    print(f"Se han agregado {dinero_agregado} a tu cuenta. Dinero disponible actual: {dinero_disponible}")


def retirar_dinero():
    global dinero_disponible

    print("¿Cuánto dinero desea retirar de su cuenta?")
    dinero_retirado = float(input("Ingrese el monto: "))
    if dinero_retirado > dinero_disponible:
        print(Fore.RED + "No tienes suficiente dinero en la cuenta para retirar.")
    else:
        dinero_disponible -= dinero_retirado
        print(f"Se han retirado {dinero_retirado} de tu cuenta. Dinero disponible actual: {dinero_disponible}")


menu()