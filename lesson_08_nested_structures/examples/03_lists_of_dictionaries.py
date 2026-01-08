# Приклад 3: Списки словників

print("=== СПИСКИ СЛОВНИКІВ ===")

# ============================================================================
# 1. БАЗА ДАНИХ УЧНІВ
# ============================================================================

print("1. База даних учнів школи")
print("-" * 40)

# Створюємо базу даних учнів
students_database = [
    {
        "id": 1,
        "name": "Анна Петренко",
        "age": 16,
        "class": "10-А",
        "subjects": ["математика", "фізика", "хімія", "біологія"],
        "average_grade": 11.2,
        "phone": "+380501234567",
        "email": "anna.petrenko@school.edu"
    },
    {
        "id": 2,
        "name": "Борис Іваненко", 
        "age": 17,
        "class": "11-Б",
        "subjects": ["алгебра", "геометрія", "інформатика", "фізика"],
        "average_grade": 9.8,
        "phone": "+380502345678",
        "email": "boris.ivanenko@school.edu"
    },
    {
        "id": 3,
        "name": "Віра Сидоренко",
        "age": 16,
        "class": "10-В",
        "subjects": ["біологія", "хімія", "географія", "екологія"],
        "average_grade": 11.8,
        "phone": "+380503456789",
        "email": "vira.sydorenko@school.edu"
    },
    {
        "id": 4,
        "name": "Григорій Коваленко",
        "age": 17,
        "class": "11-А",
        "subjects": ["історія", "література", "англійська", "німецька"],
        "average_grade": 8.9,
        "phone": "+380504567890",
        "email": "hryhoriy.kovalenko@school.edu"
    },
    {
        "id": 5,
        "name": "Дарина Мельник",
        "age": 16,
        "class": "10-Б",
        "subjects": ["математика", "інформатика", "англійська", "фізика"],
        "average_grade": 10.5,
        "phone": "+380505678901",
        "email": "daryna.melnyk@school.edu"
    }
]

print("База даних учнів:")
for student in students_database:
    print(f"ID: {student['id']}")
    print(f"  Ім'я: {student['name']}")
    print(f"  Вік: {student['age']}")
    print(f"  Клас: {student['class']}")
    print(f"  Предмети: {', '.join(student['subjects'])}")
    print(f"  Середній бал: {student['average_grade']}")
    print(f"  Контакт: {student['phone']}")
    print()

# Функції для роботи з базою учнів
def find_student_by_id(database, student_id):
    """Знаходить учня за ID"""
    for student in database:
        if student['id'] == student_id:
            return student
    return None

def find_students_by_class(database, class_name):
    """Знаходить всіх учнів певного класу"""
    result = []
    for student in database:
        if student['class'] == class_name:
            result.append(student)
    return result

def find_top_students(database, min_grade=10.0):
    """Знаходить учнів з високим середнім балом"""
    result = []
    for student in database:
        if student['average_grade'] >= min_grade:
            result.append(student)
    
    # Сортуємо за середнім балом (від найвищого)
    result.sort(key=lambda x: x['average_grade'], reverse=True)
    return result

def find_students_by_subject(database, subject):
    """Знаходить учнів, які вивчають певний предмет"""
    result = []
    for student in database:
        if subject in student['subjects']:
            result.append(student)
    return result

def get_age_statistics(database):
    """Обчислює статистику по віку"""
    ages = [student['age'] for student in database]
    
    return {
        "total_students": len(database),
        "average_age": sum(ages) / len(ages),
        "min_age": min(ages),
        "max_age": max(ages),
        "age_16_count": ages.count(16),
        "age_17_count": ages.count(17)
    }

# Тестуємо функції
print("--- Тестування функцій ---")

# Пошук за ID
student = find_student_by_id(students_database, 3)
if student:
    print(f"Учень з ID 3: {student['name']} ({student['class']})")

# Пошук за класом
class_10a = find_students_by_class(students_database, "10-А")
print(f"\nУчні класу 10-А:")
for student in class_10a:
    print(f"  {student['name']} (бал: {student['average_grade']})")

# Топ учні
print(f"\nТоп учні (середній бал >= 10.5):")
top_students = find_top_students(students_database, 10.5)
for i, student in enumerate(top_students, 1):
    print(f"  {i}. {student['name']} - {student['average_grade']}")

# Пошук за предметом
math_students = find_students_by_subject(students_database, "математика")
print(f"\nУчні, які вивчають математику:")
for student in math_students:
    print(f"  {student['name']} ({student['class']})")

# Статистика по віку
age_stats = get_age_statistics(students_database)
print(f"\nСтатистика по віку:")
print(f"  Всього учнів: {age_stats['total_students']}")
print(f"  Середній вік: {age_stats['average_age']:.1f}")
print(f"  16 років: {age_stats['age_16_count']} учнів")
print(f"  17 років: {age_stats['age_17_count']} учнів")

# ============================================================================
# 2. КАТАЛОГ ТОВАРІВ ІНТЕРНЕТ-МАГАЗИНУ
# ============================================================================

print("\n" + "=" * 50)
print("2. Каталог товарів інтернет-магазину")
print("-" * 40)

# База товарів
products_catalog = [
    {
        "id": 101,
        "name": "Смартфон Samsung Galaxy A54",
        "category": "електроніка",
        "price": 12999,
        "currency": "грн",
        "in_stock": 15,
        "rating": 4.5,
        "reviews_count": 127,
        "tags": ["смартфон", "android", "samsung", "5g"]
    },
    {
        "id": 102,
        "name": "Ноутбук ASUS VivoBook",
        "category": "електроніка",
        "price": 25999,
        "currency": "грн",
        "in_stock": 8,
        "rating": 4.2,
        "reviews_count": 89,
        "tags": ["ноутбук", "asus", "windows", "офіс"]
    },
    {
        "id": 103,
        "name": "Навушники Sony WH-1000XM4",
        "category": "аудіо",
        "price": 8999,
        "currency": "грн",
        "in_stock": 23,
        "rating": 4.8,
        "reviews_count": 245,
        "tags": ["навушники", "sony", "bluetooth", "шумозаглушення"]
    },
    {
        "id": 104,
        "name": "Футболка Nike Dri-FIT",
        "category": "одяг",
        "price": 1299,
        "currency": "грн",
        "in_stock": 50,
        "rating": 4.3,
        "reviews_count": 67,
        "tags": ["футболка", "nike", "спорт", "dri-fit"]
    },
    {
        "id": 105,
        "name": "Книга 'Python для початківців'",
        "category": "книги",
        "price": 599,
        "currency": "грн",
        "in_stock": 12,
        "rating": 4.7,
        "reviews_count": 34,
        "tags": ["книга", "програмування", "python", "навчання"]
    }
]

print("Каталог товарів:")
for product in products_catalog:
    availability = "В наявності" if product['in_stock'] > 0 else "Немає в наявності"
    print(f"ID: {product['id']}")
    print(f"  Назва: {product['name']}")
    print(f"  Категорія: {product['category']}")
    print(f"  Ціна: {product['price']} {product['currency']}")
    print(f"  Наявність: {product['in_stock']} шт. ({availability})")
    print(f"  Рейтинг: {product['rating']}/5 ({product['reviews_count']} відгуків)")
    print(f"  Теги: {', '.join(product['tags'])}")
    print()

# Функції для роботи з каталогом
def find_products_by_category(catalog, category):
    """Знаходить товари за категорією"""
    return [product for product in catalog if product['category'] == category]

def find_products_in_price_range(catalog, min_price, max_price):
    """Знаходить товари в ціновому діапазоні"""
    result = []
    for product in catalog:
        if min_price <= product['price'] <= max_price:
            result.append(product)
    return result

def find_products_by_tag(catalog, tag):
    """Знаходить товари за тегом"""
    result = []
    for product in catalog:
        if tag.lower() in [t.lower() for t in product['tags']]:
            result.append(product)
    return result

def get_top_rated_products(catalog, min_rating=4.0):
    """Знаходить товари з високим рейтингом"""
    result = []
    for product in catalog:
        if product['rating'] >= min_rating:
            result.append(product)
    
    # Сортуємо за рейтингом
    result.sort(key=lambda x: x['rating'], reverse=True)
    return result

def calculate_total_inventory_value(catalog):
    """Обчислює загальну вартість товарів на складі"""
    total_value = 0
    for product in catalog:
        total_value += product['price'] * product['in_stock']
    return total_value

def get_low_stock_products(catalog, threshold=10):
    """Знаходить товари з низькими залишками"""
    return [product for product in catalog if product['in_stock'] <= threshold]

# Тестуємо функції каталогу
print("--- Робота з каталогом ---")

# Пошук за категорією
electronics = find_products_by_category(products_catalog, "електроніка")
print(f"Товари категорії 'електроніка' ({len(electronics)} шт.):")
for product in electronics:
    print(f"  {product['name']} - {product['price']} грн")

# Пошук за ціною
affordable = find_products_in_price_range(products_catalog, 500, 2000)
print(f"\nТовари від 500 до 2000 грн:")
for product in affordable:
    print(f"  {product['name']} - {product['price']} грн")

# Пошук за тегом
nike_products = find_products_by_tag(products_catalog, "nike")
print(f"\nТовари Nike:")
for product in nike_products:
    print(f"  {product['name']}")

# Топ товари за рейтингом
top_rated = get_top_rated_products(products_catalog, 4.5)
print(f"\nТоп товари (рейтинг >= 4.5):")
for product in top_rated:
    print(f"  {product['name']} - {product['rating']}/5")

# Загальна вартість
total_value = calculate_total_inventory_value(products_catalog)
print(f"\nЗагальна вартість товарів на складі: {total_value:,} грн")

# Товари з низькими залишками
low_stock = get_low_stock_products(products_catalog, 15)
print(f"\nТовари з низькими залишками (<= 15 шт.):")
for product in low_stock:
    print(f"  {product['name']} - {product['in_stock']} шт.")

# ============================================================================
# 3. СИСТЕМА УПРАВЛІННЯ ЗАВДАННЯМИ (TODO LIST)
# ============================================================================

print("\n" + "=" * 50)
print("3. Система управління завданнями")
print("-" * 40)

# База завдань
tasks_list = [
    {
        "id": 1,
        "title": "Зробити домашнє завдання з математики",
        "description": "Розв'язати задачі 15-20 на сторінці 45",
        "priority": "високий",
        "status": "в процесі",
        "due_date": "2024-01-15",
        "category": "навчання",
        "estimated_hours": 2,
        "tags": ["математика", "домашка", "терміново"]
    },
    {
        "id": 2,
        "title": "Підготуватись до контрольної з фізики",
        "description": "Повторити розділи про механіку та термодинаміку",
        "priority": "високий",
        "status": "не розпочато",
        "due_date": "2024-01-18",
        "category": "навчання",
        "estimated_hours": 4,
        "tags": ["фізика", "контрольна", "повторення"]
    },
    {
        "id": 3,
        "title": "Прибрати кімнату",
        "description": "Пропилососити, протерти пил, розібрати речі",
        "priority": "середній",
        "status": "завершено",
        "due_date": "2024-01-12",
        "category": "дім",
        "estimated_hours": 1,
        "tags": ["прибирання", "кімната"]
    },
    {
        "id": 4,
        "title": "Прочитати книгу 'Гаррі Поттер'",
        "description": "Дочитати до 200 сторінки",
        "priority": "низький",
        "status": "в процесі",
        "due_date": "2024-01-25",
        "category": "хобі",
        "estimated_hours": 3,
        "tags": ["читання", "книга", "фентезі"]
    },
    {
        "id": 5,
        "title": "Піти в спортзал",
        "description": "Тренування ніг та спини",
        "priority": "середній",
        "status": "не розпочато",
        "due_date": "2024-01-14",
        "category": "спорт",
        "estimated_hours": 1.5,
        "tags": ["спорт", "здоров'я", "тренування"]
    }
]

print("Список завдань:")
for task in tasks_list:
    status_emoji = {"не розпочато": "⏳", "в процесі": "🔄", "завершено": "✅"}
    priority_emoji = {"високий": "🔴", "середній": "🟡", "низький": "🟢"}
    
    print(f"ID: {task['id']} {status_emoji.get(task['status'], '❓')}")
    print(f"  Назва: {task['title']}")
    print(f"  Пріоритет: {priority_emoji.get(task['priority'], '⚪')} {task['priority']}")
    print(f"  Статус: {task['status']}")
    print(f"  Дедлайн: {task['due_date']}")
    print(f"  Категорія: {task['category']}")
    print(f"  Час: {task['estimated_hours']} год")
    print(f"  Теги: {', '.join(task['tags'])}")
    print()

# Функції для управління завданнями
def find_tasks_by_status(tasks, status):
    """Знаходить завдання за статусом"""
    return [task for task in tasks if task['status'] == status]

def find_tasks_by_priority(tasks, priority):
    """Знаходить завдання за пріоритетом"""
    return [task for task in tasks if task['priority'] == priority]

def find_tasks_by_category(tasks, category):
    """Знаходить завдання за категорією"""
    return [task for task in tasks if task['category'] == category]

def get_overdue_tasks(tasks, current_date="2024-01-13"):
    """Знаходить прострочені завдання"""
    overdue = []
    for task in tasks:
        if task['due_date'] < current_date and task['status'] != "завершено":
            overdue.append(task)
    return overdue

def calculate_total_work_hours(tasks, status_filter=None):
    """Обчислює загальну кількість годин роботи"""
    total_hours = 0
    for task in tasks:
        if status_filter is None or task['status'] == status_filter:
            total_hours += task['estimated_hours']
    return total_hours

def get_tasks_statistics(tasks):
    """Повертає статистику завдань"""
    total = len(tasks)
    completed = len([t for t in tasks if t['status'] == 'завершено'])
    in_progress = len([t for t in tasks if t['status'] == 'в процесі'])
    not_started = len([t for t in tasks if t['status'] == 'не розпочато'])
    
    high_priority = len([t for t in tasks if t['priority'] == 'високий'])
    
    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "not_started": not_started,
        "completion_rate": (completed / total * 100) if total > 0 else 0,
        "high_priority": high_priority
    }

# Тестуємо функції завдань
print("--- Управління завданнями ---")

# Завдання за статусом
in_progress = find_tasks_by_status(tasks_list, "в процесі")
print(f"Завдання в процесі ({len(in_progress)}):")
for task in in_progress:
    print(f"  {task['title']} (дедлайн: {task['due_date']})")

# Високопріоритетні завдання
high_priority = find_tasks_by_priority(tasks_list, "високий")
print(f"\nВисокопріоритетні завдання ({len(high_priority)}):")
for task in high_priority:
    print(f"  {task['title']} - {task['status']}")

# Навчальні завдання
study_tasks = find_tasks_by_category(tasks_list, "навчання")
print(f"\nНавчальні завдання ({len(study_tasks)}):")
for task in study_tasks:
    print(f"  {task['title']} ({task['estimated_hours']} год)")

# Прострочені завдання
overdue = get_overdue_tasks(tasks_list)
print(f"\nПрострочені завдання ({len(overdue)}):")
for task in overdue:
    print(f"  {task['title']} (дедлайн був: {task['due_date']})")

# Загальна кількість годин
total_hours = calculate_total_work_hours(tasks_list)
remaining_hours = calculate_total_work_hours(tasks_list, "не розпочато")
print(f"\nЗагальна кількість годин роботи: {total_hours}")
print(f"Залишилось годин роботи: {remaining_hours}")

# Статистика
stats = get_tasks_statistics(tasks_list)
print(f"\nСтатистика завдань:")
print(f"  Всього завдань: {stats['total']}")
print(f"  Завершено: {stats['completed']}")
print(f"  В процесі: {stats['in_progress']}")
print(f"  Не розпочато: {stats['not_started']}")
print(f"  Відсоток виконання: {stats['completion_rate']:.1f}%")
print(f"  Високопріоритетних: {stats['high_priority']}")

print("\n=== ВИСНОВКИ ===")
print("Списки словників ідеальні для:")
print("• Баз даних з однотипними записами")
print("• Каталогів товарів, учнів, завдань")
print("• Систем управління контентом")
print("• API відповідей та JSON структур")
print("• Легкого пошуку, фільтрації та сортування")
print("• Масштабованих структур даних")