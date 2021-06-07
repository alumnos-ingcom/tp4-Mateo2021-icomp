################
#Mateo2021-icomp
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Restas sucesivas
contador = int(0)

dividendo = int(input("Por favor ingrese el dividendo: "))
divisor = int(input("Por favor ingrese el divisor:" ))
dividendo = dividendo - divisor

while(dividendo >= 0) :
    contador = contador + 1;
    dividendo = dividendo - divisor
    resto = contador % 2
    resto = resto - 1
    print("el cociente es igual a: " + str(contador))
    print("el resto es igual a: " + str(resto))