'''
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
'''

def pedirNumero(msj: str) -> int:
    '''Pedir un número entero por consola

    Args:
        msj (str): mensaje que se muestra por consola al pedir el número

    Return:
        int: número introducido por el usuario
    '''
    try:
        num = int(input(msj))
    except:
        raise ValueError
    
    return num


def main():

    try:
        num = pedirNumero('Introduce un número entero: ')
    except ValueError:
        print(f'La entrada no es correcta - {ValueError}')


if __name__ == '__main__':
    main()