################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Restas sucesivas

def prueba():
    dividendo = int(input("Por favor ingrese el dividendo: "))
    divisor = int(input("Por favor ingrese el divisor:" ))
    dividendo = dividendo - divisor
    def division_lenta(dividendo, divisor):
       contador = int(0)
       while(dividendo >= 0) :
            contador = contador + 1;
            dividendo = dividendo - divisor
            resto =  contador % 2
            resto = resto -1 
            print("el cociente es igual a: " + str(contador))
            print("el resto es igual a: " + str(resto))
            if resto == -1:
                print("el cociente es igual a: " + str(contador))
                print("el resto es igual a: " + str(resto +1))
            pass
    print(division_lenta(dividendo, divisor))

if __name__ == "__main__":
    prueba()
