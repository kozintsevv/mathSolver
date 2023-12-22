from sympy import integrate, sympify
from sympy.abc import *
from vsb_math.expression import Expression


class DoubleIntegral(Expression):
    def __init__(self, expression, interval_x, interval_y):
        super().__init__(expression)
        self.lower_interval_x, self.upper_interval_x = sympify(interval_x)
        self.lower_interval_y, self.upper_interval_y = sympify(interval_y)

    def calculate(self):
        self.integrate_y = integrate(self.expression, y)

        self.upper_sub_y = self.integrate_y.subs(y, self.upper_interval_y)
        self.lower_sub_y = self.integrate_y.subs(y, self.lower_interval_y)

        self.subtract_y = self.upper_sub_y - self.lower_sub_y

        self.integrate_x = integrate(self.subtract_y, x)

        self.upper_sub_x = self.integrate_x.subs(x, self.upper_interval_x)
        self.lower_sub_x = self.integrate_x.subs(x, self.lower_interval_x)

        self.subtract_x = self.upper_sub_x - self.lower_sub_x


if __name__ == "__main__":
    expression = DoubleIntegral("x**2", "(1,2)", "(0,1/x)")
    expression.calculate()
