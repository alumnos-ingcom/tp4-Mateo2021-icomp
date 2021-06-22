################
# Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Ordenar 3 valores

def prueba():
    print("Bienvenido")
    uno = int(input("Ingrese el primer numero: "))
    dos = int(input("Ingrese el segundo numero: "))
    tres = int(input("Ingrese el tercer numero: "))
    def ordenar_mayor_a_menor(uno, dos, tres):
        globals
        Primero = min (uno, dos, tres)
        return Primero

    def ordenar_menor_a_mayor(uno, dos, tres):
        globals
        Tercero= max (uno, dos, tres)
        return Tercero

    Primero = int(ordenar_mayor_a_menor(uno,dos,tres))
    Tercero = int(ordenar_menor_a_mayor(uno,dos,tres))
    Segundo = (uno + dos + tres) - Primero - Tercero
    lista = (Primero, Segundo,Tercero)
    listados = (Tercero, Segundo, Primero)
    print('de menor a mayor es: ', lista)
    print('y de mayor a menor es: ',listados)

if __name__ == "__main__":
    prueba()
