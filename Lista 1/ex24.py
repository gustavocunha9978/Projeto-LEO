litros_refresco = float(input("Digite a quantidade de litros: "))

litros_agua = (litros_refresco * 8) / (8 + 2)
litros_suco = (litros_refresco * 2) / (2 + 8)

print(f"{litros_agua} litros de água")
print(f"{litros_suco} litros de suco ")