inicio = int(input("Começar em: "))
fim = int(input("Terminar em: "))
passo = int(input("Pular de quanto em quanto: "))

for i in range(inicio, fim + 1, passo):
    print(i)
