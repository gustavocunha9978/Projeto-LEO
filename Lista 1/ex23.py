height = float(input("Qual a sua altura? "))
shadow = float(input("Qual o comprimento da sua sombra? "))
building_shadow = float(input("Qual o comprimento da sombra do prédio? "))

building = building_shadow * height 

building_f = building / shadow

print(f"{building_f:.2f}")