#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Conversion de Temperaturas

def prueba():
    print("Bienvenido")
    Centigrados = float(input("Ingrese los grados Celsius: "))
    Fahrenheit = 0
    def convertir_a_fahrenheit(Centigrados):
        Fahrenheit = (Centigrados * 9/5) + 32 
        return Fahrenheit
    print("Los grados Celsius pasados a Fahrenheit son: ", convertir_a_fahrenheit(Centigrados))

    fahrenheit = float(input("Ingrese grados Fahrenheit: "))
    centigrados = 0
    def convertir_a_centigrados(fahrenheit):
        centigrados = float(fahrenheit - 32) * (5/9)
        return centigrados
    print("La conversion de Celsius a Fahrenheit: ", convertir_a_centigrados(fahrenheit))

if __name__ == "__main__":
    prueba()