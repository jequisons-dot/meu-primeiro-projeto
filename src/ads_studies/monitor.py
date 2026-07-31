"""Resumo portátil de recursos do sistema."""

from dataclasses import dataclass


@dataclass(frozen=True)
class StatusSistema:
    cpu_percentual: float
    memoria_percentual: float


def obter_status() -> StatusSistema:
    """Obtém o uso atual de CPU e memória com psutil instalado."""
    try:
        import psutil
    except ImportError as error:
        raise RuntimeError("Instale o extra de monitoramento: pip install .[monitor]") from error
    return StatusSistema(psutil.cpu_percent(interval=0.1), psutil.virtual_memory().percent)
