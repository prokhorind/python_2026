# Приклад 2: Видалення елементів зі списку

print("=== ВИДАЛЕННЯ ЕЛЕМЕНТІВ ===")

# Список оцінок студента
grades = [10, 8, 9, 7, 10, 6, 9, 8, 10]
print(f"Початкові оцінки: {grades}")
print(f"Кількість оцінок: {len(grades)}")

# remove() - видаляє перше входження елемента
print(f"\n1. Використання remove():")
grades.remove(10)  # Видалить перший 10
print(f"Після remove(10): {grades}")

grades.remove(8)   # Видалить перший 8
print(f"Після remove(8): {grades}")

# Безпечне видалення з перевіркою
grade_to_remove = 12
if grade_to_remove in grades:
    grades.remove(grade_to_remove)
    print(f"Видалено оцінку {grade_to_remove}")
else:
    print(f"Оцінки {grade_to_remove} немає в списку")

# pop() - видаляє та повертає елемент за індексом
print(f"\n2. Використання pop():")
last_grade = grades.pop()  # Видаляє останній елемент
print(f"Видалена остання оцінка: {last_grade}")
print(f"Список після pop(): {grades}")

first_grade = grades.pop(0)  # Видаляє перший елемент
print(f"Видалена перша оцінка: {first_grade}")
print(f"Список після pop(0): {grades}")

middle_grade = grades.pop(2)  # Видаляє елемент з індексом 2
print(f"Видалена оцінка з позиції 2: {middle_grade}")
print(f"Список після pop(2): {grades}")

# del - видаляє елемент за індексом (не повертає значення)
print(f"\n3. Використання del:")
print(f"Перед del grades[1]: {grades}")
del grades[1]
print(f"Після del grades[1]: {grades}")

# Видалення кількох елементів через зріз
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nПочаткові числа: {numbers}")
del numbers[2:5]  # Видаляє елементи з індексу 2 до 5 (не включно)
print(f"Після del numbers[2:5]: {numbers}")

# Видалення елементів за умовою
print(f"\n4. Видалення за умовою:")
test_scores = [85, 92, 45, 78, 96, 32, 88, 91, 67]
print(f"Всі оцінки: {test_scores}")

# Видаляємо всі оцінки нижче 70 (йдемо з кінця, щоб не зміщувались індекси)
for i in range(len(test_scores) - 1, -1, -1):
    if test_scores[i] < 70:
        removed_score = test_scores.pop(i)
        print(f"Видалено низьку оцінку: {removed_score}")

print(f"Оцінки після видалення низьких: {test_scores}")

# Альтернативний спосіб - створення нового списку
all_scores = [85, 92, 45, 78, 96, 32, 88, 91, 67]
good_scores = []
for score in all_scores:
    if score >= 70:
        good_scores.append(score)

print(f"Хороші оцінки (новий список): {good_scores}")

# clear() - очищає весь список
temp_list = [1, 2, 3, 4, 5]
print(f"\nПеред clear(): {temp_list}")
temp_list.clear()
print(f"Після clear(): {temp_list}")

# Підрахунок видалених елементів
print(f"\n=== СТАТИСТИКА ===")
original_count = 9  # Початкова кількість оцінок
current_count = len(grades)
removed_count = original_count - current_count
print(f"Початкова кількість оцінок: {original_count}")
print(f"Поточна кількість оцінок: {current_count}")
print(f"Видалено оцінок: {removed_count}")

if grades:
    print(f"Середня оцінка: {sum(grades) / len(grades):.1f}")
else:
    print("Список оцінок порожній")