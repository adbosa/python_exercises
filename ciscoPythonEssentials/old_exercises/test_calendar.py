import calendar

# Testar a aplicação de calendário

# Dados para teste
testar_anos   = [2000, 2021, 2004, 1988, 2006, 2009, "21", 2021, 2021]
testar_meses  = [  12,   11,    2,    5,   10,    2,   23,   50,   11]
testar_dias   = [  31,   10,   29,   29,   31,   29,   10,   10,   99]
base_de_teste = [testar_anos, testar_meses, testar_dias]

def testarValidadorDeDatas():
    print("#"*20)
    print("Testar validador de datas.")
    print("#"*20)

    for x in range(len(base_de_teste[0])):
        teste = []
        print(f"Teste {x + 1} ", end="==> ")
        for y in range(len(base_de_teste)):
            teste.append(base_de_teste[y][x])
        ano = teste[0]
        mes = teste[1]
        dia = teste[2]
        esperado = [True,True,True,True,True,None,None,None,None]

        if calendar.validadorDeData(ano, mes, dia) == esperado[x]:
            print("Passou")
        else:
            print(f"Falhou - [{teste}]")

    return

def testarAnoBisexto():
    print("#"*20)
    print("Testar validação de ano bisexto.")
    print("#"*20)

    esperado = [True,False, True, True, False, False, None, False, False]

    for x in range(len(base_de_teste[0])):
        teste = []
        print(f"Teste {x + 1}", end="==> ")
        if calendar.ehAnoBisexto(base_de_teste[0][x]) == esperado[x]:
            print("Passou")
        else:
            print(f"Falhou. ({base_de_teste[0][x]})")
    return

def testarDiasDoMes():
    print("#"*20)
    print("Testar retorno do dias por mês.")
    print("#"*20)
    resultados = [31, 30, 29, 31, 31, 28, None, None, 30]
    for x in range(len(base_de_teste[0])):
        teste = []
        print("Teste 1", end="==> ")
        for y in range(len(base_de_teste) - 1):
            teste.append(base_de_teste[y][x])
        if calendar.diasDoMes(teste[0],teste[1]) == resultados[x]:
            print("Passou")
        else:
            print(f"Falhou. ({teste})")
    return

def testarDiaDoAno():
    print("#"*20)
    print("Testar posição do dia no ano.")
    print("#"*20)
    resultados = [ 366,  314,   60,  150,  304, None, None, None, None]

    for x in range(len(base_de_teste[0])): # Pega itens dentro das listas
        teste = []
        for y in range(len(base_de_teste)): # Pega cada lista da matriz
            teste.append(base_de_teste[y][x])
        print(f"Teste {x + 1}", end="==> ")
        if calendar.diaDoAno(teste[0], teste[1], teste[2]) == resultados[x]:
            print("Passou")
        else:
            print("Falhou")
    return

testarValidadorDeDatas()
print()
testarDiasDoMes()
print()
testarAnoBisexto()
print()
testarDiaDoAno()
