'''
El algoritmo burbuja

El algoritmo burbuja te permite ordenar valores de un array. Funciona revisando cada elemento con el elemanto adyacente. Si ambos elementos no están ordenados, se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado.
'''

def main():
    a = [8, 3, 1, 19, 14]

    # calcular la longitud de la lista
    n = len(a)

    for i in range(0, (n - 1)):

        for j in range(0, (n - 1 - i)):
            # compara los numero de las dos posiciones y los intercambia si el primero es mayor
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            
            j += 1
        
        i += 1

    print(a)


if __name__ == "__main__":
    main()