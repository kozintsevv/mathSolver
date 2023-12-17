from sympy import integrate, sympify
from sympy.abc import *
from expression import Expression


class DoubleIntegral(Expression):
    def __init__(self, expression, interval_x, interval_y):
        super().__init__(expression)
        self.lower_interval_x, self.upper_interval_x = sympify(interval_x)
        self.lower_interval_y, self.upper_interval_y = sympify(interval_y)

    def calculate(self):
        self.integrate_y = integrate(self.expression, y)
        print(f'Интегрирование по y :{self.integrate_y}')

        self.upper_sub_y = self.integrate_y.subs(y, self.upper_interval_y)
        self.lower_sub_y = self.integrate_y.subs(y, self.lower_interval_y)

        self.subtract_y = self.upper_sub_y - self.lower_sub_y
        print(f'Разность по y: {self.upper_sub_y}-{self.lower_sub_y}')

        self.integrate_x = integrate(self.subtract_y, x)
        print(f'Интегрирование по x: {self.integrate_x}')

        self.upper_sub_x = self.integrate_x.subs(x, self.upper_interval_x)
        self.lower_sub_x = self.integrate_x.subs(x, self.lower_interval_x)

        self.subtract_x = self.upper_sub_x - self.lower_sub_x
        print(f'Разность по х: {self.upper_sub_x}-{self.lower_sub_x}')

        print(f'Ответ:{self.subtract_x}')
