"""
ФАЙЛ: ЗБЕРЕЖЕННЯ ГРАФІКА У PNG

Що ми робимо:
- будуємо траєкторію кота
- зберігаємо графік у файл (PNG)

Це вже реальний use-case:
- можна вставити у звіт
- можна відправити як результат
"""

import math
import matplotlib.pyplot as plt

L = 10
steps = 100
k = 0.5

x_points = []
y_points = []

# 🔹 1. Генеруємо точки
for i in range(steps + 1):
    x = L * (i / steps)
    y = math.sqrt(L**2 - x**2)

    # позиція кота
    cat_x = x * (1 - k)
    cat_y = y * k

    x_points.append(cat_x)
    y_points.append(cat_y)

# 🔹 2. Малюємо графік
plt.plot(x_points, y_points)
plt.title("Траєкторія кота")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

# 🔹 3. Зберігаємо файл
plt.savefig("cat_trajectory.png", dpi=300)

plt.show()