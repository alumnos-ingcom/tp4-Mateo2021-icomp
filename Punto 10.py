################
# Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Factores Primos

def prueba():
    print("Bienvenido")
    numero = int(input("Ingrese un numero: "))

    def factores_primos(numero) :
        primos = []
        for i in range(2, numero+ 1) :
            while numero % i == 0 :
                        primos.append (i)
                        numero = numero / i
        return primos
    print ("Los factores primos son: ",factores_primos(numero))

if __name__ == "__main__":
    prueba()



       