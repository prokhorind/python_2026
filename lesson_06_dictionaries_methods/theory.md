# Урок 6: Словники - методи та операції

## Мета уроку
Детально вивчити роботу зі словниками: методи додавання, видалення, пошуку та обробки пар ключ-значення.

## Теоретичний матеріал

### 1. Створення та базові операції зі словниками

```python
# Різні способи створення словників
empty_dict = {}
student = {"name": "Олексій", "age": 16, "grade": 10}
grades = dict(math=10, physics=9, chemistry=8)

# Створення з списку кортежів
subjects = [("математика", 10), ("фізика", 9), ("хімія", 8)]
grade_dict = dict(subjects)

# Доступ до значень
print(student["name"])        # "Олексій"
print(student.get("age"))     # 16
print(student.get("city", "Невідомо"))  # "Невідомо" (значення за замовчуванням)

# Зміна та додавання значень
student["age"] = 17           # Зміна існуючого ключа
student["city"] = "Київ"      # Додавання нового ключа
```

### 2. Основні методи словників

#### 2.1 Методи доступу до елементів

```python
student_info = {
    "name": "Марія",
    "age": 16,
    "subjects": ["математика", "фізика", "англійська"],
    "gpa": 9.5
}

# get() - безпечний доступ до значення
name = student_info.get("name")           # "Марія"
phone = student_info.get("phone", "Немає")  # "Немає"

# keys() - отримання всіх ключів
all_keys = student_info.keys()
print(f"Ключі: {list(all_keys)}")

# values() - отримання всіх значень
all_values = student_info.values()
print(f"Значення: {list(all_values)}")

# items() - отримання пар ключ-значення
all_items = student_info.items()
print(f"Пари: {list(all_items)}")

# Перевірка наявності ключа
if "name" in student_info:
    print(f"Ім'я студента: {student_info['name']}")

if "phone" not in student_info:
    print("Телефон не вказано")
```

#### 2.2 Методи додавання та оновлення

```python
# Початковий словник
contacts = {"Мама": "+380501234567", "Тато": "+380507654321"}

# update() - оновлення кількома парами
new_contacts = {"Друг": "+380631112233", "Школа": "+380442223344"}
contacts.update(new_contacts)
print(contacts)

# update() з іншими форматами
contacts.update([("Бабуся", "+380509998877")])  # Список кортежів
contacts.update(Дідусь="+380509998866")         # Іменовані аргументи

# setdefault() - встановлює значення, якщо ключа немає
contacts.setdefault("Лікар", "+380443334455")
contacts.setdefault("Мама", "інший номер")  # Не змінить існуючий

print(f"Контакти: {contacts}")
```

#### 2.3 Методи видалення

```python
student_data = {
    "name": "Іван",
    "age": 17,
    "city": "Львів",
    "hobby": "футбол",
    "grade": 11
}

# pop() - видаляє та повертає значення за ключем
age = student_data.pop("age")
print(f"Видалений вік: {age}")

# pop() з значенням за замовчуванням
phone = student_data.pop("phone", "Не вказано")
print(f"Телефон: {phone}")

# popitem() - видаляє та повертає останню пару (Python 3.7+)
last_item = student_data.popitem()
print(f"Остання пара: {last_item}")

# del - видаляє елемент за ключем
del student_data["hobby"]

# clear() - очищає весь словник
# student_data.clear()  # Розкоментуйте для очищення

print(f"Залишилось: {student_data}")
```

### 3. Ітерація по словниках

```python
grades = {"математика": 10, "фізика": 9, "хімія": 8, "біологія": 11}

# Ітерація по ключах (за замовчуванням)
print("Предмети:")
for subject in grades:
    print(f"- {subject}")

# Ітерація по ключах (явно)
print("\nПредмети (явно):")
for subject in grades.keys():
    print(f"- {subject}")

# Ітерація по значеннях
print("\nОцінки:")
for grade in grades.values():
    print(f"- {grade}")

# Ітерація по парах ключ-значення
print("\nПредмети та оцінки:")
for subject, grade in grades.items():
    print(f"{subject}: {grade}")

# Ітерація з enumerate
print("\nНумеровані предмети:")
for i, (subject, grade) in enumerate(grades.items(), 1):
    print(f"{i}. {subject} - {grade}")
```

### 4. Сортування словників

```python
student_grades = {
    "Анна": 95,
    "Борис": 87,
    "Віра": 92,
    "Григорій": 89,
    "Дарина": 96
}

# Сортування за ключами (іменами)
sorted_by_names = dict(sorted(student_grades.items()))
print(f"За іменами: {sorted_by_names}")

# Сортування за значеннями (оцінками)
sorted_by_grades = dict(sorted(student_grades.items(), key=lambda x: x[1]))
print(f"За оцінками (зростання): {sorted_by_grades}")

# Сортування за значеннями (спадання)
sorted_by_grades_desc = dict(sorted(student_grades.items(), key=lambda x: x[1], reverse=True))
print(f"За оцінками (спадання): {sorted_by_grades_desc}")

# Топ-3 студенти
top_3 = dict(list(sorted_by_grades_desc.items())[:3])
print(f"Топ-3 студенти: {top_3}")
```

### 5. Вкладені словники

```python
# Словник з інформацією про кілька студентів
students_db = {
    "student_001": {
        "name": "Олексій Петренко",
        "age": 16,
        "class": "10-А",
        "subjects": {
            "математика": 10,
            "фізика": 9,
            "англійська": 8
        },
        "contact": {
            "email": "alex@school.edu",
            "phone": "+380501234567"
        }
    },
    "student_002": {
        "name": "Марія Іваненко",
        "age": 17,
        "class": "10-Б",
        "subjects": {
            "математика": 11,
            "хімія": 10,
            "біологія": 9
        },
        "contact": {
            "email": "maria@school.edu",
            "phone": "+380507654321"
        }
    }
}

# Доступ до вкладених даних
student_id = "student_001"
student = students_db[student_id]

print(f"Ім'я: {student['name']}")
print(f"Клас: {student['class']}")
print(f"Email: {student['contact']['email']}")

# Оцінки студента
print(f"Оцінки {student['name']}:")
for subject, grade in student["subjects"].items():
    print(f"  {subject}: {grade}")

# Середня оцінка
grades_list = list(student["subjects"].values())
average = sum(grades_list) / len(grades_list)
print(f"Середня оцінка: {average:.1f}")
```

### 6. Словники та списки

```python
# Список словників
class_students = [
    {"name": "Анна", "age": 16, "grade": 95},
    {"name": "Борис", "age": 17, "grade": 87},
    {"name": "Віра", "age": 16, "grade": 92}
]

# Обробка списку словників
print("Студенти класу:")
for student in class_students:
    print(f"{student['name']} ({student['age']} років) - {student['grade']} балів")

# Фільтрація
excellent_students = []
for student in class_students:
    if student["grade"] >= 90:
        excellent_students.append(student["name"])

print(f"Відмінники: {excellent_students}")

# Словник зі списками
subjects_schedule = {
    "понеділок": ["математика", "фізика", "англійська"],
    "вівторок": ["хімія", "біологія", "історія"],
    "середа": ["математика", "література", "географія"],
    "четвер": ["фізика", "англійська", "мистецтво"],
    "п'ятниця": ["хімія", "фізкультура", "інформатика"]
}

# Пошук предмету в розкладі
search_subject = "математика"
found_days = []

for day, subjects in subjects_schedule.items():
    if search_subject in subjects:
        found_days.append(day)

print(f"Предмет '{search_subject}' є в такі дні: {found_days}")
```

### 7. Практичні застосування словників

#### 7.1 Підрахунок частоти

```python
def count_frequency(text):
    """Підраховує частоту символів у тексті"""
    frequency = {}
    
    for char in text.lower():
        if char.isalpha():  # Тільки літери
            frequency[char] = frequency.get(char, 0) + 1
    
    return frequency

# Тестування
text = "Програмування Python"
char_count = count_frequency(text)

print(f"Частота літер у '{text}':")
for char, count in sorted(char_count.items()):
    print(f"'{char}': {count}")

# Найчастіша літера
most_frequent = max(char_count.items(), key=lambda x: x[1])
print(f"Найчастіша літера: '{most_frequent[0]}' ({most_frequent[1]} разів)")
```

#### 7.2 Групування даних

```python
def group_students_by_grade(students):
    """Групує студентів за класами"""
    groups = {}
    
    for student in students:
        grade = student["grade"]
        if grade not in groups:
            groups[grade] = []
        groups[grade].append(student["name"])
    
    return groups

# Тестові дані
all_students = [
    {"name": "Анна", "grade": 10},
    {"name": "Борис", "grade": 11},
    {"name": "Віра", "grade": 10},
    {"name": "Григорій", "grade": 11},
    {"name": "Дарина", "grade": 9}
]

grouped = group_students_by_grade(all_students)

print("Студенти за класами:")
for grade, names in sorted(grouped.items()):
    print(f"{grade} клас: {', '.join(names)}")
```

#### 7.3 Кеш (збереження результатів)

```python
# Кеш для збереження результатів обчислень
fibonacci_cache = {}

def fibonacci_with_cache(n):
    """Обчислює числа Фібоначчі з кешуванням"""
    if n in fibonacci_cache:
        print(f"Беремо з кешу: fib({n}) = {fibonacci_cache[n]}")
        return fibonacci_cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)
    
    fibonacci_cache[n] = result
    print(f"Обчислили та зберегли: fib({n}) = {result}")
    return result

# Тестування
print("Обчислення fib(6) з кешуванням:")
result = fibonacci_with_cache(6)
print(f"\nРезультат: {result}")
print(f"Кеш: {fibonacci_cache}")
```

## Ключові поняття
- **get()** - безпечний доступ до значення з можливістю значення за замовчуванням
- **keys()**, **values()**, **items()** - отримання ключів, значень та пар
- **update()** - оновлення словника іншим словником або парами
- **pop()**, **popitem()** - видалення з поверненням значення
- **setdefault()** - встановлення значення, якщо ключа немає
- **Вкладені словники** - словники всередині словників
- **Частота** - підрахунок кількості входжень елементів

## Практичні поради
1. Використовуйте get() замість прямого доступу для безпеки
2. items() ідеально для ітерації по парах ключ-значення
3. setdefault() зручний для ініціалізації значень
4. Словники відмінно підходять для підрахунку та групування
5. Вкладені словники корисні для складних структур даних
6. Кешування з словниками прискорює повторні обчислення