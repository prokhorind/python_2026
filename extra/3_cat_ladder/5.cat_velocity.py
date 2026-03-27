"""
ФАЙЛ: ШВИДКІСТЬ КОТА

Що ми робимо:
- рахуємо, як змінюється швидкість кота під час руху
- показуємо, що рух НЕ рівномірний

Математика:

1. Маємо точки траєкторії:
   (x1, y1), (x2, y2)

2. Відстань між ними:
   d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

3. Швидкість:
   v = d / dt

(у нас dt однаковий → можна аналізувати просто d)
"""

import math
import matplotlib.pyplot as plt

L = 10
steps = 200
k = 0.5

points = []

# 🔹 1. Генеруємо точки траєкторії
for i in range(steps + 1):
    x = L * (i / steps)
    y = math.sqrt(L**2 - x**2)

    cat_x = x * (1 - k)
    cat_y = y * k

    points.append((cat_x, cat_y))

# 🔹 2. Рахуємо "швидкість" (відстань між точками)
velocities = []

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    velocities.append(d)

# 🔹 3. Візуалізація швидкості
plt.plot(velocities)
plt.title("Швидкість кота (зміна по кроках)")
plt.xlabel("Крок")
plt.ylabel("Швидкість")
plt.grid()

plt.show()