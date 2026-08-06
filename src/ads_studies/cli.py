"""Interface de terminal para os exercícios de ADS."""

from ads_studies.calculadora import calcular
from ads_studies.materias import adicionar_materia
from ads_studies.monitor import obter_status


def mostrar_menu() -> None:
    """Exibe as opções disponíveis para a pessoa usuária."""
    print("\n=== Estudos de Python — ADS ===")
    print("1. Usar calculadora")
    print("2. Adicionar disciplina")
    print("3. Listar disciplinas")
    print("4. Ver monitor do sistema")
    print("0. Sair")


def ler_numero(mensagem: str) -> float:
    """Lê um número e informa um erro amigável para entradas inválidas."""
    try:
        return float(input(mensagem).replace(",", "."))
    except ValueError as error:
        raise ValueError("Digite um número válido.") from error


def executar_calculadora() -> None:
    """Lê a operação e os dois números, depois mostra o resultado."""
    operacao = input("Operação (+, -, * ou /): ").strip()
    primeiro = ler_numero("Primeiro número: ")
    segundo = ler_numero("Segundo número: ")
    resultado = calcular(operacao, primeiro, segundo)
    print(f"Resultado: {resultado:g}")


def executar_monitor() -> None:
    """Mostra o percentual atual de CPU e memória."""
    status = obter_status()
    print(f"CPU: {status.cpu_percentual:.1f}%")
    print(f"Memória: {status.memoria_percentual:.1f}%")


def main() -> None:
    """Executa o menu até a pessoa usuária escolher sair."""
    materias: list[str] = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                executar_calculadora()
            elif opcao == "2":
                materia = input("Nome da disciplina: ")
                materias = adicionar_materia(materias, materia)
                print("Disciplina adicionada.")
            elif opcao == "3":
                if not materias:
                    print("Nenhuma disciplina cadastrada.")
                else:
                    print("Disciplinas cadastradas:")
                    for indice, materia in enumerate(materias, start=1):
                        print(f"{indice}. {materia}")
            elif opcao == "4":
                executar_monitor()
            elif opcao == "0":
                print("Até mais!")
                return
            else:
                print("Opção inválida. Escolha um número do menu.")
        except (RuntimeError, ValueError) as error:
            print(f"Erro: {error}")


if __name__ == "__main__":
    main()
