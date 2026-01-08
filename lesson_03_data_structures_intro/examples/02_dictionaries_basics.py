# Приклад 2: Основи роботи зі словниками

# Створення профілю студента
student_profile = {
    "name": "Анна Петренко",
    "age": 16,
    "class": "10-Б",
    "favorite_subjects": ["математика", "фізика", "англійська"],
    "gpa": 10.5,
    "has_laptop": True
}

print("=== ПРОФІЛЬ СТУДЕНТА ===")
print(f"Ім'я: {student_profile['name']}")
print(f"Вік: {student_profile['age']} років")
print(f"Клас: {student_profile['class']}")
print(f"Середній бал: {student_profile['gpa']}")

# Виведення улюблених предметів
print("\nУлюблені предмети:")
for i, subject in enumerate(student_profile['favorite_subjects'], 1):
    print(f"  {i}. {subject}")

# Додавання нової інформації
student_profile['city'] = 'Харків'
student_profile['hobbies'] = ['читання', 'плавання', 'програмування']

print(f"\nМісто: {student_profile['city']}")
print("Хобі:", ', '.join(student_profile['hobbies']))

# Оновлення існуючої інформації
student_profile['age'] += 1  # День народження!
student_profile['gpa'] = round(student_profile['gpa'] + 0.3, 1)

print(f"\nПісля дня народження:")
print(f"Новий вік: {student_profile['age']} років")
print(f"Новий середній бал: {student_profile['gpa']}")

# Перевірка наявності ключа
if 'phone' in student_profile:
    print(f"Телефон: {student_profile['phone']}")
else:
    print("Номер телефону не вказано")

# Отримання всіх ключів та значень
print(f"\nВся інформація про студента:")
for key, value in student_profile.items():
    if isinstance(value, list):
        print(f"{key}: {', '.join(value)}")
    else:
        print(f"{key}: {value}")

# Безпечне отримання значення
phone = student_profile.get('phone', 'Не вказано')
print(f"\nТелефон: {phone}")