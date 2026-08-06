import sys
from types import SimpleNamespace

from ads_studies.monitor import obter_status


def test_obtem_status_do_sistema(monkeypatch):
    psutil_falso = SimpleNamespace(
        cpu_percent=lambda interval: 42.5,
        virtual_memory=lambda: SimpleNamespace(percent=64.0),
    )
    monkeypatch.setitem(sys.modules, "psutil", psutil_falso)

    status = obter_status()

    assert status.cpu_percentual == 42.5
    assert status.memoria_percentual == 64.0
