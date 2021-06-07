################
# Mateo2021-icomp
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Ordenar 3 valores

print("Bienvenido")
print("Ingrese el primer numero")
numero = int(input())
print("Ingrese el segundo numero")
numerodos = int(input())
print("Ingrese el tercer numero")
numerotres = int(input())

Primero = min (numero, numerodos, numerotres)
Tercero= max (numero, numerodos, numerotres)
Segundo = (numero + numerodos + numerotres) - Primero - Tercero

lista = (Primero, Segundo, Tercero)
print(lista)


