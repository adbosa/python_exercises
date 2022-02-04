from math import sqrt

class Bhaskara:
    
    def main(self):
        ''' Prompts the user for the values of the three terms of a second
        degree equation and returns the value of "x". '''

        a = float(input('Digite um valor para "a":'))
        b = float(input('Digite um valor para "b":'))
        c = float(input('Digite um valor para "c":'))

        return self.get_roots(a, b, c)

    def get_roots(self, a, b, c):
        ''' Receive three values and returns the roots found with bhaskara. '''
        delta = self.get_delta(a, b, c)
        # Delta smaller than zero, there is not valid roots
        if delta < 0:
            return 0
        # Delta equal zero, we hare one root, bigger than, two roots
        elif delta >= 0:
            x1 = (-b + sqrt(delta)) / (2 * a)
            if delta > 0:
                x2 = (-b - sqrt(delta)) / (2 * a)
                return 2, x1, x2
            return 1, x1

    def get_delta(self, a, b, c):
        ''' Receive three values and returns delta.'''
        return b**2 - (4 * a * c)
