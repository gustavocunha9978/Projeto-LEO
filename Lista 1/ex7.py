dia = int(input("dia: "))
mes = int(input("mes: "))

while (dia < 1 or dia > 30):
    print("dia invalido!")
    dia = int(input("dia: "))
    
while (mes < 1 or mes > 12):
    print ("mes invalido!")
    mes = int(input("mes: "))
    
dias_passados = ((mes-1)*30) + dia

print (dias_passados)