quantidade = int(input("Quantas unidades você deseja comprar? "))
preco_unitario = 100.00
valor_total = quantidade * preco_unitario
if quantidade >=10:
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f"Você ganhou 10% de desconto!")
    print(f"Valor original: R$ {valor_total: .2f}")
    print(f"Desconto: R$ {desconto:.2f}")
else:
    valor_final = valor_total
    print("Valor pago integralmente (sem desconto).")
    print(f"Valor final da compra: R$ {valor_final:.2f}")