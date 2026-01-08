# Приклад 1: Основи роботи зі стеком

print("=== СТЕК - ОСНОВИ ===")

# Створюємо стек за допомогою списку
stack = []

print("1. Створили порожній стек")
print(f"Стек: {stack}")
print(f"Чи порожній стек? {len(stack) == 0}")

# Додаємо елементи (push операція)
print("\n2. Додаємо елементи до стека:")

items_to_add = ["книга 1", "книга 2", "книга 3", "книга 4"]

for item in items_to_add:
    stack.append(item)  # push операція
    print(f"Додали: {item}")
    print(f"Стек зараз: {stack}")
    print(f"Розмір стека: {len(stack)}")
    print()

# Дивимось на верхній елемент (peek операція)
print("3. Дивимось на верхній елемент:")
if stack:
    top_item = stack[-1]  # peek операція
    print(f"Верхній елемент: {top_item}")
    print(f"Стек не змінився: {stack}")

# Забираємо елементи (pop операція)
print("\n4. Забираємо елементи зі стека:")

while stack:
    removed_item = stack.pop()  # pop операція
    print(f"Забрали: {removed_item}")
    print(f"Стек зараз: {stack}")
    print(f"Розмір стека: {len(stack)}")
    print()

print("5. Стек тепер порожній")
print(f"Чи порожній стек? {len(stack) == 0}")

# Демонстрація LIFO принципу
print("\n=== ДЕМОНСТРАЦІЯ LIFO ===")

# Додаємо числа від 1 до 5
numbers_stack = []
print("Додаємо числа 1, 2, 3, 4, 5:")

for i in range(1, 6):
    numbers_stack.append(i)
    print(f"Додали {i}, стек: {numbers_stack}")

print("\nЗабираємо всі числа:")
removed_numbers = []

while numbers_stack:
    num = numbers_stack.pop()
    removed_numbers.append(num)
    print(f"Забрали {num}, стек: {numbers_stack}")

print(f"\nПорядок додавання: 1, 2, 3, 4, 5")
print(f"Порядок забирання: {', '.join(map(str, removed_numbers))}")
print("Це і є принцип LIFO - Last In, First Out!")

# Практичний приклад - стопка тарілок
print("\n=== ПРАКТИЧНИЙ ПРИКЛАД: СТОПКА ТАРІЛОК ===")

plates_stack = []
plate_colors = ["біла", "синя", "червона", "зелена", "жовта"]

print("Складаємо тарілки в стопку:")
for color in plate_colors:
    plates_stack.append(f"{color} тарілка")
    print(f"Поклали {color} тарілку")
    print(f"Стопка: {plates_stack}")
    print()

print("Беремо тарілки зі стопки для сервірування:")
for i in range(3):  # Беремо 3 тарілки
    if plates_stack:
        plate = plates_stack.pop()
        print(f"Взяли: {plate}")
        print(f"Залишилось у стопці: {plates_stack}")
        print()

print(f"У стопці залишилось {len(plates_stack)} тарілок")

# Функції для роботи зі стеком
print("\n=== ФУНКЦІЇ ДЛЯ РОБОТИ ЗІ СТЕКОМ ===")

def create_stack():
    """Створює порожній стек"""
    return []

def push(stack, item):
    """Додає елемент до стека"""
    stack.append(item)
    return f"Додано: {item}"

def pop(stack):
    """Забирає елемент зі стека"""
    if is_empty(stack):
        return "Помилка: стек порожній!"
    return stack.pop()

def peek(stack):
    """Дивиться на верхній елемент"""
    if is_empty(stack):
        return "Стек порожній"
    return stack[-1]

def is_empty(stack):
    """Перевіряє, чи стек порожній"""
    return len(stack) == 0

def size(stack):
    """Повертає розмір стека"""
    return len(stack)

# Тестуємо функції
my_stack = create_stack()
print(f"Створили стек: {my_stack}")

print(push(my_stack, "елемент A"))
print(push(my_stack, "елемент B"))
print(push(my_stack, "елемент C"))

print(f"Стек: {my_stack}")
print(f"Верхній елемент: {peek(my_stack)}")
print(f"Розмір стека: {size(my_stack)}")

print(f"Забрали: {pop(my_stack)}")
print(f"Стек після pop: {my_stack}")

print(f"Чи порожній стек? {is_empty(my_stack)}")