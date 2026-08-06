from ads_studies.cli import main


def test_main_adiciona_e_lista_disciplina(monkeypatch, capsys):
    entradas = iter(["2", "Python", "3", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main()

    saida = capsys.readouterr().out
    assert "Disciplina adicionada." in saida
    assert "1. Python" in saida


def test_main_informa_opcao_invalida(monkeypatch, capsys):
    entradas = iter(["9", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main()

    assert "Opção inválida" in capsys.readouterr().out
