"""
ФАЙЛ: КІЛЬКА КОТІВ (РІЗНІ k)

Що ми робимо:
- моделюємо кількох котів на різних позиціях драбини
- будуємо їх траєкторії

Математика:

cat_x = x(1 - k)
cat_y = k * sqrt(L² - x²)

k визначає:
- де сидить кіт
- як виглядає його траєкторія
"""

import math
import matplotlib.pyplot as plt

L = 10
steps = 100

# різні положення кота
k_values = [0.2, 0.5, 0.8]

for k in k_values:
    x_points = []
    y_points = []

    for i in range(steps + 1):
        x = L * (i / steps)
        y = math.sqrt(L**2 - x**2)

        cat_x = x * (1 - k)
        cat_y = y * k

        x_points.append(cat_x)
        y_points.append(cat_y)

    plt.plot(x_points, y_points, label=f"k = {k}")

plt.title("Траєкторії різних котів")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

plt.show()