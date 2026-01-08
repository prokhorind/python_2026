# Урок 8: Вкладені структури

## Мета уроку
Вивчити концепцію вкладених структур даних та навчитися працювати зі складними комбінаціями списків, словників та інших структур.

## Теоретичний матеріал

### 1. Що таке вкладені структури?

Вкладені структури - це структури даних, які містять інші структури даних як свої елементи. Це дозволяє створювати складні ієрархічні дані.

```python
# Приклади вкладених структур:

# 1. Список списків (двовимірний масив)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Словник зі списками
student_grades = {
    "Анна": [12, 11, 10, 12],
    "Борис": [9, 10, 11, 10],
    "Віра": [12, 12, 11, 12]
}

# 3. Список словників
students = [
    {"name": "Анна", "age": 16, "class": "10-А"},
    {"name": "Борис", "age": 17, "class": "11-Б"},
    {"name": "Віра", "age": 16, "class": "10-В"}
]

# 4. Словник словників
school_data = {
    "10-А": {
        "teacher": "Петренко О.І.",
        "students": 25,
        "subjects": ["математика", "фізика", "хімія"]
    },
    "11-Б": {
        "teacher": "Іваненко М.П.",
        "students": 23,
        "subjects": ["алгебра", "геометрія", "інформатика"]
    }
}
```

### 2. Список списків (Двовимірні масиви)

```python
# Створення та робота з матрицями
print("=== СПИСОК СПИСКІВ ===")

# Створення матриці 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Матриця:")
for row in matrix:
    print(row)

# Доступ до елементів
print(f"\nЕлемент [0][0]: {matrix[0][0]}")  # Перший рядок, перший стовпець
print(f"Елемент [1][2]: {matrix[1][2]}")  # Другий рядок, третій стовпець
print(f"Елемент [2][1]: {matrix[2][1]}")  # Третій рядок, другий стовпець

# Зміна елементів
matrix[1][1] = 99
print(f"\nПісля зміни [1][1] на 99:")
for row in matrix:
    print(row)

# Додавання нового рядка
matrix.append([10, 11, 12])
print(f"\nПісля додавання рядка:")
for i, row in enumerate(matrix):
    print(f"Рядок {i}: {row}")

# Створення матриці за допомогою циклів
rows, cols = 3, 4
empty_matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)  # Заповнюємо нулями
    empty_matrix.append(row)

print(f"\nПорожня матриця {rows}x{cols}:")
for row in empty_matrix:
    print(row)

# Більш компактний спосіб створення
zeros_matrix = [[0 for j in range(cols)] for i in range(rows)]
print(f"\nМатриця нулів (компактно):")
for row in zeros_matrix:
    print(row)
```

### 3. Словник зі списками

```python
print("\n=== СЛОВНИК ЗІ СПИСКАМИ ===")

# База даних оцінок учнів
grades_db = {
    "Анна Петренко": [12, 11, 10, 12, 11],
    "Борис Іваненко": [9, 10, 11, 10, 9],
    "Віра Сидоренко": [12, 12, 11, 12, 12],
    "Григорій Коваленко": [8, 9, 10, 9, 8],
    "Дарина Мельник": [11, 10, 12, 11, 10]
}

print("База даних оцінок:")
for student, grades in grades_db.items():
    average = sum(grades) / len(grades)
    print(f"{student}: {grades} (середній бал: {average:.1f})")

# Додавання нової оцінки
def add_grade(student_name, grade):
    """Додає оцінку учню"""
    if student_name in grades_db:
        grades_db[student_name].append(grade)
        print(f"Додано оцінку {grade} для {student_name}")
    else:
        print(f"Учень {student_name} не знайдений")

# Обчислення статистики
def get_student_stats(student_name):
    """Повертає статистику учня"""
    if student_name not in grades_db:
        return None
    
    grades = grades_db[student_name]
    return {
        "total_grades": len(grades),
        "average": sum(grades) / len(grades),
        "max_grade": max(grades),
        "min_grade": min(grades),
        "grades": grades
    }

# Тестування функцій
print("\n--- Додавання оцінок ---")
add_grade("Анна Петренко", 12)
add_grade("Новий учень", 10)  # Помилка

print("\n--- Статистика учня ---")
stats = get_student_stats("Віра Сидоренко")
if stats:
    print(f"Статистика для Віри Сидоренко:")
    print(f"  Кількість оцінок: {stats['total_grades']}")
    print(f"  Середній бал: {stats['average']:.2f}")
    print(f"  Найвища оцінка: {stats['max_grade']}")
    print(f"  Найнижча оцінка: {stats['min_grade']}")
```

### 4. Список словників

```python
print("\n=== СПИСОК СЛОВНИКІВ ===")

# База даних учнів
students_db = [
    {
        "id": 1,
        "name": "Анна Петренко",
        "age": 16,
        "class": "10-А",
        "subjects": ["математика", "фізика", "хімія"],
        "average_grade": 11.2
    },
    {
        "id": 2,
        "name": "Борис Іваненко",
        "age": 17,
        "class": "11-Б",
        "subjects": ["алгебра", "геометрія", "інформатика"],
        "average_grade": 9.8
    },
    {
        "id": 3,
        "name": "Віра Сидоренко",
        "age": 16,
        "class": "10-В",
        "subjects": ["біологія", "хімія", "географія"],
        "average_grade": 11.8
    },
    {
        "id": 4,
        "name": "Григорій Коваленко",
        "age": 17,
        "class": "11-А",
        "subjects": ["історія", "література", "англійська"],
        "average_grade": 8.9
    }
]

print("База даних учнів:")
for student in students_db:
    print(f"ID: {student['id']}")
    print(f"  Ім'я: {student['name']}")
    print(f"  Вік: {student['age']}")
    print(f"  Клас: {student['class']}")
    print(f"  Предмети: {', '.join(student['subjects'])}")
    print(f"  Середній бал: {student['average_grade']}")
    print()

# Пошук учнів за критеріями
def find_students_by_class(class_name):
    """Знаходить всіх учнів певного класу"""
    result = []
    for student in students_db:
        if student['class'] == class_name:
            result.append(student)
    return result

def find_top_students(min_grade=10.0):
    """Знаходить учнів з високим середнім балом"""
    result = []
    for student in students_db:
        if student['average_grade'] >= min_grade:
            result.append(student)
    return result

# Тестування пошуку
print("--- Пошук учнів ---")
class_10a = find_students_by_class("10-А")
print(f"Учні класу 10-А:")
for student in class_10a:
    print(f"  {student['name']} (бал: {student['average_grade']})")

print()
top_students = find_top_students(11.0)
print(f"Учні з середнім балом >= 11.0:")
for student in top_students:
    print(f"  {student['name']} - {student['average_grade']}")

# Додавання нового учня
def add_student(name, age, class_name, subjects, average_grade):
    """Додає нового учня до бази"""
    new_id = max(student['id'] for student in students_db) + 1
    
    new_student = {
        "id": new_id,
        "name": name,
        "age": age,
        "class": class_name,
        "subjects": subjects,
        "average_grade": average_grade
    }
    
    students_db.append(new_student)
    print(f"Додано нового учня: {name} (ID: {new_id})")

add_student("Дарина Мельник", 16, "10-Б", ["математика", "інформатика"], 10.5)
```

### 5. Словник словників

```python
print("\n=== СЛОВНИК СЛОВНИКІВ ===")

# Структура школи
school_structure = {
    "10-А": {
        "teacher": "Петренко Олена Іванівна",
        "students_count": 25,
        "subjects": ["математика", "фізика", "хімія", "біологія"],
        "classroom": "201",
        "schedule": {
            "понеділок": ["математика", "фізика", "українська", "англійська"],
            "вівторок": ["хімія", "біологія", "історія", "фізкультура"],
            "середа": ["математика", "географія", "література", "мистецтво"]
        }
    },
    "11-Б": {
        "teacher": "Іваненко Микола Петрович",
        "students_count": 23,
        "subjects": ["алгебра", "геометрія", "інформатика", "фізика"],
        "classroom": "305",
        "schedule": {
            "понеділок": ["алгебра", "геометрія", "інформатика", "англійська"],
            "вівторок": ["фізика", "хімія", "українська", "фізкультура"],
            "середа": ["алгебра", "історія", "література", "біологія"]
        }
    },
    "9-В": {
        "teacher": "Сидоренко Віра Олександрівна",
        "students_count": 28,
        "subjects": ["алгебра", "геометрія", "біологія", "географія"],
        "classroom": "102",
        "schedule": {
            "понеділок": ["алгебра", "біологія", "українська", "англійська"],
            "вівторок": ["геометрія", "географія", "історія", "фізкультура"],
            "середа": ["алгебра", "хімія", "література", "мистецтво"]
        }
    }
}

print("Структура школи:")
for class_name, class_info in school_structure.items():
    print(f"\nКлас {class_name}:")
    print(f"  Класний керівник: {class_info['teacher']}")
    print(f"  Кількість учнів: {class_info['students_count']}")
    print(f"  Кабінет: {class_info['classroom']}")
    print(f"  Предмети: {', '.join(class_info['subjects'])}")
    
    print("  Розклад:")
    for day, lessons in class_info['schedule'].items():
        print(f"    {day.capitalize()}: {', '.join(lessons)}")

# Функції для роботи зі структурою
def get_class_info(class_name):
    """Отримує інформацію про клас"""
    if class_name in school_structure:
        return school_structure[class_name]
    return None

def find_teacher_classes(teacher_name):
    """Знаходить класи певного вчителя"""
    result = []
    for class_name, class_info in school_structure.items():
        if teacher_name.lower() in class_info['teacher'].lower():
            result.append(class_name)
    return result

def get_monday_schedule():
    """Отримує розклад на понеділок для всіх класів"""
    monday_schedule = {}
    for class_name, class_info in school_structure.items():
        if "понеділок" in class_info['schedule']:
            monday_schedule[class_name] = class_info['schedule']['понеділок']
    return monday_schedule

# Тестування функцій
print("\n--- Робота з функціями ---")

# Інформація про клас
class_info = get_class_info("11-Б")
if class_info:
    print(f"Інформація про 11-Б:")
    print(f"  Вчитель: {class_info['teacher']}")
    print(f"  Учнів: {class_info['students_count']}")

# Пошук класів вчителя
teacher_classes = find_teacher_classes("Петренко")
print(f"\nКласи вчителя Петренко: {teacher_classes}")

# Розклад на понеділок
monday = get_monday_schedule()
print(f"\nРозклад на понеділок:")
for class_name, lessons in monday.items():
    print(f"  {class_name}: {', '.join(lessons)}")
```

### 6. Складні вкладені структури

```python
print("\n=== СКЛАДНІ ВКЛАДЕНІ СТРУКТУРИ ===")

# Комплексна база даних школи
school_database = {
    "school_info": {
        "name": "Ліцей №15",
        "address": "вул. Шевченка, 25",
        "phone": "+380441234567",
        "director": "Коваленко Петро Іванович"
    },
    
    "classes": {
        "10-А": {
            "teacher": "Петренко О.І.",
            "students": [
                {"name": "Анна Петренко", "grades": [12, 11, 10], "phone": "0501234567"},
                {"name": "Борис Іваненко", "grades": [9, 10, 11], "phone": "0507654321"},
                {"name": "Віра Сидоренко", "grades": [12, 12, 11], "phone": "0509876543"}
            ],
            "subjects": {
                "математика": {"hours_per_week": 4, "teacher": "Петренко О.І."},
                "фізика": {"hours_per_week": 3, "teacher": "Іваненко М.П."},
                "хімія": {"hours_per_week": 2, "teacher": "Сидоренко В.О."}
            }
        },
        
        "11-Б": {
            "teacher": "Іваненко М.П.",
            "students": [
                {"name": "Григорій Коваленко", "grades": [8, 9, 10], "phone": "0502345678"},
                {"name": "Дарина Мельник", "grades": [11, 10, 12], "phone": "0508765432"}
            ],
            "subjects": {
                "алгебра": {"hours_per_week": 3, "teacher": "Петренко О.І."},
                "геометрія": {"hours_per_week": 2, "teacher": "Петренко О.І."},
                "інформатика": {"hours_per_week": 2, "teacher": "Іваненко М.П."}
            }
        }
    },
    
    "teachers": {
        "Петренко О.І.": {
            "full_name": "Петренко Олена Іванівна",
            "subjects": ["математика", "алгебра", "геометрія"],
            "experience": 15,
            "phone": "0501111111"
        },
        "Іваненко М.П.": {
            "full_name": "Іваненко Микола Петрович",
            "subjects": ["фізика", "інформатика"],
            "experience": 12,
            "phone": "0502222222"
        },
        "Сидоренко В.О.": {
            "full_name": "Сидоренко Віра Олександрівна",
            "subjects": ["хімія", "біологія"],
            "experience": 8,
            "phone": "0503333333"
        }
    }
}

# Функції для роботи з комплексною базою
def get_all_students():
    """Отримує список всіх учнів школи"""
    all_students = []
    
    for class_name, class_data in school_database["classes"].items():
        for student in class_data["students"]:
            student_info = student.copy()  # Копіюємо дані учня
            student_info["class"] = class_name  # Додаємо інформацію про клас
            all_students.append(student_info)
    
    return all_students

def get_teacher_workload():
    """Обчислює навантаження кожного вчителя"""
    workload = {}
    
    for class_name, class_data in school_database["classes"].items():
        for subject, subject_info in class_data["subjects"].items():
            teacher = subject_info["teacher"]
            hours = subject_info["hours_per_week"]
            
            if teacher not in workload:
                workload[teacher] = 0
            workload[teacher] += hours
    
    return workload

def find_student_by_name(student_name):
    """Знаходить учня за ім'ям"""
    for class_name, class_data in school_database["classes"].items():
        for student in class_data["students"]:
            if student["name"] == student_name:
                result = student.copy()
                result["class"] = class_name
                result["class_teacher"] = class_data["teacher"]
                return result
    return None

def get_class_average_grade(class_name):
    """Обчислює середній бал класу"""
    if class_name not in school_database["classes"]:
        return None
    
    all_grades = []
    students = school_database["classes"][class_name]["students"]
    
    for student in students:
        all_grades.extend(student["grades"])
    
    if all_grades:
        return sum(all_grades) / len(all_grades)
    return 0

# Демонстрація роботи з комплексною структурою
print("Демонстрація роботи з комплексною базою даних:")

# Всі учні
print("\n1. Всі учні школи:")
all_students = get_all_students()
for student in all_students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"  {student['name']} ({student['class']}) - середній бал: {avg_grade:.1f}")

# Навантаження вчителів
print("\n2. Навантаження вчителів:")
workload = get_teacher_workload()
for teacher, hours in workload.items():
    teacher_info = school_database["teachers"][teacher]
    print(f"  {teacher_info['full_name']}: {hours} годин на тиждень")

# Пошук учня
print("\n3. Пошук учня:")
student = find_student_by_name("Віра Сидоренко")
if student:
    print(f"  Знайдено: {student['name']}")
    print(f"  Клас: {student['class']}")
    print(f"  Класний керівник: {student['class_teacher']}")
    print(f"  Оцінки: {student['grades']}")
    print(f"  Телефон: {student['phone']}")

# Середні бали класів
print("\n4. Середні бали класів:")
for class_name in school_database["classes"]:
    avg_grade = get_class_average_grade(class_name)
    print(f"  {class_name}: {avg_grade:.2f}")
```

## Ключові поняття
- **Вкладені структури** - структури даних, що містять інші структури
- **Двовимірний масив** - список списків для представлення таблиць/матриць
- **Індексація** - доступ до елементів через кілька індексів [i][j]
- **Ієрархічні дані** - дані з деревоподібною структурою
- **Композиція структур** - поєднання різних типів структур даних

## Практичні поради
1. Використовуйте зрозумілі назви ключів у словниках
2. Перевіряйте існування ключів перед доступом до них
3. Створюйте функції для роботи зі складними структурами
4. Документуйте структуру ваших даних
5. Використовуйте циклі для обходу вкладених структур
6. Будьте обережні з глибоким копіюванням вкладених структур
7. Розбивайте складні структури на менші функції для кращої читабельності

## Типові застосування
- **Бази даних** - зберігання інформації про користувачів, товари
- **Конфігураційні файли** - налаштування програм
- **Ігрові дані** - карти, персонажі, інвентар
- **Веб-розробка** - JSON API, структури сторінок
- **Наукові дані** - матриці, таблиці результатів
- **Файлові системи** - структура папок та файлів