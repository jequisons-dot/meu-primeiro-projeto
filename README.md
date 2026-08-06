# 🐍 Estudos de Python — ADS

Projetos e exercícios de lógica desenvolvidos durante o curso de Análise e Desenvolvimento de Sistemas.

## 📦 Conteúdos

- 🧮 **Calculadora:** operações matemáticas com validação de erros.
- 📚 **Disciplinas:** exemplo de listas, condições e funções puras.
- 💻 **Monitor de sistema:** resumo de CPU e memória usando `psutil` (opcional).
- ⌨️ **Interface de terminal:** menu que reúne os exercícios em um único programa.

## 🚀 Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev,monitor]'
ads-studies
```

Para executar os testes:

```bash
pytest
```

## 🗂️ Estrutura

```text
src/ads_studies/  # código reutilizável
tests/            # testes automatizados
```

## 🎯 Metas de Aprendizado (ADS)

- [x] Configuração de ambiente Python, `.venv` e gerenciamento com `pyproject.toml`
- [x] Criação e execução de testes automatizados com `pytest`
- [x] Implementação de interface CLI amigável para os scripts
- [ ] Integração contínua (CI) com GitHub Actions para rodar testes automaticamente
- [ ] Cobertura de testes unitários para o módulo de monitoramento de sistema
- [ ] Conexão do projeto com banco de dados relacional (SQLite/PostgreSQL)
