# Приклад 3: Вбудовані функції з лямбда

print("=== filter() - фільтрація елементів ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Фільтрація парних чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Всі числа: {numbers}")
print(f"Парні числа: {even_numbers}")

# Фільтрація чисел більше 5
big_numbers = list(filter(lambda x: x > 5, numbers))
print(f"Числа > 5: {big_numbers}")

# Фільтрація чисел, які діляться на 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(f"Діляться на 3: {divisible_by_3}")

print("\n=== map() - перетворення елементів ===")

# Квадрати чисел
squares = list(map(lambda x: x ** 2, numbers[:6]))
print(f"Числа: {numbers[:6]}")
print(f"Квадрати: {squares}")

# Перетворення температури з Цельсія в Фаренгейт
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(f"Цельсій: {celsius}")
print(f"Фаренгейт: {fahrenheit}")

print("\n=== sorted() - сортування з ключем ===")

# Сортування студентів за оцінками
students = [
    ("Іван", 85),
    ("Марія", 92),
    ("Петро", 78),
    ("Анна", 96),
    ("Олег", 81)
]

# Сортування за оцінкою (зростання)
by_grade_asc = sorted(students, key=lambda student: student[1])
print("Сортування за оцінкою (зростання):")
for name, grade in by_grade_asc:
    print(f"  {name}: {grade}")

# Сортування за оцінкою (спадання)
by_grade_desc = sorted(students, key=lambda student: student[1], reverse=True)
print("\nСортування за оцінкою (спадання):")
for name, grade in by_grade_desc:
    print(f"  {name}: {grade}")

# Сортування за ім'ям
by_name = sorted(students, key=lambda student: student[0])
print("\nСортування за ім'ям:")
for name, grade in by_name:
    print(f"  {name}: {grade}")

print("\n=== Комбінування функцій ===")

# Знайти квадрати парних чисел більше 3
result = list(map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0 and x > 3, numbers)
))
print(f"Квадрати парних чисел > 3: {result}")

print("\n=== Практичний приклад: обробка слів ===")

words = ["python", "програмування", "лямбда", "функція", "код"]

# Фільтрація слів довжиною більше 5 символів
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"Слова довжиною > 5: {long_words}")

# Перетворення в верхній регістр
upper_words = list(map(lambda word: word.upper(), words))
print(f"Верхній регістр: {upper_words}")

# Сортування за довжиною
by_length = sorted(words, key=lambda word: len(word))
print(f"Сортування за довжиною: {by_length}")