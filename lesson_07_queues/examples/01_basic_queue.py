# Приклад 1: Основи роботи з чергою

print("=== ЧЕРГА - ОСНОВИ ===")

from collections import deque

# Створюємо чергу за допомогою deque
queue = deque()

print("1. Створили порожню чергу")
print(f"Черга: {list(queue)}")
print(f"Чи порожня черга? {len(queue) == 0}")

# Додаємо елементи (enqueue операція)
print("\n2. Додаємо людей до черги в магазині:")

customers = ["Анна", "Борис", "Віра", "Григорій", "Дарина"]

for customer in customers:
    queue.append(customer)  # enqueue операція
    print(f"До черги приєднався: {customer}")
    print(f"Черга зараз: {list(queue)}")
    print(f"Розмір черги: {len(queue)}")
    print()

# Дивимось на першого в черзі (front операція)
print("3. Дивимось на першого в черзі:")
if queue:
    first_customer = queue[0]  # front операція
    print(f"Перший в черзі: {first_customer}")
    print(f"Черга не змінилась: {list(queue)}")

# Дивимось на останнього в черзі (rear операція)
if queue:
    last_customer = queue[-1]  # rear операція
    print(f"Останній в черзі: {last_customer}")

# Обслуговуємо клієнтів (dequeue операція)
print("\n4. Обслуговуємо клієнтів:")

while queue:
    served_customer = queue.popleft()  # dequeue операція
    print(f"Обслужили: {served_customer}")
    print(f"Черга зараз: {list(queue)}")
    print(f"Розмір черги: {len(queue)}")
    print()

print("5. Черга тепер порожня")
print(f"Чи порожня черга? {len(queue) == 0}")

# Демонстрація FIFO принципу
print("\n=== ДЕМОНСТРАЦІЯ FIFO ===")

# Додаємо завдання від 1 до 5
task_queue = deque()
print("Додаємо завдання 1, 2, 3, 4, 5:")

for i in range(1, 6):
    task_queue.append(f"Завдання {i}")
    print(f"Додали {i}, черга: {list(task_queue)}")

print("\nВиконуємо всі завдання:")
completed_tasks = []

while task_queue:
    task = task_queue.popleft()
    completed_tasks.append(task)
    print(f"Виконали {task}, черга: {list(task_queue)}")

print(f"\nПорядок додавання: Завдання 1, 2, 3, 4, 5")
print(f"Порядок виконання: {', '.join(completed_tasks)}")
print("Це і є принцип FIFO - First In, First Out!")

# Практичний приклад - черга на автобус
print("\n=== ПРАКТИЧНИЙ ПРИКЛАД: ЧЕРГА НА АВТОБУС ===")

bus_queue = deque()
passengers = ["Студент", "Пенсіонер", "Мама з дитиною", "Робітник", "Школяр"]

print("Люди стають в чергу на автобус:")
for passenger in passengers:
    bus_queue.append(passenger)
    print(f"В чергу став: {passenger}")
    print(f"Черга: {list(bus_queue)}")
    print()

print("Автобус приїхав! Посадка пасажирів:")
bus_capacity = 3  # Автобус може взяти 3 пасажирів

boarded = []
for i in range(min(bus_capacity, len(bus_queue))):
    passenger = bus_queue.popleft()
    boarded.append(passenger)
    print(f"Сів в автобус: {passenger}")
    print(f"Залишилось в черзі: {list(bus_queue)}")
    print()

print(f"В автобус сіли: {', '.join(boarded)}")
print(f"Залишились чекати: {list(bus_queue)}")

# Функції для роботи з чергою
print("\n=== ФУНКЦІЇ ДЛЯ РОБОТИ З ЧЕРГОЮ ===")

def create_queue():
    """Створює порожню чергу"""
    return deque()

def enqueue(queue, item):
    """Додає елемент до черги"""
    queue.append(item)
    return f"Додано: {item}"

def dequeue(queue):
    """Забирає елемент з черги"""
    if is_empty(queue):
        return "Помилка: черга порожня!"
    return queue.popleft()

def front(queue):
    """Дивиться на перший елемент"""
    if is_empty(queue):
        return "Черга порожня"
    return queue[0]

def rear(queue):
    """Дивиться на останній елемент"""
    if is_empty(queue):
        return "Черга порожня"
    return queue[-1]

def is_empty(queue):
    """Перевіряє, чи черга порожня"""
    return len(queue) == 0

def size(queue):
    """Повертає розмір черги"""
    return len(queue)

# Тестуємо функції
my_queue = create_queue()
print(f"Створили чергу: {list(my_queue)}")

print(enqueue(my_queue, "Перший"))
print(enqueue(my_queue, "Другий"))
print(enqueue(my_queue, "Третій"))

print(f"Черга: {list(my_queue)}")
print(f"Перший в черзі: {front(my_queue)}")
print(f"Останній в черзі: {rear(my_queue)}")
print(f"Розмір черги: {size(my_queue)}")

print(f"Забрали: {dequeue(my_queue)}")
print(f"Черга після dequeue: {list(my_queue)}")

print(f"Чи порожня черга? {is_empty(my_queue)}")

# Порівняння зі стеком
print("\n=== ПОРІВНЯННЯ ЧЕРГИ ТА СТЕКА ===")

print("СТЕК (LIFO - Last In, First Out):")
stack = []
stack.append("A")  # push
stack.append("B")  # push
stack.append("C")  # push
print(f"Стек: {stack}")
print(f"Забираємо: {stack.pop()}")  # pop - забираємо останній
print(f"Стек: {stack}")

print("\nЧЕРГА (FIFO - First In, First Out):")
queue = deque()
queue.append("A")  # enqueue
queue.append("B")  # enqueue
queue.append("C")  # enqueue
print(f"Черга: {list(queue)}")
print(f"Забираємо: {queue.popleft()}")  # dequeue - забираємо перший
print(f"Черга: {list(queue)}")

print("\nВисновок:")
print("• Стек: додаємо і забираємо з одного кінця (вершини)")
print("• Черга: додаємо в один кінець, забираємо з іншого")
print("• Стек: як стопка тарілок")
print("• Черга: як черга в магазині")