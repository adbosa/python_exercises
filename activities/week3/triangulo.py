''' Exercício 1: Uma classe para triângulos

Defina a classe Triangulo cujo construtor recebe 3 valores inteiros
correspondentes aos lados a, b e c de um triângulo. A classe triângulo
também deve possuir um método perimetro, que não recebe parâmetros e
devolve um valor inteiro correspondente ao perímetro do triângulo.

Exercício 2: Tipos de triângulos

Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado()
que devolve uma string dizendo se o triângulo é:
isósceles (dois lados iguais)
equilátero (todos os lados iguais)
escaleno (todos os lados diferentes)
Note que se o triângulo for equilátero, a função não deve devolver isóceles.
'''
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return(self.a + self. b + self.c)

    def tipo_lado(self):
        if  self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return 'isósceles'
        else:
            return 'escaleno'
    
