"""
ФАЙЛ 2: ПОБУДОВА ГРАФІКА

Що ми робимо:
- Генеруємо точки траєкторії кота
- Візуалізуємо їх

Математика така ж:
x² + y² = L²
cat_x = x(1 - k)
cat_y = k * sqrt(L² - x²)

Результат:
- бачимо реальну форму траєкторії (трактрису)
"""

import math
import matplotlib.pyplot as plt

L = 10
steps = 100
k = 0.5

x_points = []
y_points = []

for i in range(steps + 1):
    # параметр руху
    x = L * (i / steps)

    # обмеження довжини драбини
    y = math.sqrt(L**2 - x**2)

    # позиція кота
    cat_x = x * (1 - k)
    cat_y = y * k

    x_points.append(cat_x)
    y_points.append(cat_y)

# Малюємо траєкторію
plt.plot(x_points, y_points)
plt.title("Траєкторія кота")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

plt.show()