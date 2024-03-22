year = int(input("Digite o ano: "))

golden = year % 19 + 1
century = year // 100 + 1
correction_x = (3 * century // 4) - 12
correction_z = (8 * century + 5) // 25 - 5
epact = (11 * golden + 20 + correction_z - correction_x) % 30

if (epact == 25 and golden > 11) or (epact == 24):
    epact += 1

moon = 44 - epact
if moon < 21:
    moon += 30

sunday = (5 * year) // 4  - (correction_x + 10)
moon = (moon + 7) - ((sunday + moon) % 7)

if moon > 31:
    moon -= 31
    print(moon, "of April")
else:
    print(moon, "of March")