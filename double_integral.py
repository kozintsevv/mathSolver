from sympy import integrate, sympify, simplify
from sympy.abc import x, y

class Integral:
    def __init__(self,expression,interval_x,interval_y):
        self.expression=sympify(expression)
        self.lower_interval_x,self.upper_interval_x=sympify(interval_x)
        self.lower_interval_y,self.upper_interval_y=sympify(interval_y)

    
        

def integral():
    integ=Integral(x**2,(1,3),(0,1/x))

    integrate_y=integrate(integ.expression,y)
    print(f'Интегрирование по y :{integrate_y}')

    upper_sub_y=integrate_y.subs(y,integ.upper_interval_y)
    lower_sub_y=integrate_y.subs(y,integ.lower_interval_y)

    subtract_y=upper_sub_y-lower_sub_y
    print(f'Разность по y: {upper_sub_y}-{lower_sub_y}')

    integrate_x=integrate(subtract_y,x)
    print(f'Интегрирование по x: {integrate_x}')

    upper_sub_x=integrate_x.subs(x,integ.upper_interval_x)
    lower_sub_x=integrate_x.subs(x,integ.lower_interval_x)

    subtract_x=upper_sub_x-lower_sub_x
    print(f'Разность по х: {upper_sub_x}-{lower_sub_x}')

    print(f'Ответ:{subtract_x}')

integral()

