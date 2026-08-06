import pytest

from ads_studies.calculadora import calcular


def test_soma():
    assert calcular("+", 2, 3) == 5


def test_divisao_por_zero():
    with pytest.raises(ValueError, match="dividir por zero"):
        calcular("/", 8, 0)


def test_operacao_invalida():
    with pytest.raises(ValueError, match="Operação inválida"):
        calcular("%", 8, 2)
