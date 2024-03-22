year = int(input("Digite o ano: "))

aurea = year % 19 + 1
sec = year // 100 + 1
correcao_x = (3 * sec // 4) - 12
correcao_z = (8 * sec + 5) // 25 - 5
epacta = (11 * aurea + 20 + correcao_z - correcao_x) % 30

if (epacta == 25 and aurea > 11) or (epacta == 24):
    epacta += 1

lua = 44 - epacta 
if lua < 21:
    lua += 30

domingo = (5 * year) // 4  - (correcao_x + 10)
lua = (lua + 7) - ((domingo + lua) % 7)

if lua > 31:
    lua -= 31
    print(lua, "de abril")
else:
    print(lua, "de março")
    
