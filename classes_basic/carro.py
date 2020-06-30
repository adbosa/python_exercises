def main():
    carro1 = Carro('brasília', 1968, 'amarela', 80)
    carro2 = Carro('fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_max):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
        self.velocidade = 0
        self.velocidade_max = velocidade_max

    def imprima(self):
        if self.velocidade == 0: # Carro parado, podesse ver o ano
            print(f'{self.modelo.capitalize()} {self.cor} {self.ano}')
        elif self.velocidade < self.velocidade_max:
            print(f'{self.modelo.capitalize()} {self.cor} indo a {self.velocidade} Km/h')
        else:
            print(f'{self.modelo.capitalize()} {self.cor} indo muito raaaaaaaaaaaaaaaaaaaapido!')

    def acelere(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidade_max:
            self.velocidade = self.velocidade_max
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()

main()
