'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

def pedirNumero(msj: str) -> int:
    '''Pedir un número entero por consola

    Args:
        msj (str): mensaje que se muestra por consola al pedir el número

    Return:
        int: número introducido por el usuario
    '''
    num = None

    try:
        num = int(input(msj))
    except ValueError:
         print('**ERROR** - INTRODUCE UN NÚMERO ENTERO')
    
    return num


def serieImpares(num: int) -> str:
    '''
    '''
    if num < 0:
        raise ValueError('**ERROR** - EL NÚMERO DEBE SER POSITIVO')
    
    serie = ''

    for i in range(1, (num + 1), 2):
        if i == 1:
            serie = serie + f'{i}'
        else:
            serie = serie + f', {i}'
        
        i += 2

    return serie


def main():
    num = pedirNumero('Introduce un número entero positivo: ')

    #Comprobar que el valor de num es un número entero
    if num != None:

        serie = None

        try:
            serie = serieImpares(num)
        except ValueError as e:
            print(e)
        except:
            print('**ERROR**')

        # Solo se imprime la serie si no ha saltado ningún error
        if serie != None:
            print(serie)


if __name__ == "__main__":
    main()