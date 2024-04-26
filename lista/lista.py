lista = [900, 1000, 2000, 700, 1500]
lista_2 = []
remover = [1, 2, 3]


for i in range(len(lista)):
    if i not in remover:
        lista_2.append(lista[i])
          
print (lista_2)
        
        
        # for i in lista:
#     if i > 1000:
#         lista_2.append(i)

# print(lista_2)

# x = sum(lista_2)
# print(x)