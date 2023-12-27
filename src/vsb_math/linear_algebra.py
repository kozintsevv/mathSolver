from sympy.abc import *
from sympy import (
    Matrix,
    Symbol,
    shape,
    linsolve,
    sympify,
    det,
)
from aiogram.types import Message


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
    # Создаем матрицу
    original_matrix = [1, -1, 2, 2], [-2, 3, -5, -2], [-1, 2, -1, 1], [2, -4, 5, -1]

    # original_matrix = Matrix([[1, 2, 1, 2], [-1, -3, 0, -1], [0, 2, -1, 1], [0, 3, -2, 1]])
    # Вычисляем обратную матрицу с выводом максимально полной информации
    inverse_matrix_steps = invert_matrix(original_matrix)


from sympy import Matrix, eye


async def invert_matrix(message):
    matrix = Matrix(list(sympify(message.text)))
    n = matrix.shape[0]

    # Создаем расширенную матрицу [A | I], где A - исходная матрица, I - единичная матрица
    augmented_matrix = Matrix.hstack(matrix, eye(n))

    for i in range(n):
        # Приводим главный элемент текущей строки к единице
        diag_element = augmented_matrix[i, i]
        augmented_matrix.row_op(i, lambda row, j: row / diag_element)
        await message.answer(
            f"\nШаг {i + 1}: Приведение главного элемента {i + 1} строки к единице\nМножитель: 1/{diag_element}\n{augmented_matrix}"
        )

        # Обнуляем элементы под и над текущим главным элементом
        for j in range(n):
            if i != j:
                multiplier = augmented_matrix[j, i]
                augmented_matrix.row_op(
                    j, lambda row, k: row - multiplier * augmented_matrix[i, k]
                )
                if multiplier != 0:
                    await message.answer(
                        f"Шаг {i + 1}: Обнуление элементов под и над главным элементом {i + 1}\nОтнимаем от {j+1} строки строку {i+1} умноженную на {multiplier}\n{augmented_matrix}"
                    )

    # Выделяем обратную матрицу из расширенной матрицы
    inverse_matrix = augmented_matrix[:, n:]

    await message.answer(f"Обратная матрица:\n{inverse_matrix}")
