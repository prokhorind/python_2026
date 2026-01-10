# Приклад 2: Функції вищого порядку

print("=== Функції, які приймають інші функції ===")

def apply_to_list(numbers, operation):
    """Застосовує операцію до кожного елемента списку"""
    return [operation(num) for num in numbers]

numbers = [1, 2, 3, 4, 5]

# Різні операції з лямбда
squares = apply_to_list(numbers, lambda x: x ** 2)
cubes = apply_to_list(numbers, lambda x: x ** 3)
doubled = apply_to_list(numbers, lambda x: x * 2)

print(f"Числа: {numbers}")
print(f"Квадрати: {squares}")
print(f"Куби: {cubes}")
print(f"Подвоєні: {doubled}")

print("\n=== Функції з умовними лямбда ===")

def filter_and_transform(numbers, condition, transformation):
    """Фільтрує числа за умовою та перетворює їх"""
    filtered = [num for num in numbers if condition(num)]
    transformed = [transformation(num) for num in filtered]
    return filtered, transformed

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Парні числа та їх квадрати
even_nums, even_squares = filter_and_transform(
    numbers,
    lambda x: x % 2 == 0,  # умова: парні
    lambda x: x ** 2       # перетворення: квадрат
)

print(f"Парні числа: {even_nums}")
print(f"Їх квадрати: {even_squares}")

print("\n=== Функція, яка повертає функцію ===")

def create_multiplier(factor):
    """Створює функцію множення на заданий фактор"""
    return lambda x: x * factor

# Створюємо різні множники
double = create_multiplier(2)
triple = create_multiplier(3)
multiply_by_10 = create_multiplier(10)

number = 7
print(f"Число: {number}")
print(f"Подвоїти: {double(number)}")
print(f"Потроїти: {triple(number)}")
print(f"Помножити на 10: {multiply_by_10(number)}")

print("\n=== Практичний приклад: обробка оцінок ===")

def process_grades(grades, processor):
    """Обробляє оцінки за допомогою переданої функції"""
    return [processor(grade) for grade in grades]

grades = [85, 92, 78, 96, 88, 73, 91]

# Різні способи обробки оцінок
rounded_grades = process_grades(grades, lambda x: round(x / 10) * 10)
grade_categories = process_grades(grades, lambda x: 'Відмінно' if x >= 90 else 'Добре' if x >= 80 else 'Задовільно')
bonus_grades = process_grades(grades, lambda x: min(100, x + 5))

print(f"Оригінальні оцінки: {grades}")
print(f"Округлені до десятків: {rounded_grades}")
print(f"Категорії оцінок: {grade_categories}")
print(f"З бонусом +5: {bonus_grades}")