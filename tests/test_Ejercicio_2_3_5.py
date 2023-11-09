import pytest
from src.Ejercicio_2_3_5 import comprobarPasswd

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ('contraseña', True)
    ]
)

def test_comprobarPasswd_params(input_x, expected):
    assert comprobarPasswd(input_x) == expected


def test_comprobarPasswd_NameError():
    with pytest.raises(NameError):
        comprobarPasswd('Hola')