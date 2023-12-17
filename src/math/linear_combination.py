from sympy.abc import *
from sympy import Matrix,Symbol

k1=Symbol('k1')
k2=Symbol('k2')
k3=Symbol('k3')

M=Matrix([[3,-2,4]])
M1=Matrix([[1,-1,3]])
M2=Matrix([[1,0,1]])
M3=Matrix([[0,1,1]])

Mk=M1*k1+M2*k2+M3*k3
# print(Mk.det())

Mr=Matrix([[M1[0],M2[0],M3[0]],[M1[1],M2[1],M3[1]],[M1[2],M2[2],M3[2]]])
print(Mr.inv())