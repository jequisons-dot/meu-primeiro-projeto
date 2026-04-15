import psutil
import time
import os

def monitorar():
    print("🚀 Iniciando monitoramento de saúde do Mac...")
    time.sleep(1)
    
    try:
        while True:
            # Limpa a tela do terminal para ficar legível
            os.system('clear')
            
            # Pega o uso da CPU e Memória
            uso_cpu = psutil.cpu_percent(interval=1)
            memoria = psutil.virtual_memory().percent
            
            print(f"--- STATUS DO SISTEMA ---")
            print(f"Uso de CPU: {uso_cpu}%")
            print(f"Uso de Memória: {memoria}%")
            print(f"--------------------------")
            
            if uso_cpu > 70:
                print("⚠️ ALERTA: Uso de CPU elevado!")
            else:
                print("✅ Tudo normal por aqui.")
                
            print("\n(Pressione Ctrl+C para encerrar)")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nMonitoramento finalizado.")

if __name__ == "__main__":
    monitorar()