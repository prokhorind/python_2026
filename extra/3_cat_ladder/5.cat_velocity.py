"""
ФАЙЛ 4: ПАРАМЕТРИЧНА МОДЕЛЬ

Що ми робимо:
- Замість "кроків" використовуємо параметр t
- Це більш математичний підхід

Математика:

Вводимо параметр:
t ∈ [0, 1]

Тоді:
x = L * t
y = L * sqrt(1 - t²)

Кіт:
cat_x = L * t * (1 - k)
cat_y = L * k * sqrt(1 - t²)

Це і є параметричне рівняння траєкторії
"""

import math
import matplotlib.pyplot as plt

L = 10
k = 0.5

t_values = [i / 100 for i in range(101)]

x_points = []
y_points = []

for t in t_values:
    # параметрична форма
    x = L * t
    y = L * math.sqrt(1 - t**2)

    # положення кота
    cat_x = x * (1 - k)
    cat_y = y * k

    x_points.append(cat_x)
    y_points.append(cat_y)

plt.plot(x_points, y_points)
plt.title("Параметрична траєкторія кота")
plt.grid()

plt.show()