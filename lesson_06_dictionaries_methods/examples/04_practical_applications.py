# Приклад 4: Практичні застосування словників

print("=== ПРАКТИЧНІ ЗАСТОСУВАННЯ СЛОВНИКІВ ===")

# 1. Підрахунок частоти елементів
print("1. ПІДРАХУНОК ЧАСТОТИ ЕЛЕМЕНТІВ")

def count_frequency(items):
    """Підраховує частоту елементів у списку"""
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Аналіз оцінок класу
class_grades = [10, 8, 9, 10, 7, 8, 9, 10, 6, 9, 8, 10, 11, 9, 8]
grade_frequency = count_frequency(class_grades)

print(f"Оцінки класу: {class_grades}")
print("Частота оцінок:")
for grade in sorted(grade_frequency.keys()):
    count = grade_frequency[grade]
    percentage = (count / len(class_grades)) * 100
    print(f"  {grade}: {count} разів ({percentage:.1f}%)")

# Найчастіша оцінка
most_common_grade = max(grade_frequency.items(), key=lambda x: x[1])
print(f"Найчастіша оцінка: {most_common_grade[0]} ({most_common_grade[1]} разів)")

# Аналіз тексту
print(f"\n2. АНАЛІЗ ТЕКСТУ")

def analyze_text(text):
    """Аналізує частоту літер у тексті"""
    # Очищаємо текст та приводимо до нижнього регістру
    clean_text = ''.join(char.lower() for char in text if char.isalpha())
    
    letter_count = count_frequency(clean_text)
    
    return {
        'total_letters': len(clean_text),
        'unique_letters': len(letter_count),
        'frequency': letter_count
    }

sample_text = "Програмування Python - це цікаво та корисно!"
analysis = analyze_text(sample_text)

print(f"Текст: '{sample_text}'")
print(f"Всього літер: {analysis['total_letters']}")
print(f"Унікальних літер: {analysis['unique_letters']}")

# Топ-5 найчастіших літер
top_letters = sorted(analysis['frequency'].items(), key=lambda x: x[1], reverse=True)[:5]
print("Топ-5 найчастіших літер:")
for letter, count in top_letters:
    print(f"  '{letter}': {count}")

# 3. Групування даних
print(f"\n3. ГРУПУВАННЯ ДАНИХ")

# Список студентів з їх класами
students_list = [
    {"name": "Анна", "class": "10-А", "age": 16},
    {"name": "Борис", "class": "10-Б", "age": 17},
    {"name": "Віра", "class": "10-А", "age": 16},
    {"name": "Григорій", "class": "11-А", "age": 17},
    {"name": "Дарина", "class": "10-Б", "age": 16},
    {"name": "Євген", "class": "11-А", "age": 18}
]

def group_by_field(items, field):
    """Групує елементи за певним полем"""
    groups = {}
    for item in items:
        key = item[field]
        groups.setdefault(key, []).append(item)
    return groups

# Групування за класами
by_class = group_by_field(students_list, "class")
print("Студенти за класами:")
for class_name, students in sorted(by_class.items()):
    names = [student["name"] for student in students]
    print(f"  {class_name}: {', '.join(names)} ({len(students)} студентів)")

# Групування за віком
by_age = group_by_field(students_list, "age")
print(f"\nСтуденти за віком:")
for age, students in sorted(by_age.items()):
    names = [student["name"] for student in students]
    print(f"  {age} років: {', '.join(names)}")

# 4. Кешування результатів
print(f"\n4. КЕШУВАННЯ РЕЗУЛЬТАТІВ")

# Кеш для збереження результатів обчислень
calculation_cache = {}
cache_hits = 0
cache_misses = 0

def expensive_calculation(n):
    """Імітація складного обчислення (факторіал)"""
    global cache_hits, cache_misses
    
    if n in calculation_cache:
        cache_hits += 1
        print(f"  Кеш HIT: {n}! = {calculation_cache[n]}")
        return calculation_cache[n]
    
    cache_misses += 1
    print(f"  Кеш MISS: обчислюємо {n}!")
    
    # Обчислюємо факторіал
    if n <= 1:
        result = 1
    else:
        result = n * expensive_calculation(n - 1)
    
    # Зберігаємо в кеші
    calculation_cache[n] = result
    return result

print("Обчислення факторіалів з кешуванням:")
test_numbers = [5, 3, 7, 5, 3, 6]

for num in test_numbers:
    result = expensive_calculation(num)
    print(f"    {num}! = {result}")

print(f"\nСтатистика кешу:")
print(f"  Попадань: {cache_hits}")
print(f"  Промахів: {cache_misses}")
print(f"  Ефективність: {cache_hits/(cache_hits+cache_misses)*100:.1f}%")
print(f"  Збережено в кеші: {len(calculation_cache)} значень")

# 5. Конфігурація програми
print(f"\n5. КОНФІГУРАЦІЯ ПРОГРАМИ")

# Словник конфігурації
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "school_db",
        "user": "admin"
    },
    "ui": {
        "theme": "dark",
        "language": "uk",
        "font_size": 14
    },
    "features": {
        "notifications": True,
        "auto_save": True,
        "debug_mode": False
    },
    "limits": {
        "max_students": 1000,
        "max_file_size": 10485760,  # 10MB
        "session_timeout": 3600     # 1 година
    }
}

def get_config_value(config, path, default=None):
    """Отримує значення конфігурації за шляхом"""
    keys = path.split('.')
    value = config
    
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return default
    
    return value

# Тестування конфігурації
config_tests = [
    "database.host",
    "ui.theme", 
    "features.notifications",
    "limits.max_students",
    "nonexistent.key"
]

print("Читання конфігурації:")
for path in config_tests:
    value = get_config_value(app_config, path, "НЕ ЗНАЙДЕНО")
    print(f"  {path}: {value}")

# 6. Індексування та пошук
print(f"\n6. ІНДЕКСУВАННЯ ТА ПОШУК")

# Створюємо індекс для швидкого пошуку
def create_index(items, index_field):
    """Створює індекс для швидкого пошуку"""
    index = {}
    for i, item in enumerate(items):
        key = item[index_field]
        index.setdefault(key, []).append(i)
    return index

# Індексуємо студентів за іменем та класом
name_index = create_index(students_list, "name")
class_index = create_index(students_list, "class")

print("Індекси створено:")
print(f"  За іменами: {len(name_index)} унікальних імен")
print(f"  За класами: {len(class_index)} унікальних класів")

# Швидкий пошук
def find_students(students, index, field, value):
    """Швидкий пошук студентів за індексом"""
    if value in index:
        indices = index[value]
        return [students[i] for i in indices]
    return []

# Пошук студентів
search_results = find_students(students_list, class_index, "class", "10-А")
print(f"\nСтуденти класу 10-А:")
for student in search_results:
    print(f"  {student['name']} ({student['age']} років)")

# 7. Статистика та звіти
print(f"\n7. СТАТИСТИКА ТА ЗВІТИ")

def generate_statistics(students):
    """Генерує статистику по студентах"""
    stats = {
        "total_students": len(students),
        "by_class": {},
        "by_age": {},
        "age_stats": {
            "min": float('inf'),
            "max": 0,
            "sum": 0
        }
    }
    
    for student in students:
        # Статистика по класах
        class_name = student["class"]
        stats["by_class"][class_name] = stats["by_class"].get(class_name, 0) + 1
        
        # Статистика по віку
        age = student["age"]
        stats["by_age"][age] = stats["by_age"].get(age, 0) + 1
        
        # Мін/макс вік
        stats["age_stats"]["min"] = min(stats["age_stats"]["min"], age)
        stats["age_stats"]["max"] = max(stats["age_stats"]["max"], age)
        stats["age_stats"]["sum"] += age
    
    # Середній вік
    stats["age_stats"]["average"] = stats["age_stats"]["sum"] / len(students)
    
    return stats

stats = generate_statistics(students_list)

print("Статистика студентів:")
print(f"  Всього: {stats['total_students']}")
print(f"  Середній вік: {stats['age_stats']['average']:.1f}")
print(f"  Вік від {stats['age_stats']['min']} до {stats['age_stats']['max']}")

print("  Розподіл по класах:")
for class_name, count in sorted(stats["by_class"].items()):
    percentage = (count / stats['total_students']) * 100
    print(f"    {class_name}: {count} ({percentage:.1f}%)")

print("\n=== ВИСНОВКИ ===")
print("Словники ідеально підходять для:")
print("• Підрахунку частоти та статистики")
print("• Групування та класифікації даних")
print("• Кешування результатів обчислень")
print("• Зберігання конфігурації програм")
print("• Створення індексів для швидкого пошуку")
print("• Генерації звітів та аналітики")
print("• Організації складних структур даних")