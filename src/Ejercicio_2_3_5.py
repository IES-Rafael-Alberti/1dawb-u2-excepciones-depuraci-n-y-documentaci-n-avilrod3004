'''
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!" 
'''

def pedirPasswd() -> str:
    '''
    Pide una cadena de texto por consola

    Return:
        str: cadena de texto introducida por el usuario
    '''
    passwd = input('Introduce la contraseña: ')

    return passwd


def comprobarPasswd(passwd: str) -> bool:
    '''
    Comprueba si la contraseña guardad es igual que la introducida por el usuario

    Args:
        passwd (str): contraseña dada por el usuario

    Return:
        bool: True si coincide
    '''
    passwdOriginal = 'contraseña'

    if passwd == passwdOriginal:
        return True
    else:
        raise NameError('Incorrect Password!!')
    

def main():
    passwd = pedirPasswd()

    # comprueba si la contraseña introducida por el usuario coincide con la original
    # en caso de que sean diferentes lanza una excepción
    try:
        comprobarPasswd(passwd)
    except NameError as e:
        print(f'{NameError} {e}')


if __name__ == '__main__':
    main()