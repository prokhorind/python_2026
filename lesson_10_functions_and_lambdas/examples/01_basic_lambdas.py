# Приклад 1: Основи лямбда функцій

print("=== Прості лямбда функції ===")

# Квадрат числа
square = lambda x: x ** 2
print(f"Квадрат 5: {square(5)}")

# Додавання двох чисел
add = lambda x, y: x + y
print(f"3 + 7 = {add(3, 7)}")

# Перевірка парності
is_even = lambda n: n % 2 == 0
print(f"8 парне? {is_even(8)}")
print(f"7 парне? {is_even(7)}")

print("\n=== Порівняння з звичайними функціями ===")

# Звичайна функція
def multiply_normal(x, y):
    return x * y

# Лямбда функція
multiply_lambda = lambda x, y: x * y

print(f"Звичайна функція: 4 * 6 = {multiply_normal(4, 6)}")
print(f"Лямбда функція: 4 * 6 = {multiply_lambda(4, 6)}")

print("\n=== Лямбда з умовами ===")

# Максимум з двох чисел
max_of_two = lambda a, b: a if a > b else b
print(f"Максимум з 10 та 15: {max_of_two(10, 15)}")

# Абсолютне значення
abs_value = lambda x: x if x >= 0 else -x
print(f"Абсолютне значення -5: {abs_value(-5)}")
print(f"Абсолютне значення 3: {abs_value(3)}")