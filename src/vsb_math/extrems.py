from sympy import solve, diff
from sympy.abc import *
from vsb_math.expression import Expression


class Extrems(Expression):
    def __init__(self, expression):
        super().__init__(expression)

    def system(self):
        self.deff_y = self.expression.diff(y)
        self.deff_x = self.expression.diff(x)
        self.system = [self.deff_y, self.deff_x]

    def roots(self):
        self.roots = solve(self.system, x, y, dict=True)
        self.matrixes = [[] for i in range(0, len(self.roots))]

    def second_deffs(self):
        self.deff_y_y = self.deff_y.diff(y)
        self.deff_x_x = self.deff_x.diff(x)
        self.deff_y_x = self.deff_y.diff(x)
        self.deffs = [self.deff_x_x, self.deff_y_x, self.deff_y_x, self.deff_y_y]

    def subs_points(self):
        index = 0
        for point in self.roots:
            for deff in self.deffs:
                substitution = deff.subs(point)
                self.matrixes[index].append(substitution)
            index += 1

    def find_extrems(self):
        self.system()
        self.roots()
        self.second_deffs()
        self.subs_points()

        return self.roots


if __name__ == "__main__":
    extrem = Extrems("x**2+4*y+15").find_extrems()
