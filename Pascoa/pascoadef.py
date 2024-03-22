def aurea(year):
    return year % 19 + 1


def sec(year):
    return year // 100 + 1


def correcao_x(year):
    sec_val = sec(year)
    return (3 * sec_val // 4) - 12


def correcao_z(year):
    sec_val = sec(year)
    return (8 * sec_val + 5) // 25 - 5


def epacta(year):
    aurea_val = aurea(year)
    correcao_x_val = correcao_x(year)
    correcao_z_val = correcao_z(year)
    epacta_val = (11 * aurea_val + 20 + correcao_z_val - correcao_x_val) % 30

    if (epacta_val == 25 and aurea_val > 11) or epacta_val == 24:
        epacta_val += 1

    return epacta_val


def lua(year):
    epacta_val = epacta(year)
    lua_val = 44 - epacta_val
    if lua_val < 21:
        lua_val += 30
    return lua_val


def domingo(year):
    correcao_x_val = correcao_x(year)
    domingo_val = (5 * year) // 4 - (correcao_x_val + 10)
    return domingo_val


def mes(lua):
    if lua > 31:
        lua -= 31
        print(lua, "de abril")
    else:
        print(lua, "de março")


def calculo_pascoa(year):
    lua_val = lua(year)
    domingo_val = domingo(year)
    lua_val = (lua_val + 7) - ((domingo_val + lua_val) % 7)
    mes(lua_val)


year = int(input("Digite o ano: "))
calculo_pascoa(year)
