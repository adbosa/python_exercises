def liters_100km_to_miles_gallon(liters):
    km_por_litro = 100 / liters
    milhas_por_litro = km_por_litro / 1.609344
    milhas_por_galao = milhas_por_litro * 3.785411784
    return milhas_por_galao

def miles_gallon_to_liters_100km(miles):
    km_por_galao = miles * 1.609344
    km_por_litro = 3.785411784 /  km_por_galao
    return km_por_litro * 100 

### TESTES ###
def testarConversoes():
    eu2usa = [[3.9, 7.5, 10.], [60.31143162393162, 31.36194444444444,
                                     23.52145833333333]]
    usa2eu = [[60.3, 31.4, 23.5], [3.900739358761747, 7.490910297239915,
                                       10.009131205673757]]
    print("Testando do padrão europeu para estaduniense:\n")
    for teste in range(len(eu2usa[0])):
        base = eu2usa[0][teste]
        convertido = liters_100km_to_miles_gallon(base)
        gabarito = eu2usa[1][teste]

        print(f"Teste {teste +1} de {base} L/100 km para mpg.")
        imprimeResposta(gabarito, convertido)

    print("Testando do padrão estaduniense para europeu:\n")
    for teste in range(len(usa2eu[0])):
        base = usa2eu[0][teste]
        convertido = miles_gallon_to_liters_100km(base)
        gabarito = usa2eu[1][teste]

        print(f"Teste {teste +1} de {base}  mpg para L/100 km.")
        imprimeResposta(gabarito, convertido)

def imprimeResposta(esperado, recebido):
    if esperado == recebido:
        print("#"*16, "PASSOU", "#"*16)
        print(f"Resposta {recebido}. Passou.")
    else:
        print("#"*16, "FALHOU", "#"*16)
        print(f"Resposta esperada {esperado}.")
        print(f"Resposta obtida {recebido}.")
    print("#"*40,"\n")
    return

if  __name__ == "__main__":
    testarConversoes()

