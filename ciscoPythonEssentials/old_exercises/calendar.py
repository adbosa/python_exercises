# Programa para trabalhar com calculos de datas no calendário

# Testar se a data é válida
# Testar se é ano bisexto
# Retornar quantos dias tem determinado mês
# Dizer qual é o dia do ano dado um ano, mês e dia alvo

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def validadorDeData(ano = 1, mes = 1, dia = 1):
    if type(ano) != int:
        return None
    if type(mes) != int or not 0 < mes < 13:
        return None
    #modificadorDeAnoBisexto(ano)
    if type(dia) != int or not 0 < dia <= dias_por_mes[mes - 1]:
        return None
    return True

def diasDoMes(ano, mes):
    if not validadorDeData(ano = ano , mes = mes):
        return None
    modificadorDeAnoBisexto(ano)
    return dias_por_mes[mes - 1]

def ehAnoBisexto(ano):
    #Valida se a data é anterior a regra atual
    ano_inicial = 1582
    if not validadorDeData(ano = ano):
        return None
    if ano < ano_inicial:
        return False

    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True

def modificadorDeAnoBisexto(ano):
    if ehAnoBisexto(ano):
        dias_por_mes[1] = 29
    else:
        dias_por_mes[1] = 28
    return

def diaDoAno(ano, mes, dia):
    dias_do_ano = 0
    if not validadorDeData(ano, mes, dia):
        return None
    #modificadorDeAnoBisexto(ano)
    for x in range(mes - 1):
        dias_do_ano += diasDoMes(ano, x + 1)
    dias_do_ano += dia
    return dias_do_ano
