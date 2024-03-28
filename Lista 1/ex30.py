salario_fixo = float(input("Qual o salario fixo? "))
comissao = float(input("Qual o valor de vendas que foram feito? "))

valor_comissao = comissao * 0.04 
salario = valor_comissao + salario_fixo

print("Esse é o valor de comissão ", valor_comissao)
print("Esse é o valor do salario com a comissão", salario)