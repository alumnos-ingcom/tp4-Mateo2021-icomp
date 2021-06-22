################
# Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Comparacion de Numeros

def prueba():
    print("Bienvenido")
    numero =  int(input("ingrese el primer numero: "))
    otro_numero= int(input("ingrese el segundo numero: "))
    def compara(numero, otro_numero):
        if numero < otro_numero:
            return -1
        if numero > otro_numero:
            return 1
        if numero == otro_numero:
            return 0
    print("La comparacion de los numeros dice que: ",compara(numero, otro_numero))

if __name__ == "__main__":
    prueba()


