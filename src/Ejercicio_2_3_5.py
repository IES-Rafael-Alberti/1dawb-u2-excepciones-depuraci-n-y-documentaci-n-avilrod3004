'''
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!" 
'''

def pedirPasswd() -> str:
    '''
    '''
    passwd = input('Introduce la contraseña: ')

    return passwd


def comprobarPasswd(passwd: str) -> bool:
    '''
    '''
    passwdOriginal = 'contraseña'

    if passwd == passwdOriginal:
        return True
    else:
        raise NameError('Incorrect Password!!')
    

def main():
    passwd = pedirPasswd()

    try:
        comprobarPasswd(passwd)
    except NameError as e:
        print(f'{NameError} {e}')


if __name__ == '__main__':
    main()