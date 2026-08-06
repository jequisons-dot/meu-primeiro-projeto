import pytest

from ads_studies.materias import adicionar_materia


def test_adiciona_materia_sem_alterar_lista_original():
    materias = ["Lógica"]
    assert adicionar_materia(materias, "Python") == ["Lógica", "Python"]
    assert materias == ["Lógica"]


def test_recusa_materia_repetida():
    with pytest.raises(ValueError, match="já foi adicionada"):
        adicionar_materia(["Python"], " python ")
