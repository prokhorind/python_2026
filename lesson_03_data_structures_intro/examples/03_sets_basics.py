# Приклад 3: Основи роботи з множинами

# Створення множин
favorite_subjects = {"математика", "фізика", "інформатика", "англійська"}
visited_countries = {"Україна", "Польща", "Німеччина"}
lucky_numbers = {7, 13, 21, 7, 13}  # Дублікати автоматично видаляються

print("=== РОБОТА З МНОЖИНАМИ ===")
print(f"Улюблені предмети: {favorite_subjects}")
print(f"Відвідані країни: {visited_countries}")
print(f"Щасливі числа: {lucky_numbers}")  # {7, 13, 21}

# Додавання елементів
favorite_subjects.add("хімія")
print(f"\nПісля додавання хімії: {favorite_subjects}")

# Спроба додати існуючий елемент (нічого не зміниться)
favorite_subjects.add("математика")
print(f"Після спроби додати математику знову: {favorite_subjects}")

# Видалення елементів
favorite_subjects.remove("англійська")
print(f"Після видалення англійської: {favorite_subjects}")

# Безпечне видалення (не викличе помилку, якщо елемента немає)
favorite_subjects.discard("французька")  # Елемента немає, але помилки не буде

# Перевірка наявності
if "математика" in favorite_subjects:
    print("\nМатематика є серед улюблених предметів!")

if "географія" not in favorite_subjects:
    print("Географії немає серед улюблених предметів")

# Кількість елементів
print(f"\nКількість улюблених предметів: {len(favorite_subjects)}")

# Операції з множинами
class_10a_subjects = {"математика", "фізика", "хімія", "біологія"}
class_10b_subjects = {"математика", "інформатика", "англійська", "хімія"}

print(f"\nПредмети 10-А: {class_10a_subjects}")
print(f"Предмети 10-Б: {class_10b_subjects}")

# Перетин (спільні предмети)
common_subjects = class_10a_subjects & class_10b_subjects
print(f"Спільні предмети: {common_subjects}")

# Об'єднання (всі предмети)
all_subjects = class_10a_subjects | class_10b_subjects
print(f"Всі предмети: {all_subjects}")

# Різниця (предмети тільки в 10-А)
only_10a = class_10a_subjects - class_10b_subjects
print(f"Тільки в 10-А: {only_10a}")

# Симетрична різниця (предмети, що є тільки в одному класі)
unique_subjects = class_10a_subjects ^ class_10b_subjects
print(f"Унікальні для кожного класу: {unique_subjects}")

# Перетворення списку в множину (видалення дублікатів)
grades_with_duplicates = [10, 8, 9, 10, 7, 8, 9, 10]
unique_grades = set(grades_with_duplicates)
print(f"\nОцінки з дублікатами: {grades_with_duplicates}")
print(f"Унікальні оцінки: {unique_grades}")
print(f"Кількість унікальних оцінок: {len(unique_grades)}")