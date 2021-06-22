################
# Mateo2021-icomp
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Palindromos

def prueba():
    palindromos = [
        'Anitalavalatina' ,
        'oso' ,
        'ojo' ,
        'seres' ,
        'Yohagoyogahoy' ,
        123321
    ]
    
    def es_palindromo(p):
        estandar = str(p).lower().replace('  ', ' ')
        return estandar == estandar [:: -1]
    if __name__== '__main__':
        for p in palindromos:
            resultado = es_palindromo(p)
            print(resultado)

if __name__ == "__main__":
    prueba()