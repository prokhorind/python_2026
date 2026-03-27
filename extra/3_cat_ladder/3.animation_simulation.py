"""
ФАЙЛ 3: АНІМАЦІЯ

Що ми робимо:
- Показуємо, як драбина рухається в часі
- На кожному кадрі рахуємо координати

Математика:
x = L * t
y = sqrt(L² - x²)

Кіт:
cat_x = x(1 - k)
cat_y = y * k

Тобто:
- система змінюється з часом (t)
- але обмеження завжди виконується
"""

import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 10
steps = 100
k = 0.5

fig, ax = plt.subplots()

def update(frame):
    ax.clear()

    # параметр часу (нормалізований)
    t = frame / steps

    # положення основи
    x = L * t

    # обчислення висоти через constraint
    y = math.sqrt(L**2 - x**2)

    # позиція кота
    cat_x = x * (1 - k)
    cat_y = y * k

    # малюємо драбину (лінія від (0,y) до (x,0))
    ax.plot([0, x], [y, 0])

    # малюємо кота
    ax.scatter(cat_x, cat_y)

    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_title("Анімація руху драбини")

ani = animation.FuncAnimation(fig, update, frames=steps, interval=100)

plt.show()