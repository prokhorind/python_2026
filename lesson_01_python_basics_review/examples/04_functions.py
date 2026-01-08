# Приклад 4: Функції (складний)

def calculate_average(numbers):
    """Обчислює середнє арифметичне списку чисел"""
    if not numbers:  # Перевірка на порожній список
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    return round(total / count, 2)

def find_max_min(numbers):
    """Знаходить максимальне та мінімальне значення"""
    if not numbers:
        return None, None
    
    return max(numbers), min(numbers)

def analyze_grades(student_name, *grades):
    """Аналізує оцінки студента (використовує *args)"""
    if not grades:
        return f"{student_name}: Немає оцінок"
    
    avg = calculate_average(list(grades))
    max_grade, min_grade = find_max_min(list(grades))
    
    # Визначення рівня успішності
    if avg >= 9:
        level = "Відмінник"
    elif avg >= 7:
        level = "Хорошист"
    elif avg >= 4:
        level = "Середній учень"
    else:
        level = "Потребує допомоги"
    
    return {
        'name': student_name,
        'grades': list(grades),
        'average': avg,
        'max_grade': max_grade,
        'min_grade': min_grade,
        'level': level
    }

def create_report(**student_data):
    """Створює звіт про студента (використовує **kwargs)"""
    name = student_data.get('name', 'Невідомий')
    age = student_data.get('age', 'Невідомий')
    class_num = student_data.get('class', 'Невідомий')
    
    report = f"""
📊 ЗВІТ ПРО СТУДЕНТА
{'='*25}
👤 Ім'я: {name}
🎂 Вік: {age}
🏫 Клас: {class_num}
"""
    
    if 'grades' in student_data:
        analysis = analyze_grades(name, *student_data['grades'])
        report += f"""
📚 Академічна успішність:
   • Оцінки: {analysis['grades']}
   • Середній бал: {analysis['average']}
   • Найвища оцінка: {analysis['max_grade']}
   • Найнижча оцінка: {analysis['min_grade']}
   • Рівень: {analysis['level']}
"""
    
    return report

# Тестування функцій
print("Тестування функцій:")

# Тест 1: Аналіз оцінок
result1 = analyze_grades("Марія", 10, 9, 11, 8, 10)
print(f"Аналіз оцінок: {result1}")

print("\n" + "="*40 + "\n")

# Тест 2: Створення звіту
report = create_report(
    name="Олексій Петренко",
    age=16,
    class="10-А",
    grades=[9, 8, 10, 7, 9, 11]
)
print(report)