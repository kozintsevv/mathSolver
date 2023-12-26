from sympy.abc import *
from sympy import (
    Matrix,
    Symbol,
    shape,
    linsolve,
    sympify,
    det,
)


class LinearAlgebra:
    def __init__(self):
        self.with_matrix = ""
        self.sum_diagonals = ""
        self.sum = 0
        self.sub = ""

    def det_laplace(self, M):
        n = M.shape[0]
        if n == 1:
            return M[0]
        elif n == 2:
            return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        elif n == 3:
            m = (
                M[0, 0] * M[1, 1] * M[2, 2]
                + M[0, 1] * M[1, 2] * M[2, 0]
                + M[0, 2] * M[1, 0] * M[2, 1]
                - M[0, 2] * M[1, 1] * M[2, 0]
                - M[0, 0] * M[1, 2] * M[2, 1]
                - M[0, 1] * M[1, 0] * M[2, 2]
            )
            self.m = m
            self.sum_diagonals += f"({M[0, 0]} * {M[1, 1]} * {M[2, 2]}) + ({M[0, 1]} * {M[1, 2]} * {M[2, 0]})+ ({M[0, 2]} * {M[1, 0]} * {M[2, 1]}) - ({M[0, 2]} * {M[1, 1]} * {M[2, 0]}) - ({M[0, 0]} * {M[1, 2]} * {M[2, 1]}) - ({M[0, 1]} * {M[1, 0]} * {M[2, 2]}) = {m}|"
            return m
        else:
            self.sum = 0
            row = self.find_most_zeros_row(M)
            for i in range(n):
                if M[row, i] != 0:
                    self.with_matrix += (
                        f"(-1)** ({i+1} * {M[row,i]}) * {M.minor_submatrix(row,i)}|"
                    )
                    expression = (
                        (-1) ** (i + 1)
                        * M[row, i]
                        * self.det_laplace(M.minor_submatrix(row, i))
                    )
                    self.sub += f"({(-1)**(i+1)*M[row,i]} * {self.m})|"
                    self.sum += expression
            return self.sum

    def find_most_zeros_row(self, M):
        zeros_in_row = []
        n = M.shape[0]
        for i in range(n):
            arr = list(M.row(i))
            zeros_in_row.append(arr.count(0))
        max_value = max(zeros_in_row)
        return zeros_in_row.index(max_value)

    def inversion(self, rows):
        M = Matrix(list(sympify(rows)))
        return M.inv()


class LinearCombination:
    def __init__(self, vectors, equal_vector):
        self.vectors = sympify(vectors)
        self.equal_vector = sympify(equal_vector)

    def calculate(self):
        self.vectors = Matrix(self.vectors)
        self.M = Matrix(self.equal_vector)

        self.len_vectors = shape(self.vectors)[0]

        self.k = [Symbol(f"k{i + 1}") for i in range(0, self.len_vectors)]

        self.multiplied_vectors = [
            list(self.vectors.row(i) * self.k[i]) for i in range(0, self.len_vectors)
        ]

        self.vectors2 = Matrix(self.multiplied_vectors)
        self.matrix = Matrix(
            [list(self.vectors2.col(i)) for i in range(0, self.len_vectors)]
        )
        self.roots = linsolve([self.matrix, self.M])
        print(self.roots)


if __name__ == "__main__":
    matrix = Matrix(
        list(sympify("[1, 2, 0, 1], [0, 0, 1, 3], [0, 1, -1, 1], [3,-1, 3, -1]"))
    )
    # matrix = Matrix(
    #     list(sympify("[1, 2, 0, 1], [0, 0, 1, 3], [0, 0, -1, 1], [3,-1, 3, -1]"))
    # )
    matrix = Matrix(
        list(sympify("[0, -1, 1, -1], [-1, 0, 1, 0], [-1, 1, 1, 3], [-1, 3, 3, 2]"))
    )
    lin_alg = LinearAlgebra()
    lin_alg.det_laplace(matrix)
    print(lin_alg.sub)
