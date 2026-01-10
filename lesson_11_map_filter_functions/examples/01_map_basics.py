# Приклад 1: Основи функції map()

print("=== Основи map() ===")

# Список чисел для роботи
numbers = [1, 2, 3, 4, 5]
print(f"Початкові числа: {numbers}")

# Піднести кожне число до квадрата
squares = list(map(lambda x: x ** 2, numbers))
print(f"Квадрати: {squares}")

# Подвоїти кожне число
doubled = list(map(lambda x: x * 2, numbers))
print(f"Подвоєні: {doubled}")

# Додати 10 до кожного числа
plus_ten = list(map(lambda x: x + 10, numbers))
print(f"Плюс 10: {plus_ten}")

print("\n=== map() з рядками ===")

# Список імен
names = ["іван", "марія", "петро", "анна"]
print(f"Імена: {names}")

# Перетворити в верхній регістр
upper_names = list(map(lambda name: name.upper(), names))
print(f"Верхній регістр: {upper_names}")

# Перетворити в заголовний регістр
title_names = list(map(lambda name: name.title(), names))
print(f"Заголовний регістр: {title_names}")

# Додати привітання
greetings = list(map(lambda name: f"Привіт, {name}!", names))
print(f"Привітання: {greetings}")

print("\n=== map() з власною функцією ===")

def format_grade(grade):
    """Форматує оцінку з коментарем"""
    if grade >= 10:
        return f"{grade} - Відмінно!"
    elif grade >= 7:
        return f"{grade} - Добре!"
    else:
        return f"{grade} - Потрібно підтягнути"

grades = [12, 8, 6, 10, 9]
print(f"Оцінки: {grades}")

formatted_grades = list(map(format_grade, grades))
print("Форматовані оцінки:")
for grade in formatted_grades:
    print(f"  {grade}")

print("\n=== map() з кількома списками ===")

# map() може працювати з кількома списками одночасно
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]

# Додати відповідні елементи
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"Числа 1: {numbers1}")
print(f"Числа 2: {numbers2}")
print(f"Суми: {sums}")

# Помножити відповідні елементи
products = list(map(lambda x, y: x * y, numbers1, numbers2))
print(f"Добутки: {products}")