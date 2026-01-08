# Приклад 2: Розширені методи словників

print("=== РОЗШИРЕНІ МЕТОДИ СЛОВНИКІВ ===")

# Початковий словник контактів
contacts = {
    "Мама": "+380501234567",
    "Тато": "+380507654321",
    "Друг Олексій": "+380631112233"
}

print("1. Початкові контакти:")
for name, phone in contacts.items():
    print(f"  {name}: {phone}")

# Метод update() - різні способи
print("\n2. Метод update() - різні способи:")

# Спосіб 1: Словник
new_contacts_dict = {"Школа": "+380442223344", "Бабуся": "+380509998877"}
contacts.update(new_contacts_dict)
print("Після update(словник):")
print(f"  Додано: {list(new_contacts_dict.keys())}")

# Спосіб 2: Список кортежів
new_contacts_list = [("Дідусь", "+380509998866"), ("Лікар", "+380443334455")]
contacts.update(new_contacts_list)
print("Після update(список кортежів):")
print(f"  Додано: {[name for name, phone in new_contacts_list]}")

# Спосіб 3: Іменовані аргументи
contacts.update(Стоматолог="+380444445566", Ветеринар="+380445556677")
print("Після update(іменовані аргументи):")
print(f"  Всього контактів: {len(contacts)}")

# Метод setdefault()
print("\n3. Метод setdefault():")

# Додає ключ тільки якщо його немає
contacts.setdefault("Аптека", "+380446667788")
print("Додали 'Аптека' через setdefault()")

# Не змінює існуючий ключ
old_value = contacts.setdefault("Мама", "інший номер")
print(f"Спроба змінити 'Мама': залишилось {old_value}")

# Використання setdefault() для ініціалізації списків
student_subjects = {}
students = ["Анна", "Борис", "Віра", "Анна", "Борис"]
subjects = ["математика", "фізика", "хімія", "біологія", "англійська"]

for i, student in enumerate(students):
    # Ініціалізуємо список, якщо студента немає
    student_subjects.setdefault(student, [])
    # Додаємо предмет
    student_subjects[student].append(subjects[i % len(subjects)])

print(f"\nПредмети студентів: {student_subjects}")

# Методи pop() та popitem()
print("\n4. Методи pop() та popitem():")

# pop() - видаляє за ключем
removed_phone = contacts.pop("Стоматолог")
print(f"Видалили 'Стоматолог': {removed_phone}")

# pop() з значенням за замовчуванням
missing_contact = contacts.pop("Невідомий", "Контакт не знайдено")
print(f"Спроба видалити 'Невідомий': {missing_contact}")

# popitem() - видаляє останню пару (Python 3.7+)
last_contact = contacts.popitem()
print(f"Видалили останній контакт: {last_contact}")

# Відновлюємо видалений контакт
contacts[last_contact[0]] = last_contact[1]
print("Відновили останній контакт")

# Сортування словників
print("\n5. Сортування словників:")

grades = {"Анна": 95, "Борис": 87, "Віра": 92, "Григорій": 89, "Дарина": 96}
print(f"Оригінальні оцінки: {grades}")

# Сортування за ключами (іменами)
sorted_by_names = dict(sorted(grades.items()))
print(f"За іменами: {sorted_by_names}")

# Сортування за значеннями (оцінками) - зростання
sorted_by_grades_asc = dict(sorted(grades.items(), key=lambda x: x[1]))
print(f"За оцінками ↑: {sorted_by_grades_asc}")

# Сортування за значеннями (оцінками) - спадання
sorted_by_grades_desc = dict(sorted(grades.items(), key=lambda x: x[1], reverse=True))
print(f"За оцінками ↓: {sorted_by_grades_desc}")

# Топ-3 та останні 2
top_3 = dict(list(sorted_by_grades_desc.items())[:3])
bottom_2 = dict(list(sorted_by_grades_desc.items())[-2:])
print(f"Топ-3: {top_3}")
print(f"Останні 2: {bottom_2}")

# Фільтрація словників
print("\n6. Фільтрація словників:")

# Студенти з оцінкою >= 90
excellent_students = {name: grade for name, grade in grades.items() if grade >= 90}
print(f"Відмінники (≥90): {excellent_students}")

# Студенти з іменами на певну літеру
students_with_a = {name: grade for name, grade in grades.items() if name.startswith('А')}
print(f"Імена на 'А': {students_with_a}")

# Об'єднання та перетин словників
print("\n7. Об'єднання та перетин словників:")

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

# Об'єднання (dict2 перезаписує dict1)
merged = {**dict1, **dict2}
print(f"Об'єднання: {merged}")

# Перетин ключів
common_keys = set(dict1.keys()) & set(dict2.keys())
intersection = {key: dict1[key] for key in common_keys}
print(f"Спільні ключі: {common_keys}")
print(f"Перетин: {intersection}")

# Різниця ключів
only_in_dict1 = set(dict1.keys()) - set(dict2.keys())
only_in_dict2 = set(dict2.keys()) - set(dict1.keys())
print(f"Тільки в dict1: {only_in_dict1}")
print(f"Тільки в dict2: {only_in_dict2}")

# Інвертування словника (ключі ↔ значення)
print("\n8. Інвертування словника:")

original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(f"Оригінал: {original}")
print(f"Інвертований: {inverted}")

# Обережно з дублікатами значень!
with_duplicates = {"a": 1, "b": 2, "c": 1}
inverted_duplicates = {value: key for key, value in with_duplicates.items()}
print(f"З дублікатами: {with_duplicates}")
print(f"Інвертований (втрачено 'a'): {inverted_duplicates}")

# Групування значень при інвертуванні
grouped_inverted = {}
for key, value in with_duplicates.items():
    grouped_inverted.setdefault(value, []).append(key)
print(f"Групове інвертування: {grouped_inverted}")

# Статистика методів
print("\n9. Статистика використання методів:")
method_usage = {
    "get()": "Безпечний доступ до значень",
    "update()": "Оновлення кількома парами",
    "setdefault()": "Ініціалізація значень",
    "pop()": "Видалення з поверненням",
    "popitem()": "Видалення останньої пари",
    "keys()": "Отримання ключів",
    "values()": "Отримання значень", 
    "items()": "Отримання пар"
}

print("Корисні методи словників:")
for method, description in method_usage.items():
    print(f"  {method:12} - {description}")

print("\n=== ВИСНОВКИ ===")
print("Розширені методи словників дозволяють:")
print("• Безпечно працювати з відсутніми ключами")
print("• Ефективно оновлювати та об'єднувати словники")
print("• Сортувати за ключами або значеннями")
print("• Фільтрувати дані за умовами")
print("• Інвертувати та трансформувати структури")
print("• Групувати та аналізувати дані")