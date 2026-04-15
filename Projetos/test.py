# Script para cálculo de média de notas - ADS 2026

nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

media = (nota1 + nota2) / 2

print("-" * 20)
print(f"Jequison, sua média foi: {media:.1f}")

if media >= 6.0:
    print("Resultado: APROVADO! 🎉")
else:
    print("Resultado: REPROVADO. 📚")
print("-" * 20) 