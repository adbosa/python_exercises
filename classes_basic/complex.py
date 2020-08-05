''' Receives two parts of a complex number and displays the same as a+bj '''

def main():
    cpx1 = Complex(2,3)
    print(cpx1)

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def sum(self):
        pass
    def multiplication(self):
        pass
    def __str__(self):
        return (f'{self.real}+{self.imaginary}j')

main()
