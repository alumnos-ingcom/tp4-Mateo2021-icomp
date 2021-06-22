################
# Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Numero Primo

def prueba():
    print("Bienvenido")
    print("Un numero primo solo es divisible por 1 y si mismo")
    numero = int(input("Ingrese un numero para saber si es primo: "))
    def es_primo(numero):
        if numero > 1:
            contador = 0
        for i in range (2,numero):
            resto = numero % i
            print("{} % {} = {}".format(numero, i, resto))
            if resto ==0:
                contador+=1
            if contador ==0:
                print("True") #True seria, si es primo.
    print(es_primo(numero))

if __name__ == "__main__":
    prueba()
            