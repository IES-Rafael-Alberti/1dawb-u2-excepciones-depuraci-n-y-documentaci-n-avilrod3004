import pytest 
from src.Ejercicio_2_3_1 import aniosCumplidos

@pytest.mark.parametrize(
    "edad, expected",
    [
        (5, 'Años cumplicos --> 1 2 3 4 5'),
        (21, 'Años cumplicos --> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21'),
        (10, 'Años cumplicos --> 1 2 3 4 5 6 7 8 9 10'),
        (1, 'Años cumplicos --> 1'),
        (15, 'Años cumplicos --> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')
    ]
)

def test_aniosCumplicos_params(edad, expected):
    assert aniosCumplidos(edad) == expected