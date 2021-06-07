#################
#Mateo2021-icomp
# Suma Lenta (2)
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def suma_lenta(numero, otro_numero):
    print("inserte los numeros a sumar")
numero1 = int(input())
numero2 = int(input())
resultado = numero1 + numero2
for resultado in range(numero1, numero1 + numero2 + 1, 1):
    resultado = resultado +1
    resultado = resultado  -1
    print(resultado)
print("El resultado es" + str(resultado))


    

    






