"""Operações aritméticas simples com validação de entrada."""


def calcular(operacao: str, primeiro: float, segundo: float) -> float:
    """Executa uma operação aritmética suportada."""
    operacoes = {
        "+": lambda: primeiro + segundo,
        "-": lambda: primeiro - segundo,
        "*": lambda: primeiro * segundo,
        "/": lambda: primeiro / segundo if segundo != 0 else _divisao_por_zero(),
    }
    try:
        return operacoes[operacao]()
    except KeyError as error:
        raise ValueError("Operação inválida. Use +, -, * ou /.") from error


def _divisao_por_zero() -> float:
    raise ValueError("Não é possível dividir por zero.")
