# Приклад 4: Робота зі списками через цикли та list comprehensions

print("=== СТВОРЕННЯ СПИСКІВ ЧЕРЕЗ ЦИКЛИ ===")

# Традиційний спосіб - через цикл for
squares = []
print("Створюємо список квадратів від 1 до 10:")
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
    print(f"{i}² = {square}")

print(f"Квадрати: {squares}")

# List comprehension - коротший запис
squares_short = [i ** 2 for i in range(1, 11)]
print(f"Квадрати (list comprehension): {squares_short}")

print(f"\n=== ФІЛЬТРАЦІЯ СПИСКІВ ===")

# Фільтрація через звичайний цикл
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_numbers = []

print(f"Всі числа: {all_numbers}")
print("Знаходимо парні числа:")

for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        print(f"{num} - парне")

print(f"Парні числа: {even_numbers}")

# Фільтрація через list comprehension
even_short = [num for num in all_numbers if num % 2 == 0]
print(f"Парні числа (list comprehension): {even_short}")

print(f"\n=== ОБРОБКА СПИСКУ ОЦІНОК ===")

# Список оцінок студентів
grades = [12, 8, 10, 6, 9, 11, 7, 10, 5, 9, 8, 12]
print(f"Всі оцінки: {grades}")

# Знаходимо високі оцінки (9 і вище)
high_grades = []
for grade in grades:
    if grade >= 9:
        high_grades.append(grade)

print(f"Високі оцінки: {high_grades}")
print(f"Кількість високих оцінок: {len(high_grades)}")

# Перетворюємо оцінки в літерні
letter_grades = []
for grade in grades:
    if grade >= 10:
        letter_grades.append("A")
    elif grade >= 8:
        letter_grades.append("B")
    elif grade >= 6:
        letter_grades.append("C")
    else:
        letter_grades.append("F")

print(f"Літерні оцінки: {letter_grades}")

# Підраховуємо кількість кожної літерної оцінки
print(f"Розподіл оцінок:")
print(f"A: {letter_grades.count('A')}")
print(f"B: {letter_grades.count('B')}")
print(f"C: {letter_grades.count('C')}")
print(f"F: {letter_grades.count('F')}")

print(f"\n=== РОБОТА З ТЕКСТОМ ===")

# Список слів
words = ["python", "програмування", "список", "цикл", "функція"]
print(f"Слова: {words}")

# Знаходимо довгі слова (більше 5 символів)
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)

print(f"Довгі слова: {long_words}")

# Перетворюємо в великі літери
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())

print(f"Великі літери: {uppercase_words}")

# Знаходимо довжини слів
word_lengths = []
for word in words:
    word_lengths.append(len(word))

print(f"Довжини слів: {word_lengths}")

# Статистика слів
print(f"\nСтатистика слів:")
print(f"Всього слів: {len(words)}")
print(f"Найкоротше слово: {min(word_lengths)} символів")
print(f"Найдовше слово: {max(word_lengths)} символів")
print(f"Середня довжина: {sum(word_lengths) / len(word_lengths):.1f} символів")

print(f"\n=== МАТЕМАТИЧНІ ОПЕРАЦІЇ ===")

# Створюємо таблицю множення для числа 7
multiplication_table = []
number = 7

print(f"Таблиця множення для {number}:")
for i in range(1, 11):
    result = number * i
    multiplication_table.append(result)
    print(f"{number} × {i} = {result}")

print(f"Результати: {multiplication_table}")

# Знаходимо числа Фібоначчі
fibonacci = [0, 1]
print(f"\nПослідовність Фібоначчі:")
print(f"Початок: {fibonacci}")

for i in range(8):  # Додаємо ще 8 чисел
    next_fib = fibonacci[-1] + fibonacci[-2]  # Сума двох останніх
    fibonacci.append(next_fib)
    print(f"Додано: {next_fib}, послідовність: {fibonacci}")

print(f"Перші 10 чисел Фібоначчі: {fibonacci}")

# Аналіз послідовності
print(f"\nАналіз послідовності Фібоначчі:")
print(f"Сума всіх чисел: {sum(fibonacci)}")
print(f"Найбільше число: {max(fibonacci)}")
print(f"Парні числа: {[num for num in fibonacci if num % 2 == 0]}")

print(f"\n=== ENUMERATE ДЛЯ ІНДЕКСІВ ===")

# Використання enumerate для отримання індексів
subjects = ["математика", "фізика", "хімія", "біологія", "англійська"]
print("Розклад уроків:")

for i, subject in enumerate(subjects, 1):
    print(f"{i} урок: {subject}")

# Знаходимо позицію улюбленого предмету
favorite = "фізика"
for i, subject in enumerate(subjects):
    if subject == favorite:
        print(f"\nУлюблений предмет '{favorite}' - це {i + 1} урок")