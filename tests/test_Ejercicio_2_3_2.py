import pytest
from src.Ejercicio_2_3_2 import serieImpares

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (17, '1, 3, 5, 7, 9, 11, 13, 15, 17'),
        (10, '1, 3, 5, 7, 9'),
        (5, '1, 3, 5'),
        (23, '1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23')
    ]
)

def test_serieImpares_params(input_x, expected):
    assert serieImpares(input_x) == expected

def test_serieImpares_ValueError():
    with pytest.raises(ValueError):
        serieImpares(-5)