import psutil
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from plyer import notification

console = Console()

def enviar_alerta(cpu):
    notification.notify(
        title='⚠️Alerta de CPU',
        message=f'O uso de processador em {cpu}%!' ,
        app_name= 'Monitor M5',
        timeout=5
    )
def monitorar():
    alerta_enviado = False

    with Progress() as progress:
        tarefa_cpu = progress.add_task("[cyan]Monitorando CPU...", total=100)
        tarefa_mem = progress.add_task("[magenta]Memória", total=100)
        while True:
            # Pega os dados 
            uso_cpu = psutil.cpu_percent(interval=1)
            memoria = psutil.virtual_memory().percent
            # Atualiza as barras de progresso
            progress.update(tarefa_cpu, completed=uso_cpu)
            progress.update(tarefa_mem, completed=memoria)

            # Lógica de Alerta
            if uso_cpu > 80 and not alerta_enviado:
                enviar_alerta(uso_cpu)
                alerta_enviado = True # Evita múltiplos alertas
            elif uso_cpu < 70:
                alerta_enviado = False
            #Limpa e mostra o painel bonito
            os.system('clear')
            console.print(Panel(f"[bold green]Status do Sistema[/bold green]\n"
                                f"CPU: [bold cyan]{uso_cpu}%[/bold cyan]\n"
                                f"Memória: [bold magenta]{memoria}%[/bold magenta]",
                                title="[bold blue]MacBook Air M5[/bold blue]",
                                subtitle="[yellow]Pressione Ctrl+C para sair[/yellow]"))

if __name__ == "__main__":
    try:
        monitorar()
    except KeyboardInterrupt:
        console.print("\n[bold red]Monitoramento encerrado. Até a próxima![/bold red]")
                        