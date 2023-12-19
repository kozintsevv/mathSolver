from sympy import sympify

class Expression:
    def __init__(self, expression):
        self.expression = sympify(expression)
