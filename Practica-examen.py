

"""
Funciones separadas por operacion:
    consultar_saldo
    Depositar
    Retirar
    Salir
"""

def consultar_saldo(saldo):
    print("\n\n\n 1. Consultar saldo")
    print("Su saldo actual es: $", saldo)

def depositar(saldo):
    print("\n\n\n 2. Depositar dinero")
    deposito = int(input("Cuanto dinero deseas depositar?: $"))
    if deposito > 0:
        saldo = saldo + deposito
        print("Depositaste: $", deposito, "tu saldo ahora es: $", saldo)
    else:
        print("Monto invalido, el monto debe ser mayor que 0.")
        return saldo


def retirar(saldo):
    retiro = (int(input("Cuanto dinero deseas retirar?: $")))
    if retiro <= 0:
        print("Monto invalido, el monto debe ser mayor que 0.")
        return
    else:
        saldo = saldo - retiro
        print ("Retiro exitoso, su nuevo saldo es: $", saldo)

def salir():
        print("\n\n\n Gracias por usar nuestro servicios.")


saldo = int(1000)

def menu():
    print(
"""
***MENU***
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
-------------------
""")

def leerOpcion():
    opcion = input(">>> Opcion?: ")
    while opcion < "1" or opcion > "4":
        print("--> Error. Opcion invalida.")
        input("Presione ENTER para continuar.")
        print("\n\n\n\n\n")
        menu()
        opcion = input(">>> Opcion?: ")

    return int(opcion)

while True:
    menu()
    opcion = leerOpcion ()
    match opcion:
        case 1:
            consultar_saldo(saldo)
        case 2:
            depositar(saldo)
        case 3:
            retirar(saldo)
        case 4:
            print("Gracias por usar el programa.")
            break

input("Presione ENTER para continuar.")
