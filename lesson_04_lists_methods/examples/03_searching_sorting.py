# Приклад 3: Пошук та сортування списків

print("=== ПОШУК ЕЛЕМЕНТІВ ===")

# Список учнів класу
students = ["Анна", "Борис", "Віра", "Григорій", "Дарина", "Євген", "Жанна"]
print(f"Учні класу: {students}")

# Перевірка наявності елемента
search_name = "Віра"
if search_name in students:
    print(f"✓ {search_name} є в класі")
else:
    print(f"✗ {search_name} немає в класі")

# Пошук індексу елемента
if "Борис" in students:
    boris_index = students.index("Борис")
    print(f"Борис сидить на {boris_index + 1} місці (індекс {boris_index})")

# Безпечний пошук
def safe_find(lst, item):
    """Безпечно знаходить індекс елемента"""
    if item in lst:
        return lst.index(item)
    else:
        return -1

position = safe_find(students, "Олексій")
if position != -1:
    print(f"Олексій знайдений на позиції {position}")
else:
    print("Олексія немає в списку")

# Підрахунок входжень
grades = [10, 8, 9, 10, 7, 10, 9, 8, 10, 6]
print(f"\nОцінки: {grades}")
print(f"Кількість десяток: {grades.count(10)}")
print(f"Кількість дев'яток: {grades.count(9)}")
print(f"Кількість восьмірок: {grades.count(8)}")

# Статистика оцінок
unique_grades = []
for grade in grades:
    if grade not in unique_grades:
        unique_grades.append(grade)

print(f"Унікальні оцінки: {sorted(unique_grades)}")

print(f"\n=== СОРТУВАННЯ ===")

# Сортування чисел
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Початкові числа: {numbers}")

# sort() - сортує на місці (змінює оригінальний список)
numbers.sort()
print(f"Після sort(): {numbers}")

numbers.sort(reverse=True)
print(f"Після sort(reverse=True): {numbers}")

# sorted() - повертає новий відсортований список
original = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_copy = sorted(original)
print(f"\nОригінал: {original}")
print(f"Відсортована копія: {sorted_copy}")
print(f"Оригінал не змінився: {original}")

# Сортування рядків
cities = ["Київ", "Львів", "Одеса", "Харків", "Дніпро"]
print(f"\nМіста: {cities}")

cities.sort()
print(f"За алфавітом: {cities}")

cities.sort(reverse=True)
print(f"У зворотному алфавітному порядку: {cities}")

# Сортування за довжиною рядка
cities.sort(key=len)
print(f"За довжиною назви: {cities}")

# reverse() - змінює порядок на протилежний
fruits = ["яблуко", "банан", "апельсин", "груша"]
print(f"\nФрукти: {fruits}")
fruits.reverse()
print(f"У зворотному порядку: {fruits}")

print(f"\n=== ПОШУК ЕКСТРЕМУМІВ ===")

test_scores = [85, 92, 78, 96, 88, 91, 73, 89]
print(f"Результати тестів: {test_scores}")

# Знаходження мінімуму та максимуму
min_score = min(test_scores)
max_score = max(test_scores)
print(f"Найнижчий результат: {min_score}")
print(f"Найвищий результат: {max_score}")

# Знаходження позицій екстремумів
min_index = test_scores.index(min_score)
max_index = test_scores.index(max_score)
print(f"Найнижчий результат на позиції: {min_index + 1}")
print(f"Найвищий результат на позиції: {max_index + 1}")

# Статистика
total = sum(test_scores)
average = total / len(test_scores)
print(f"\nСтатистика:")
print(f"Всього тестів: {len(test_scores)}")
print(f"Сума балів: {total}")
print(f"Середній бал: {round(average, 2)}")
print(f"Діапазон: {min_score} - {max_score}")

# Сортування з збереженням оригінальних позицій
print(f"\n=== РЕЙТИНГ УЧНІВ ===")
student_names = ["Анна", "Борис", "Віра", "Григорій", "Дарина", "Євген", "Жанна", "Ігор"]
student_scores = [85, 92, 78, 96, 88, 91, 73, 89]

# Створюємо пари (ім'я, оцінка)
student_pairs = []
for i in range(len(student_names)):
    student_pairs.append((student_names[i], student_scores[i]))

print("Рейтинг учнів:")
# Сортуємо за оцінкою (другий елемент кортежу)
student_pairs.sort(key=lambda x: x[1], reverse=True)

for i, (name, score) in enumerate(student_pairs, 1):
    print(f"{i}. {name}: {score} балів")