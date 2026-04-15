temp = float(input("Digite a temperatura em graus Celcius: "))
if temp < 15:
    print("Classificação: Frio")
elif 15 <= temp <= 25:
    print("Classificação: Agradável")
else: 
    print("Classificação: Quente")