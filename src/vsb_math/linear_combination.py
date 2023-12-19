from sympy.abc import *
from sympy import Matrix, Symbol, shape, linsolve


class LinearCombination:
    def __init__(self, vectors, equal_vector):
        self.vectors = vectors
        self.equal_vector = equal_vector

    def calculate(self):
        self.vectors = Matrix(self.vectors)
        self.M = Matrix(self.equal_vector)

        self.len_vectors = shape(self.vectors)[0]

        self.k = [Symbol(f'k{i + 1}') for i in range(0, self.len_vectors)]

        self.multiplied_vectors = [list(self.vectors.row(i) * self.k[i]) for i in range(0, self.len_vectors)]
        print(f'{self.equal_vector}={self.multiplied_vectors}')

        self.vectors2 = Matrix(self.multiplied_vectors)
        self.matrix = Matrix([list(self.vectors2.col(i)) for i in range(0, self.len_vectors)])
        print(self.matrix)
        self.roots = linsolve([self.matrix, self.M])
        print(self.roots)


if __name__=='__main__':
    linear_combination=LinearCombination([[1, -2, 1],[-1, 1, 0],[1, 4, 2]],[[1, 3, 3]]).calculate()
    linear_combination=LinearCombination([[1, -1, 3],[1, 0, 1],[0, 1, 1]],[[3, -2, 4]]).calculate()
    linear_combination=LinearCombination([[1, 1, 3],[-1, 0, -2],[2, 2, 7]],[[1, 1, 2]]).calculate()
    linear_combination=LinearCombination([[1, -2, 1],[-1, 1, 0],[1, 4, 2]],[[1, 3, 3]]).calculate()


