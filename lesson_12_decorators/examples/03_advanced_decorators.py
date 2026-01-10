# Приклад 3: Декоратори в реальних ситуаціях

print("=== Декоратор для перевірки паролю ===")

# Імітуємо систему з паролем
current_password = "python123"

def require_password(func):
    """Декоратор, який вимагає правильний пароль"""
    def wrapper(password, *args, **kwargs):
        if password != current_password:
            print("❌ Неправильний пароль! Доступ заборонено.")
            return None
        
        print("✅ Пароль правильний! Доступ дозволено.")
        return func(*args, **kwargs)
    return wrapper

@require_password
def view_grades():
    """Переглянути оцінки (потрібен пароль)"""
    grades = [10, 8, 9, 11, 7]
    print(f"📊 Твої оцінки: {grades}")
    return grades

@require_password
def change_profile(new_name):
    """Змінити профіль (потрібен пароль)"""
    print(f"👤 Профіль змінено на: {new_name}")
    return f"Новий профіль: {new_name}"

print("Тестування системи з паролем:")
view_grades("wrongpassword")  # Помилка
view_grades("python123")      # Успіх
change_profile("python123", "Новий Іван")  # Успіх

print("\n=== Декоратор для обмеження спроб ===")

def limit_attempts(max_tries=3):
    """Декоратор, який обмежує кількість спроб"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, 'attempts'):
                wrapper.attempts = 0
            
            wrapper.attempts += 1
            
            if wrapper.attempts > max_tries:
                print(f"❌ Перевищено ліміт спроб ({max_tries})! Спробуй пізніше.")
                return None
            
            print(f"🔄 Спроба {wrapper.attempts} з {max_tries}")
            return func(*args, **kwargs)
        
        wrapper.reset = lambda: setattr(wrapper, 'attempts', 0)
        return wrapper
    return decorator

@limit_attempts(max_tries=3)
def try_login(username, password):
    """Спроба входу в систему"""
    correct_user = "student"
    correct_pass = "123456"
    
    if username == correct_user and password == correct_pass:
        print("✅ Успішний вхід!")
        return True
    else:
        print("❌ Неправильні дані!")
        return False

print("Тестування обмеження спроб:")
try_login("student", "wrong")     # Спроба 1
try_login("wrong", "123456")      # Спроба 2  
try_login("student", "123456")    # Спроба 3 - успіх
try_login("student", "123456")    # Спроба 4 - заблоковано

print("\n=== Декоратор для логування дій ===")

action_log = []

def log_action(action_name):
    """Декоратор для запису дій в лог"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            import datetime
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            
            print(f"📝 {timestamp} - Починаю дію: {action_name}")
            
            try:
                result = func(*args, **kwargs)
                log_entry = f"{timestamp} - {action_name} - УСПІХ"
                action_log.append(log_entry)
                print(f"✅ {timestamp} - Дія '{action_name}' завершена успішно")
                return result
            except Exception as e:
                log_entry = f"{timestamp} - {action_name} - ПОМИЛКА: {e}"
                action_log.append(log_entry)
                print(f"❌ {timestamp} - Помилка в дії '{action_name}': {e}")
                return None
        return wrapper
    return decorator

@log_action("Додавання оцінки")
def add_grade(student, subject, grade):
    """Додати оцінку студенту"""
    if grade < 1 or grade > 12:
        raise ValueError("Оцінка має бути від 1 до 12")
    
    message = f"Студенту {student} додано оцінку {grade} з предмету {subject}"
    print(message)
    return message

@log_action("Перегляд статистики")
def view_statistics():
    """Переглянути статистику"""
    stats = {"всього_студентів": 25, "середня_оцінка": 8.5}
    print(f"📈 Статистика: {stats}")
    return stats

print("Тестування логування дій:")
add_grade("Марія", "Математика", 10)
add_grade("Петро", "Фізика", 15)  # Помилка - оцінка > 12
view_statistics()

print(f"\nЛог дій ({len(action_log)} записів):")
for entry in action_log:
    print(f"  {entry}")

print("\n=== Декоратор для форматування виводу ===")

def format_as_box(func):
    """Декоратор, який оформлює результат в рамку"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            lines = str(result).split('\n')
            max_length = max(len(line) for line in lines)
            
            print("┌" + "─" * (max_length + 2) + "┐")
            for line in lines:
                print(f"│ {line:<{max_length}} │")
            print("└" + "─" * (max_length + 2) + "┘")
        
        return result
    return wrapper

@format_as_box
def show_student_card(name, age, grade):
    """Показати картку студента"""
    card = f"Студент: {name}\nВік: {age} років\nКлас: {grade}"
    return card

@format_as_box
def show_test_result(subject, score, max_score):
    """Показати результат тесту"""
    percentage = (score / max_score) * 100
    result = f"Предмет: {subject}\nБали: {score}/{max_score}\nВідсоток: {percentage:.1f}%"
    return result

print("Тестування форматування в рамку:")
show_student_card("Іван Петренко", 16, "10-А")
print()
show_test_result("Програмування", 18, 20)