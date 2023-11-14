'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto. 
'''

def pedirNumero(num, msj: str) -> int:
    '''Pedir un número entero por consola

    Args:
        msj (str): mensaje que se muestra por consola al pedir el número

    Return:
        int: número introducido por el usuario
    '''
    try:
        num = int(input(msj))
    except ValueError:
         print('**ERROR** - INTRODUCE UN NÚMERO ENTERO')
    
    return num


def cuentaAtras(num: int) -> str:
    '''
    '''
    if num <= 0:
        raise ValueError('**ERROR** - EL NÚMERO DEBE SER POSITIVO Y DISTINTO A CERO')
    
    serie = 'Serie --> '

    for i in range(0, (num + 1), 1):
        if i == 0:
            serie = serie + f'{num - i}'
        else:
            serie = serie + f' {num - i}'

    return serie



def main():
    num = None

    # comprobar que num tenga un valor distinto a None
    while num == None:
        num = pedirNumero(num, 'Introduce un número entero positivo: ')

    if num != None:

        serie = None

        try:
            serie = cuentaAtras(num)
        except ValueError as e:
            print(e)
        except:
            print('**ERROR**')

        # si no ha ocurrido ningún error se muestra por pantalla la cuenta atrás
        if serie != None:
            print(serie)
    

if __name__ == '__main__':
    main()