p_capacidade = 350
m_capacidade = 600
g_capacidade = 2000

p_quantidade =  int(input("quantos refrigerantes vai querer P? "))
m_quantidade =  int(input("quantos refrigerantes vai querer M? "))
g_quantidade =  int(input("quantos refrigerantes vai querer G? "))

litros_p = p_quantidade * p_capacidade / 1000
litros_m = m_quantidade * m_capacidade / 1000
litros_g = g_quantidade * g_capacidade / 1000

total = litros_p + litros_m + litros_g

print (total)