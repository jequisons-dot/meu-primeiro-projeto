import requests
from rich import print

cep = "01001000"  # Exemplo de CEP
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
dados = response.json()

print(f"[bold yellow]Endreço encontrado: [/bold yellow]")
print(f"Rua: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']} - {dados['localidade']}")
