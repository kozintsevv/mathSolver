from sympy.abc import *
from sympy import Matrix, Symbol,shape,linsolve

def linear_combination():

    vectors=Matrix([[1, -1, 3],[1, 0, 1],[0, 1, 1]])
    len_vectors=shape(vectors)[0]
    k=[]
    for i in range(0,len_vectors):
        k.append(Symbol(f'k{i}'))

    M = Matrix([[3, -2, 4]])
    multiplied_vectors=[list(vectors.row(i) *k[i]) for i in range(0,len_vectors)]
    vectors2=Matrix(multiplied_vectors)
    matrix=Matrix([list(vectors2.col(i)) for i in range(0,len_vectors)])
    roots=linsolve([matrix, M])
    print(roots)

linear_combination()


