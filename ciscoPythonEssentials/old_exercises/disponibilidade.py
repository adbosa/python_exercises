# Cria um lista tridimencinal onde podemos encontrar cada quarto como livre
# (True) ou ocupado (False) em um hotel que tem três torres, 15 andares por
# torre e vinte quartos por andar

quartos = [[[True for quarto in range(20)] for andares in range(15)] for torres
in range(3)]

# Imprima a tabela de quartos
for torre in range(len(quartos)):
    print(f"Torre {torre +1}")
    for andar in range(len(quartos[torre])):
        print(f"Andar {andar +1}")
        for quarto in range(len(quartos[torre][andar])):
            print(f"Quarto {quarto + 1}", end=" ")
            if quartos[torre][andar][quarto]:
                print("Livre.")
            else:
                print("Ocupado.")
        input()

