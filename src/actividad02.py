'''
Actividad 2: 
    Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta, debe detectar los fallos usando try y except.
'''

def pedirCelsius(msj: str) -> float:
    '''Pide la temperatura en celsius

    Args:
        msj (str): mensaje que se muestra por consola al pedir la temperatura

    Return:
        float: temperatura intrducida por el usuario

    '''
    temp = float(input(msj))

    return temp


def convertirTemp(celsius: float) -> float:
    '''Convertir la temperatura en celsius a grados fahrenheit

    Args:
        celsius (float): temperatura en grados celsius dada por el usuario

    Return:
        float: temperatura convertida a grados fahrenheit
    '''
    if celsius < -500:
        raise ValueError('Celsius no puede ser menor de -500')
    
    far = (celsius * 9 / 5) + 32

    return far



def main():
    celsius = None
    while celsius == None:
        try:   
            celsius = pedirCelsius('Dame una temperatura en Celsius: ')
        except ValueError:
            print("**ERROR** - TEMPERATURA INTRODUCIDA NO VÁLIDA")
        except:
            print('**ERROR** - NO SE HA PODIDO CONVERTIR A FAHRENHEIT')


    fahrenheit = None
    try:
        fahrenheit = convertirTemp(celsius)
    except ValueError as e:
        print(e)


    if fahrenheit != None:
        print(f'{celsius} grados Celsius son {fahrenheit:.2f} grados en Fahrenheit')


if __name__ == "__main__":
    main()