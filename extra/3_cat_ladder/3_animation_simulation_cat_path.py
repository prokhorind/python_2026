import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 10
steps = 100
k = 0.5

fig, ax = plt.subplots()

# 🔹 зберігаємо шлях кота
cat_path_x = []
cat_path_y = []

def update(frame):
    ax.clear()

    # 🔹 останній кадр — точно (L, 0)
    if frame == steps - 1:
        x = L
        y = 0
    else:
        t_linear = frame / (steps - 1)

        # ease-out
        t = 1 - (1 - t_linear)**2

        x = L * t
        y = math.sqrt(L**2 - x**2)

    cat_x = x * (1 - k)
    cat_y = y * k

    # 🔹 накопичуємо шлях
    if frame == steps - 1:
        cat_path_x.append(None)
        cat_path_y.append(None)
    else:
        cat_path_x.append(cat_x)
        cat_path_y.append(cat_y)

    # драбина
    ax.plot([0, x], [y, 0], linewidth=2)

    # кіт (поточна позиція)
    ax.scatter(cat_x, cat_y, s=60)

    # 🔥 показуємо шлях (але без "зайвого хвоста назад")
    ax.plot(cat_path_x, cat_path_y, linestyle="--")

    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_title("Плавний рух драбини + траєкторія кота")

ani = animation.FuncAnimation(fig, update, frames=steps, interval=100)

plt.show()