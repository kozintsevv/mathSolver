from sympy import solve, diff
from sympy.abc import *
from vsb_math.expression import Expression


class Extrems(Expression):
    def __init__(self, expression):
        super().__init__(expression)

    def system(self):
        self.deff_y = self.expression.diff(y)
        self.deff_x = self.expression.diff(x)
        print(f'Производная по х: {self.deff_x}\nПроизводная по y:{self.deff_y}')
        self.system = [self.deff_y, self.deff_x]

    def roots(self):
        self.roots = solve(self.system, x, y, dict=True)
        for point in self.roots:
            print(f'({point[x]},{point[y]})')
        self.matrixes = [[] for i in range(0, len(self.roots))]

    def second_deffs(self):
        self.deff_y_y = self.deff_y.diff(y)
        self.deff_x_x = self.deff_x.diff(x)
        self.deff_y_x = self.deff_y.diff(x)
        print(f'Вторая производная по х от {self.deff_x}: {self.deff_x_x}')
        print(f'Вторая производная по y от {self.deff_x}: {self.deff_y_x}')
        print(f'Вторая производная по y от {self.deff_y}: {self.deff_y_y}')
        self.deffs = [self.deff_x_x, self.deff_y_x, self.deff_y_x, self.deff_y_y]

    def subs_points(self):
        index = 0
        for point in self.roots:
            for deff in self.deffs:
                substitution = deff.subs(point)
                self.matrixes[index].append(substitution)
            index += 1
        print(f"Подставляем точки: {self.matrixes}")

    def extrems(self):
        index = 0
        for matrix in self.matrixes:
            delta2 = matrix[0] * matrix[3] - matrix[1] * matrix[2]
            delta1 = matrix[0]
            if delta2 > 0:
                print(f'Локальный минимум в точке {self.roots[index]}') if delta1 > 0 else print(f'Локальный максимум в точке {self.roots[index]}')
            elif delta2 < 0:
                print(f'{self.roots[index]} не явялется экстремумом')
            else:
                print('Нельзя решить этим способом')
            index += 1

    def find_extrems(self):
        self.system()
        self.roots()
        self.second_deffs()
        self.subs_points()
        self.extrems()

        return self.roots


if __name__ == '__main__':
    extrem = Extrems('x**2+4*y+15').find_extrems()
