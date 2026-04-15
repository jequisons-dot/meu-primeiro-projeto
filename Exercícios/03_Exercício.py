numero = int(input("Digite um numero inteiro para ver na tabuada: "))
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")