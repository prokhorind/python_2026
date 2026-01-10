# Приклад 3: Функції sorted() та zip()

print("=== Основи sorted() ===")

# Сортування чисел
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Несортовані числа: {numbers}")

# Сортування за зростанням
sorted_asc = sorted(numbers)
print(f"За зростанням: {sorted_asc}")

# Сортування за спаданням
sorted_desc = sorted(numbers, reverse=True)
print(f"За спаданням: {sorted_desc}")

print("\n=== Сортування рядків ===")

# Список імен
names = ["Петро", "Анна", "Іван", "Марія", "Олег"]
print(f"Несортовані імена: {names}")

# Сортування за алфавітом
sorted_names = sorted(names)
print(f"За алфавітом: {sorted_names}")

# Сортування за довжиною
sorted_by_length = sorted(names, key=lambda name: len(name))
print(f"За довжиною: {sorted_by_length}")

# Сортування за останньою літерою
sorted_by_last = sorted(names, key=lambda name: name[-1])
print(f"За останньою літерою: {sorted_by_last}")

print("\n=== Сортування складних даних ===")

# Список студентів з оцінками
students = [
    ("Іван", 85),
    ("Марія", 92),
    ("Петро", 78),
    ("Анна", 96),
    ("Олег", 81)
]
print("Студенти та оцінки:")
for name, grade in students:
    print(f"  {name}: {grade}")

# Сортування за оцінкою
by_grade = sorted(students, key=lambda student: student[1])
print("\nЗа оцінкою (зростання):")
for name, grade in by_grade:
    print(f"  {name}: {grade}")

# Сортування за оцінкою (спадання)
by_grade_desc = sorted(students, key=lambda student: student[1], reverse=True)
print("\nЗа оцінкою (спадання):")
for name, grade in by_grade_desc:
    print(f"  {name}: {grade}")

print("\n=== Основи zip() ===")

# Об'єднання двох списків
names = ["Іван", "Марія", "Петро"]
ages = [16, 17, 15]
print(f"Імена: {names}")
print(f"Віки: {ages}")

# Об'єднання в пари
pairs = list(zip(names, ages))
print(f"Пари: {pairs}")

# Створення словника
student_dict = dict(zip(names, ages))
print(f"Словник: {student_dict}")

print("\n=== zip() з трьома списками ===")

names = ["Іван", "Марія", "Петро"]
ages = [16, 17, 15]
grades = [85, 92, 78]

print(f"Імена: {names}")
print(f"Віки: {ages}")
print(f"Оцінки: {grades}")

# Об'єднання трьох списків
combined = list(zip(names, ages, grades))
print(f"Об'єднано: {combined}")

print("\nІнформація про студентів:")
for name, age, grade in combined:
    print(f"  {name}, {age} років, оцінка: {grade}")

print("\n=== zip() з різною довжиною ===")

# zip() зупиняється на найкоротшому списку
short_list = [1, 2, 3]
long_list = [10, 20, 30, 40, 50]

print(f"Короткий список: {short_list}")
print(f"Довгий список: {long_list}")

zipped = list(zip(short_list, long_list))
print(f"Результат zip(): {zipped}")

print("\n=== Практичний приклад ===")

# Створення рейтингу студентів
names = ["Іван", "Марія", "Петро", "Анна", "Олег"]
grades = [85, 92, 78, 96, 81]

# Об'єднуємо та сортуємо за оцінкою
students = list(zip(names, grades))
ranking = sorted(students, key=lambda student: student[1], reverse=True)

print("Рейтинг студентів:")
for i, (name, grade) in enumerate(ranking, 1):
    print(f"  {i}. {name}: {grade} балів")