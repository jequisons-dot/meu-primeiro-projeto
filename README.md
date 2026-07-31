# Estudos de Python — ADS

Projetos e exercícios de lógica desenvolvidos durante o curso de Análise e Desenvolvimento de Sistemas.

## Conteúdos

- **Calculadora:** operações matemáticas com validação de erros.
- **Disciplinas:** exemplo de listas, condições e funções puras.
- **Monitor de sistema:** resumo de CPU e memória usando `psutil` (opcional).

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev,monitor]'
pytest
```

## Estrutura

```text
src/ads_studies/  # código reutilizável
tests/            # testes automatizados
```

## Próximos passos

Adicionar uma interface de terminal, testes para o monitor e integração contínua com GitHub Actions.
