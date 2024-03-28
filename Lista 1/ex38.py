from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
ano_atual = int(input("Digite o ano atual: "))

data_nascimento = datetime(ano_nascimento, 1, 1)
data_atual = datetime(ano_atual, 1, 1)

diferenca = data_atual - data_nascimento

idade_anos = diferenca.days // 365

idade_meses = diferenca.days // 30

idade_dias = diferenca.days

idade_semanas = diferenca.days // 7

print("-----------------------------------------------")
print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
print("Idade em semanas:", idade_semanas)