'''
## Atributos
1. numerador; 2. denominador;

## Métodos
*somar; *subtrair; *multiplicar; *dividir; *inverter; *negar; *simplificar;
'''

class Fracao:

    def __init__(self, num, den):
        self.numerador = num
        if den == 0:
            return 'Denominador não pode ser igual a zero'
        else:
            self.denominador = den

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def __erp__(self):
        return f'Fracao({self.numerador}, {self.denominador})'

    def inverter(self):
        return Fracao(self.denominador, self.numerador)

    def negar(self):
        return Fracao(-self.numerador, self.denominador)


    def somar(self, outra):
        if self.denominador == outra.denominador:
            num = self.numerador + outra.numerador
            den = self.denominador
            return Fracao(num, den)
        num = self.numerador * outra.denominador + outra.numerador * self.denominador
        den = self.denominador * outra.denominador
        return Fracao(num, den)

    def subtrair(self, outra):
        return self.somar(outra.negar())

    def multiplicar(self, outra):
        num = self.numerador * outra.numerador
        den = self.denominador * outra.denominador
        return Fracao(num, den)

    def dividir(self, outra):
        return self.multiplicar(outra.inverter())

    def simplificar(self):
        pass

