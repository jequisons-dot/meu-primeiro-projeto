"""Gerenciamento de disciplinas estudadas."""


def adicionar_materia(materias: list[str], materia: str) -> list[str]:
    """Retorna uma nova lista com uma disciplina válida, sem duplicidade."""
    nome = materia.strip()
    if not nome:
        raise ValueError("O nome da disciplina não pode estar vazio.")
    if nome.casefold() in {item.casefold() for item in materias}:
        raise ValueError("Esta disciplina já foi adicionada.")
    return [*materias, nome]
