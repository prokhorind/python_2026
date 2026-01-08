# Приклад 4: Складні вкладені структури

print("=== СКЛАДНІ ВКЛАДЕНІ СТРУКТУРИ ===")

# ============================================================================
# 1. КОМПЛЕКСНА БАЗА ДАНИХ ШКОЛИ
# ============================================================================

print("1. Комплексна база даних школи")
print("-" * 40)

# Повна структура школи з усіма даними
school_database = {
    "school_info": {
        "name": "Ліцей №15 'Інтелект'",
        "address": {
            "street": "вул. Шевченка",
            "building": "25А",
            "city": "Київ",
            "postal_code": "01001"
        },
        "contacts": {
            "phone": "+380441234567",
            "email": "info@lyceum15.edu.ua",
            "website": "www.lyceum15.edu.ua"
        },
        "director": {
            "name": "Коваленко Петро Іванович",
            "phone": "+380441234568",
            "email": "director@lyceum15.edu.ua"
        },
        "founded": 1995,
        "total_students": 450,
        "total_teachers": 35
    },
    
    "classes": {
        "10-А": {
            "teacher": {
                "name": "Петренко Олена Іванівна",
                "subject": "математика",
                "phone": "+380501111111",
                "experience": 15
            },
            "students": [
                {
                    "id": 1001,
                    "name": "Анна Петренко",
                    "birth_date": "2007-03-15",
                    "address": {
                        "street": "вул. Лесі Українки",
                        "building": "12",
                        "apartment": "45"
                    },
                    "parents": [
                        {
                            "name": "Петренко Іван Михайлович",
                            "relation": "батько",
                            "phone": "+380501234567",
                            "work": "інженер"
                        },
                        {
                            "name": "Петренко Марія Олександрівна", 
                            "relation": "мати",
                            "phone": "+380671234567",
                            "work": "лікар"
                        }
                    ],
                    "grades": {
                        "математика": [12, 11, 12, 11],
                        "фізика": [11, 10, 11, 12],
                        "хімія": [10, 11, 10, 11],
                        "біологія": [12, 12, 11, 12]
                    },
                    "attendance": {
                        "total_days": 120,
                        "present_days": 115,
                        "sick_days": 3,
                        "other_absences": 2
                    }
                }
            ]
        }
    }
}

# Функції для роботи з комплексною структурою
def get_school_summary(database):
    """Повертає загальну інформацію про школу"""
    info = database["school_info"]
    
    return {
        "name": info["name"],
        "full_address": f"{info['address']['street']}, {info['address']['building']}, {info['address']['city']}",
        "contact_phone": info["contacts"]["phone"],
        "director": info["director"]["name"],
        "years_operating": 2024 - info["founded"],
        "students": info["total_students"],
        "teachers": info["total_teachers"]
    }

def calculate_student_average(student_grades):
    """Обчислює середній бал учня по всіх предметах"""
    all_grades = []
    
    for subject, grades in student_grades.items():
        all_grades.extend(grades)
    
    return sum(all_grades) / len(all_grades) if all_grades else 0

def get_student_attendance_rate(attendance):
    """Обчислює відсоток відвідуваності"""
    total = attendance["total_days"]
    present = attendance["present_days"]
    
    return (present / total * 100) if total > 0 else 0

# Демонстрація роботи з комплексною структурою
summary = get_school_summary(school_database)
print("Інформація про школу:")
print(f"  Назва: {summary['name']}")
print(f"  Адреса: {summary['full_address']}")
print(f"  Телефон: {summary['contact_phone']}")
print(f"  Директор: {summary['director']}")
print(f"  Років роботи: {summary['years_operating']}")
print(f"  Учнів: {summary['students']}")
print(f"  Вчителів: {summary['teachers']}")

# Робота з даними учня
student = school_database["classes"]["10-А"]["students"][0]
avg_grade = calculate_student_average(student["grades"])
attendance_rate = get_student_attendance_rate(student["attendance"])

print(f"\nІнформація про учня:")
print(f"  Ім'я: {student['name']}")
print(f"  Середній бал: {avg_grade:.2f}")
print(f"  Відвідуваність: {attendance_rate:.1f}%")
print(f"  Батьки:")
for parent in student["parents"]:
    print(f"    {parent['name']} ({parent['relation']}) - {parent['work']}")

# ============================================================================
# 2. СИСТЕМА УПРАВЛІННЯ ПРОЕКТАМИ
# ============================================================================

print("\n" + "=" * 50)
print("2. Система управління проектами")
print("-" * 40)

# Структура проектів з командами та завданнями
projects_system = {
    "projects": [
        {
            "id": "PROJ001",
            "name": "Розробка мобільного додатку",
            "description": "Створення додатку для замовлення їжі",
            "status": "в розробці",
            "start_date": "2024-01-01",
            "end_date": "2024-06-30",
            "budget": {
                "total": 500000,
                "spent": 150000,
                "currency": "грн"
            },
            "team": {
                "project_manager": {
                    "name": "Іваненко Олексій",
                    "email": "alex.ivanenko@company.com",
                    "phone": "+380501111111"
                },
                "developers": [
                    {
                        "name": "Петренко Анна",
                        "role": "Frontend Developer",
                        "skills": ["React", "JavaScript", "CSS"],
                        "hourly_rate": 800
                    },
                    {
                        "name": "Сидоренко Максим",
                        "role": "Backend Developer", 
                        "skills": ["Python", "Django", "PostgreSQL"],
                        "hourly_rate": 900
                    }
                ],
                "designer": {
                    "name": "Коваленко Марія",
                    "role": "UI/UX Designer",
                    "skills": ["Figma", "Adobe XD", "Photoshop"],
                    "hourly_rate": 700
                }
            },
            "tasks": [
                {
                    "id": "TASK001",
                    "title": "Створити дизайн головної сторінки",
                    "description": "Розробити макет головної сторінки додатку",
                    "assignee": "Коваленко Марія",
                    "status": "завершено",
                    "priority": "високий",
                    "estimated_hours": 16,
                    "actual_hours": 14,
                    "due_date": "2024-01-15",
                    "completed_date": "2024-01-14",
                    "subtasks": [
                        {"name": "Дослідження конкурентів", "completed": True},
                        {"name": "Створення wireframes", "completed": True},
                        {"name": "Дизайн макету", "completed": True},
                        {"name": "Презентація клієнту", "completed": True}
                    ]
                },
                {
                    "id": "TASK002",
                    "title": "Розробити API для користувачів",
                    "description": "Створити REST API для реєстрації та авторизації",
                    "assignee": "Сидоренко Максим",
                    "status": "в процесі",
                    "priority": "високий",
                    "estimated_hours": 24,
                    "actual_hours": 18,
                    "due_date": "2024-01-25",
                    "completed_date": None,
                    "subtasks": [
                        {"name": "Налаштування бази даних", "completed": True},
                        {"name": "Створення моделей", "completed": True},
                        {"name": "Розробка endpoints", "completed": False},
                        {"name": "Написання тестів", "completed": False}
                    ]
                }
            ]
        }
    ]
}

# Функції для роботи з проектами
def get_project_progress(project):
    """Обчислює прогрес проекту"""
    tasks = project["tasks"]
    if not tasks:
        return 0
    
    completed_tasks = len([t for t in tasks if t["status"] == "завершено"])
    return (completed_tasks / len(tasks)) * 100

def calculate_budget_usage(project):
    """Обчислює використання бюджету"""
    budget = project["budget"]
    usage_percent = (budget["spent"] / budget["total"]) * 100
    remaining = budget["total"] - budget["spent"]
    
    return {
        "usage_percent": usage_percent,
        "remaining": remaining,
        "spent": budget["spent"],
        "total": budget["total"]
    }

def get_team_cost_per_hour(project):
    """Обчислює вартість команди за годину"""
    team = project["team"]
    total_cost = 0
    
    # Додаємо розробників
    for dev in team["developers"]:
        total_cost += dev["hourly_rate"]
    
    # Додаємо дизайнера
    total_cost += team["designer"]["hourly_rate"]
    
    return total_cost

def get_overdue_tasks(project, current_date="2024-01-20"):
    """Знаходить прострочені завдання"""
    overdue = []
    
    for task in project["tasks"]:
        if (task["due_date"] < current_date and 
            task["status"] != "завершено"):
            overdue.append(task)
    
    return overdue

# Демонстрація роботи з проектами
project = projects_system["projects"][0]

print(f"Проект: {project['name']}")
print(f"Статус: {project['status']}")

# Прогрес проекту
progress = get_project_progress(project)
print(f"Прогрес: {progress:.1f}%")

# Бюджет
budget_info = calculate_budget_usage(project)
print(f"Бюджет: {budget_info['spent']:,} / {budget_info['total']:,} грн ({budget_info['usage_percent']:.1f}%)")
print(f"Залишилось: {budget_info['remaining']:,} грн")

# Команда
team_cost = get_team_cost_per_hour(project)
print(f"Вартість команди: {team_cost} грн/год")

# Прострочені завдання
overdue = get_overdue_tasks(project)
if overdue:
    print(f"Прострочені завдання ({len(overdue)}):")
    for task in overdue:
        print(f"  {task['title']} (дедлайн: {task['due_date']})")
else:
    print("Немає прострочених завдань")

# ============================================================================
# 3. СИСТЕМА ЕЛЕКТРОННОЇ КОМЕРЦІЇ
# ============================================================================

print("\n" + "=" * 50)
print("3. Система електронної комерції")
print("-" * 40)

# Структура інтернет-магазину
ecommerce_system = {
    "store_info": {
        "name": "TechStore Ukraine",
        "currency": "UAH",
        "tax_rate": 0.20,
        "shipping_zones": {
            "kyiv": {"name": "Київ", "cost": 50, "delivery_days": 1},
            "ukraine": {"name": "Україна", "cost": 100, "delivery_days": 3},
            "international": {"name": "Міжнародна", "cost": 500, "delivery_days": 7}
        }
    },
    
    "customers": [
        {
            "id": "CUST001",
            "personal_info": {
                "name": "Петренко Анна Іванівна",
                "email": "anna.petrenko@email.com",
                "phone": "+380501234567",
                "birth_date": "1990-05-15"
            },
            "addresses": [
                {
                    "type": "home",
                    "street": "вул. Хрещатик, 1",
                    "city": "Київ",
                    "postal_code": "01001",
                    "is_default": True
                },
                {
                    "type": "work",
                    "street": "вул. Льва Толстого, 15",
                    "city": "Київ", 
                    "postal_code": "01033",
                    "is_default": False
                }
            ],
            "payment_methods": [
                {
                    "type": "card",
                    "last_four": "1234",
                    "expiry": "12/26",
                    "is_default": True
                }
            ],
            "order_history": [
                {
                    "order_id": "ORD001",
                    "date": "2024-01-10",
                    "status": "доставлено",
                    "items": [
                        {
                            "product_id": "PROD001",
                            "name": "iPhone 15 Pro",
                            "price": 45000,
                            "quantity": 1,
                            "total": 45000
                        }
                    ],
                    "subtotal": 45000,
                    "tax": 9000,
                    "shipping": 50,
                    "total": 54050,
                    "shipping_address": {
                        "street": "вул. Хрещатик, 1",
                        "city": "Київ"
                    }
                }
            ],
            "preferences": {
                "newsletter": True,
                "sms_notifications": False,
                "favorite_categories": ["електроніка", "гаджети"]
            }
        }
    ]
}

# Функції для роботи з e-commerce системою
def calculate_customer_lifetime_value(customer):
    """Обчислює загальну вартість покупок клієнта"""
    total_spent = 0
    
    for order in customer["order_history"]:
        total_spent += order["total"]
    
    return total_spent

def get_customer_order_statistics(customer):
    """Повертає статистику замовлень клієнта"""
    orders = customer["order_history"]
    
    if not orders:
        return {"total_orders": 0, "average_order": 0, "total_spent": 0}
    
    total_orders = len(orders)
    total_spent = sum(order["total"] for order in orders)
    average_order = total_spent / total_orders
    
    # Статус замовлень
    status_counts = {}
    for order in orders:
        status = order["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    return {
        "total_orders": total_orders,
        "average_order": average_order,
        "total_spent": total_spent,
        "status_breakdown": status_counts
    }

def calculate_order_total(items, tax_rate, shipping_cost):
    """Обчислює загальну вартість замовлення"""
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping_cost
    
    return {
        "subtotal": subtotal,
        "tax": tax,
        "shipping": shipping_cost,
        "total": total
    }

# Демонстрація роботи з e-commerce
customer = ecommerce_system["customers"][0]

print(f"Клієнт: {customer['personal_info']['name']}")
print(f"Email: {customer['personal_info']['email']}")

# Статистика клієнта
stats = get_customer_order_statistics(customer)
print(f"\nСтатистика замовлень:")
print(f"  Всього замовлень: {stats['total_orders']}")
print(f"  Середнє замовлення: {stats['average_order']:,.0f} грн")
print(f"  Загальна сума: {stats['total_spent']:,.0f} грн")

# Адреси
print(f"\nАдреси клієнта:")
for addr in customer["addresses"]:
    default_mark = " (основна)" if addr["is_default"] else ""
    print(f"  {addr['type'].title()}: {addr['street']}, {addr['city']}{default_mark}")

# Останнє замовлення
if customer["order_history"]:
    last_order = customer["order_history"][-1]
    print(f"\nОстаннє замовлення ({last_order['order_id']}):")
    print(f"  Дата: {last_order['date']}")
    print(f"  Статус: {last_order['status']}")
    print(f"  Сума: {last_order['total']:,} грн")

print("\n=== ВИСНОВКИ ===")
print("Складні вкладені структури дозволяють:")
print("• Моделювати реальні бізнес-процеси")
print("• Зберігати пов'язані дані разом")
print("• Створювати гнучкі та масштабовані системи")
print("• Легко розширювати функціональність")
print("• Підтримувати цілісність даних")
print("• Ефективно працювати з комплексною інформацією")