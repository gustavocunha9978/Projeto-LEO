num_pao = int(input("Numero de pães: "))
num_broa = int(input("Numero de broas: "))

valor_total_vendas = num_pao * 0.12 + num_broa * 1.5

valor_poupanca = valor_total_vendas * 0.1

print(valor_total_vendas , valor_poupanca)