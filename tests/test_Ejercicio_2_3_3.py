import pytest
from src.Ejercicio_2_3_3 import cuentaAtras

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (10, 'Serie --> 10 9 8 7 6 5 4 3 2 1 0'),
        (5, 'Serie --> 5 4 3 2 1 0'),
        (12, 'Serie --> 12 11 10 9 8 7 6 5 4 3 2 1 0'),
        (18, 'Serie --> 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0')
    ]
)

def test_cuentaAtras_params(input_x, expected):
    assert cuentaAtras(input_x) == expected

def test_cuentaAtras_ValueError():
    with pytest.raises(ValueError):
        cuentaAtras(-1),
        cuentaAtras(0)