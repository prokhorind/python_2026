# Приклад 2: Основи функції filter()

print("=== Основи filter() ===")

# Список чисел для роботи
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Всі числа: {numbers}")

# Фільтрація парних чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Парні числа: {even_numbers}")

# Фільтрація непарних чисел
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(f"Непарні числа: {odd_numbers}")

# Фільтрація чисел більше 5
big_numbers = list(filter(lambda x: x > 5, numbers))
print(f"Числа > 5: {big_numbers}")

# Фільтрація чисел в діапазоні
range_numbers = list(filter(lambda x: 3 <= x <= 7, numbers))
print(f"Числа від 3 до 7: {range_numbers}")

print("\n=== filter() з рядками ===")

# Список слів
words = ["кіт", "собака", "миша", "слон", "жираф", "їжак"]
print(f"Всі слова: {words}")

# Фільтрація коротких слів (до 4 символів)
short_words = list(filter(lambda word: len(word) <= 4, words))
print(f"Короткі слова: {short_words}")

# Фільтрація довгих слів (більше 4 символів)
long_words = list(filter(lambda word: len(word) > 4, words))
print(f"Довгі слова: {long_words}")

# Фільтрація слів, що починаються на певну букву
words_with_s = list(filter(lambda word: word.startswith('с'), words))
print(f"Слова на 'с': {words_with_s}")

print("\n=== filter() з оцінками ===")

# Список оцінок студентів
grades = [12, 8, 6, 10, 9, 5, 11, 7, 4, 12]
print(f"Всі оцінки: {grades}")

# Відмінні оцінки (10-12)
excellent_grades = list(filter(lambda grade: grade >= 10, grades))
print(f"Відмінні оцінки: {excellent_grades}")

# Добрі оцінки (7-9)
good_grades = list(filter(lambda grade: 7 <= grade <= 9, grades))
print(f"Добрі оцінки: {good_grades}")

# Незадовільні оцінки (менше 7)
poor_grades = list(filter(lambda grade: grade < 7, grades))
print(f"Незадовільні оцінки: {poor_grades}")

print("\n=== filter() з власною функцією ===")

def is_teenager(age):
    """Перевіряє чи є особа підлітком (13-19 років)"""
    return 13 <= age <= 19

ages = [10, 15, 22, 17, 8, 19, 25, 14, 30, 16]
print(f"Всі віки: {ages}")

teenager_ages = list(filter(is_teenager, ages))
print(f"Віки підлітків: {teenager_ages}")

print("\n=== Комбінування filter() ===")

# Знайти парні числа більше 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"Всі числа: {numbers}")

# Спочатку фільтруємо числа > 5, потім парні
big_numbers = filter(lambda x: x > 5, numbers)
even_big_numbers = list(filter(lambda x: x % 2 == 0, big_numbers))
print(f"Парні числа > 5: {even_big_numbers}")

# Або в одну лінію
result = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(f"Те саме в одну лінію: {result}")