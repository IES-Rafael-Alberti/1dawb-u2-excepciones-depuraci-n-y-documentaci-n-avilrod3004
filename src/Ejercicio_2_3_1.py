'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def pedirEdad() -> int:
    """
    Pedir la edad y comprobar que se trata de un número entero entre 1 y 100
    
    Return:
        int: un entero con el valor de la edad introducida por consola
    """

    # Inicializar a None para no retornar un número si se produjo un error
    edad = None

    try:
        edad = int(input("Introduzca su edad: "))
    except ValueError:
        print('**ERROR** - INTRODUCE UN NÚMERO ENTERO')
    except:
        print('**ERROR** - VUELVE A INTENTARLO')

    return edad


def aniosCumplidos(edad: int) -> str:
    '''
    Crea una lista str con los años cumplidos del usuario desde 1.

    Args:
        edad (int): entero dado por el usuario por consola

    Return:
        str: años cumplidos desde 1 hasta la edad dada por el usuario
    '''
    lista = 'Años cumplicos -->'

    for i in range(1, (edad + 1), 1):
        lista = lista + f' {i}'

    return lista


def main():
    edad = pedirEdad()
    
    # Para continuar comprueba si la función pedirEdad() devuelve un número entero
    if edad != None:
        print(aniosCumplidos(edad))


if __name__ == "__main__":
    main()