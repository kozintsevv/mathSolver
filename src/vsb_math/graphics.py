import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy.abc import x, y, z


def draw_domain(f):
    f = sympify(f)
    f_numeric = lambdify((x, y), f, "numpy")
    # Создаем данные для графика
    x_values = np.linspace(-5, 5, 1000)
    y_values = np.linspace(-5, 5, 1000)
    x_grid, y_grid = np.meshgrid(x_values, y_values)
    f_values = f_numeric(x_grid, y_grid)

    plt.contourf(x_grid, y_grid, f_values, cmap="autumn", alpha=0.5)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("2D Projection on XY Plane")

    plt.xticks(np.arange(-5, 6, 1))
    plt.yticks(np.arange(-5, 6, 1))

    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    plt.savefig("graphics_output/xy_projection.png")
    plt.close()


if __name__ == "__main__":
    # draw_domain("sqrt(x**2 - 1) + sqrt(1 - y**2)")
    # draw_domain("log(x + y,10)")
    # draw_domain("sqrt(x - y) / (x + y)")
    draw_domain("sqrt((x**2 + y**2 - x) / (2 * x - x**2 - y**2))")
