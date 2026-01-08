# Приклад 3: Вкладені словники та складні структури

print("=== ВКЛАДЕНІ СЛОВНИКИ ===")

# База даних студентів з вкладеними структурами
students_database = {
    "STU001": {
        "personal_info": {
            "name": "Олексій Петренко",
            "age": 16,
            "birth_date": "2008-03-15",
            "city": "Київ"
        },
        "academic_info": {
            "class": "10-А",
            "year": 2024,
            "subjects": {
                "математика": {"grade": 10, "teacher": "Іваненко І.І."},
                "фізика": {"grade": 9, "teacher": "Петров П.П."},
                "англійська": {"grade": 11, "teacher": "Сміт Дж."}
            }
        },
        "contact_info": {
            "email": "alex.petrenko@school.edu",
            "phone": "+380501234567",
            "parent_phone": "+380507654321"
        },
        "activities": ["футбол", "програмування", "шахи"]
    },
    "STU002": {
        "personal_info": {
            "name": "Марія Іваненко",
            "age": 17,
            "birth_date": "2007-07-22",
            "city": "Львів"
        },
        "academic_info": {
            "class": "10-Б",
            "year": 2024,
            "subjects": {
                "математика": {"grade": 12, "teacher": "Іваненко І.І."},
                "хімія": {"grade": 10, "teacher": "Коваленко К.К."},
                "біологія": {"grade": 11, "teacher": "Біолог Б.Б."}
            }
        },
        "contact_info": {
            "email": "maria.ivanenko@school.edu",
            "phone": "+380631112233",
            "parent_phone": "+380637654321"
        },
        "activities": ["волейбол", "малювання", "музика"]
    }
}

print("1. Структура бази даних:")
print(f"Всього студентів: {len(students_database)}")

# Доступ до вкладених даних
print("\n2. Доступ до вкладених даних:")

student_id = "STU001"
student = students_database[student_id]

# Глибокий доступ
name = student["personal_info"]["name"]
age = student["personal_info"]["age"]
class_name = student["academic_info"]["class"]
email = student["contact_info"]["email"]

print(f"Студент {student_id}:")
print(f"  Ім'я: {name}")
print(f"  Вік: {age}")
print(f"  Клас: {class_name}")
print(f"  Email: {email}")

# Безпечний доступ до вкладених даних
def safe_get_nested(dictionary, *keys, default=None):
    """Безпечно отримує значення з вкладеного словника"""
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return default
    return dictionary

# Тестування безпечного доступу
phone = safe_get_nested(student, "contact_info", "phone", default="Не вказано")
missing = safe_get_nested(student, "contact_info", "address", default="Не вказано")

print(f"  Телефон: {phone}")
print(f"  Адреса: {missing}")

# Робота з предметами
print("\n3. Аналіз предметів:")

for student_id, student_data in students_database.items():
    name = student_data["personal_info"]["name"]
    subjects = student_data["academic_info"]["subjects"]
    
    print(f"\n{name} ({student_id}):")
    
    total_grade = 0
    subject_count = 0
    
    for subject, info in subjects.items():
        grade = info["grade"]
        teacher = info["teacher"]
        total_grade += grade
        subject_count += 1
        
        print(f"  {subject}: {grade} (вчитель: {teacher})")
    
    # Середня оцінка
    average = total_grade / subject_count if subject_count > 0 else 0
    print(f"  Середня оцінка: {average:.1f}")

# Пошук та фільтрація
print("\n4. Пошук та фільтрація:")

# Знайти студентів з певного міста
def find_students_by_city(database, city):
    """Знаходить студентів з певного міста"""
    result = []
    for student_id, data in database.items():
        if data["personal_info"]["city"] == city:
            result.append({
                "id": student_id,
                "name": data["personal_info"]["name"],
                "city": city
            })
    return result

kyiv_students = find_students_by_city(students_database, "Київ")
print(f"Студенти з Києва: {kyiv_students}")

# Знайти студентів з високими оцінками
def find_excellent_students(database, min_grade=10):
    """Знаходить студентів з високими оцінками"""
    result = []
    
    for student_id, data in database.items():
        name = data["personal_info"]["name"]
        subjects = data["academic_info"]["subjects"]
        
        high_grades = []
        for subject, info in subjects.items():
            if info["grade"] >= min_grade:
                high_grades.append(f"{subject}({info['grade']})")
        
        if high_grades:
            result.append({
                "name": name,
                "high_grades": high_grades
            })
    
    return result

excellent = find_excellent_students(students_database, 10)
print(f"\nВідмінники (оцінка ≥ 10):")
for student in excellent:
    print(f"  {student['name']}: {', '.join(student['high_grades'])}")

# Додавання нових даних
print("\n5. Додавання нових даних:")

# Додаємо нового студента
new_student = {
    "personal_info": {
        "name": "Іван Сидоренко",
        "age": 16,
        "birth_date": "2008-01-10",
        "city": "Одеса"
    },
    "academic_info": {
        "class": "10-В",
        "year": 2024,
        "subjects": {
            "математика": {"grade": 8, "teacher": "Іваненко І.І."},
            "географія": {"grade": 9, "teacher": "Географ Г.Г."}
        }
    },
    "contact_info": {
        "email": "ivan.sydorenko@school.edu",
        "phone": "+380441234567"
    },
    "activities": ["баскетбол", "читання"]
}

students_database["STU003"] = new_student
print(f"Додано нового студента. Всього: {len(students_database)}")

# Оновлення існуючих даних
print("\n6. Оновлення існуючих даних:")

# Додаємо новий предмет існуючому студенту
student_id = "STU001"
new_subject = {
    "інформатика": {"grade": 12, "teacher": "Програміст П.П."}
}

students_database[student_id]["academic_info"]["subjects"].update(new_subject)
print(f"Додано предмет 'інформатика' студенту {student_id}")

# Оновлюємо контактну інформацію
students_database[student_id]["contact_info"]["address"] = "вул. Хрещатик, 1"
print(f"Додано адресу студенту {student_id}")

# Статистика по базі даних
print("\n7. Статистика по базі даних:")

# Загальна статистика
total_students = len(students_database)
cities = set()
all_subjects = set()
all_activities = []

for student_data in students_database.values():
    # Міста
    cities.add(student_data["personal_info"]["city"])
    
    # Предмети
    subjects = student_data["academic_info"]["subjects"].keys()
    all_subjects.update(subjects)
    
    # Активності
    activities = student_data.get("activities", [])
    all_activities.extend(activities)

print(f"Загальна статистика:")
print(f"  Студентів: {total_students}")
print(f"  Міст: {len(cities)} ({', '.join(sorted(cities))})")
print(f"  Унікальних предметів: {len(all_subjects)}")
print(f"  Всього активностей: {len(all_activities)}")

# Найпопулярніші активності
activity_count = {}
for activity in all_activities:
    activity_count[activity] = activity_count.get(activity, 0) + 1

popular_activities = sorted(activity_count.items(), key=lambda x: x[1], reverse=True)
print(f"  Популярні активності:")
for activity, count in popular_activities[:3]:
    print(f"    {activity}: {count} студентів")

# Експорт даних
print("\n8. Експорт даних:")

def export_student_summary(database):
    """Створює спрощений звіт по студентах"""
    summary = []
    
    for student_id, data in database.items():
        # Обчислюємо середню оцінку
        subjects = data["academic_info"]["subjects"]
        grades = [info["grade"] for info in subjects.values()]
        avg_grade = sum(grades) / len(grades) if grades else 0
        
        summary.append({
            "id": student_id,
            "name": data["personal_info"]["name"],
            "class": data["academic_info"]["class"],
            "city": data["personal_info"]["city"],
            "average_grade": round(avg_grade, 1),
            "subjects_count": len(subjects),
            "activities_count": len(data.get("activities", []))
        })
    
    return summary

summary = export_student_summary(students_database)
print("Звіт по студентах:")
for student in summary:
    print(f"  {student['name']} ({student['class']}) - середня: {student['average_grade']}")

print("\n=== ВИСНОВКИ ===")
print("Вкладені словники дозволяють:")
print("• Створювати складні ієрархічні структури даних")
print("• Організовувати інформацію логічними групами")
print("• Легко розширювати та модифікувати структуру")
print("• Ефективно шукати та фільтрувати дані")
print("• Створювати гнучкі бази даних без SQL")
print("• Експортувати та аналізувати інформацію")