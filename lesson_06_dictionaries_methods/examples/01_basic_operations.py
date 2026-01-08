# Приклад 1: Основні операції зі словниками

print("=== ОСНОВНІ ОПЕРАЦІЇ ЗІ СЛОВНИКАМИ ===")

# Створення словника з інформацією про студента
student = {
    "name": "Олексій Петренко",
    "age": 16,
    "class": "10-А",
    "city": "Київ"
}

print("1. Початковий словник:")
print(f"Студент: {student}")
print(f"Кількість полів: {len(student)}")

# Доступ до значень
print("\n2. Доступ до значень:")
print(f"Ім'я: {student['name']}")
print(f"Вік: {student['age']}")

# Безпечний доступ з get()
print("\n3. Безпечний доступ з get():")
print(f"Клас: {student.get('class')}")
print(f"Телефон: {student.get('phone', 'Не вказано')}")

# Перевірка наявності ключів
print("\n4. Перевірка наявності ключів:")
if "name" in student:
    print("✓ Ім'я вказано")

if "phone" not in student:
    print("✗ Телефон не вказано")

# Додавання нових полів
print("\n5. Додавання нових полів:")
student["email"] = "alex.petrenko@school.edu"
student["subjects"] = ["математика", "фізика", "англійська"]
student["gpa"] = 9.2

print(f"Після додавання: {student}")

# Зміна існуючих значень
print("\n6. Зміна існуючих значень:")
student["age"] = 17  # День народження!
student["gpa"] = 9.5  # Покращились оцінки

print(f"Після змін: {student}")
print(f"Новий вік: {student['age']}")
print(f"Новий GPA: {student['gpa']}")

# Отримання всіх ключів, значень та пар
print("\n7. Отримання ключів, значень та пар:")

print("Ключі:")
for key in student.keys():
    print(f"  - {key}")

print("\nЗначення:")
for value in student.values():
    print(f"  - {value}")

print("\nПари ключ-значення:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Копіювання словника
print("\n8. Копіювання словника:")
student_copy = student.copy()
student_backup = dict(student)

print("Оригінал та копії створені")
print(f"Копії однакові: {student == student_copy == student_backup}")

# Зміна копії не впливає на оригінал
student_copy["name"] = "Інше ім'я"
print(f"Після зміни копії:")
print(f"Оригінал: {student['name']}")
print(f"Копія: {student_copy['name']}")

# Об'єднання словників
print("\n9. Об'єднання словників:")
additional_info = {
    "hobby": "програмування",
    "favorite_color": "синій",
    "pet": "кіт"
}

# Метод 1: update()
student.update(additional_info)
print(f"Після update(): {len(student)} полів")

# Метод 2: оператор ** (Python 3.5+)
combined = {**student, **{"grade": "відмінник"}}
print(f"Об'єднаний словник має {len(combined)} полів")

# Статистика словника
print("\n10. Статистика словника:")
print(f"Всього полів: {len(student)}")

# Підрахунок типів значень
type_count = {}
for value in student.values():
    value_type = type(value).__name__
    type_count[value_type] = type_count.get(value_type, 0) + 1

print("Типи значень:")
for data_type, count in type_count.items():
    print(f"  {data_type}: {count}")

# Пошук за значенням
print("\n11. Пошук за значенням:")
search_value = "10-А"
found_keys = []

for key, value in student.items():
    if value == search_value:
        found_keys.append(key)

if found_keys:
    print(f"Значення '{search_value}' знайдено в ключах: {found_keys}")
else:
    print(f"Значення '{search_value}' не знайдено")

# Фільтрація словника
print("\n12. Фільтрація словника:")

# Тільки рядкові значення
string_fields = {}
for key, value in student.items():
    if isinstance(value, str):
        string_fields[key] = value

print(f"Рядкові поля: {string_fields}")

# Тільки числові значення
numeric_fields = {}
for key, value in student.items():
    if isinstance(value, (int, float)):
        numeric_fields[key] = value

print(f"Числові поля: {numeric_fields}")

print("\n=== ВИСНОВКИ ===")
print("Словники дозволяють:")
print("• Зберігати пари ключ-значення")
print("• Швидко знаходити значення за ключем")
print("• Динамічно додавати та змінювати поля")
print("• Ітерувати по ключах, значеннях або парах")
print("• Безпечно отримувати значення з get()")
print("• Легко об'єднувати та копіювати дані")