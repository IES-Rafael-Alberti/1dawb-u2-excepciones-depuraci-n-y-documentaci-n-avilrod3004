import pytest
from src.actividad02 import convertirTemp

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (10.5, 50.9),
        (124.589, 256.2602),
        (32, 89.6),
        (19, 66.2)
    ]
)

def test_convertitTemp_params(input_x, expected):
    assert convertirTemp(input_x) == expected


def test_convertirTemp_ValueError():
    with pytest.raises(ValueError):
        convertirTemp(-550)