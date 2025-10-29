import pytest
from division import division

def test_division_normal():
    assert division(10, 2) == 5.0

def test_division_decimal():
    assert division(7, 2) == 3.5

def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        division(6, 0)