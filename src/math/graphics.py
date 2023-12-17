import matplotlib.pyplot as plt
import numpy as np


def draw(x, y, z):
    plt.contourf(x, y, z, cmap='autumn', alpha=0.5)


# Создаем данные для графика
x = np.linspace(-3, 3, 1000)
y = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(x, y)
p = np.sqrt(x ** 2 - 1) + np.sqrt(1 - y ** 2)
z = np.log10(x + y)
n = np.sqrt(x - y) / (x + y)
l = np.sqrt((x ** 2 + y ** 2 - x) / (2 * x - x ** 2 - y ** 2))
functions = [p, z, n, l]


for func in functions:
    draw(x, y, func)

# Настройка меток и заголовка
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Projection on XY Plane')

# Установка шага деления для осей X и Y
plt.xticks(np.arange(-3, 4, 1))
plt.yticks(np.arange(-3, 4, 1))

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Сохраняем график в файл
# plt.savefig('xy_projection.png')

# Показываем график (необязательно)
plt.show()
