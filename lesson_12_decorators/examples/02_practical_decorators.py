# Приклад 2: Практичні декоратори для початківців

print("=== Декоратор для вимірювання часу ===")

import time

def timer(func):
    """Простий декоратор для вимірювання часу"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Функція {func.__name__} працювала {end - start:.2f} секунд")
        return result
    return wrapper

@timer
def count_to_million():
    """Рахуємо до мільйона"""
    total = 0
    for i in range(1000000):
        total += i
    return total

@timer
def say_hello_slowly():
    """Повільне привітання"""
    time.sleep(1)  # Чекаємо 1 секунду
    print("Привіт після паузи!")

print("Тестування таймера:")
result = count_to_million()
print(f"Результат підрахунку: {result}")
say_hello_slowly()

print("\n=== Декоратор для підрахунку викликів (розширений) ===")

def advanced_counter(func):
    """Декоратор з детальним підрахунком"""
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"📊 {func.__name__} - виклик №{wrapper.calls}")
        result = func(*args, **kwargs)
        print(f"📊 Загалом викликів {func.__name__}: {wrapper.calls}")
        return result
    
    wrapper.calls = 0
    return wrapper

@advanced_counter
def calculate_square(x):
    result = x * x
    print(f"Квадрат {x} = {result}")
    return result

@advanced_counter
def greet_friend(name):
    message = f"Привіт, друже {name}!"
    print(message)
    return message

print("Тестування розширеного лічильника:")
calculate_square(3)
calculate_square(5)
greet_friend("Олексій")
greet_friend("Катя")
calculate_square(7)

print("\n=== Декоратор для перевірки віку ===")

def check_age(func):
    """Декоратор для перевірки віку (має бути 16+)"""
    def wrapper(name, age, *args, **kwargs):
        if age < 16:
            print(f"❌ {name}, тобі лише {age} років. Потрібно мінімум 16!")
            return None
        
        print(f"✅ {name}, твій вік {age} років - все ОК!")
        return func(name, age, *args, **kwargs)
    return wrapper

@check_age
def register_student(name, age, subject):
    message = f"🎓 {name} ({age} років) зареєстрований на курс '{subject}'"
    print(message)
    return message

print("Тестування перевірки віку:")
register_student("Марія", 17, "Програмування")
register_student("Петрик", 14, "Математика")
register_student("Іван", 16, "Фізика")

print("\n=== Декоратор для форматування результату ===")

def beautify_result(func):
    """Декоратор для красивого оформлення результату"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is not None:
            beautiful_result = f"✨ {result} ✨"
            print(beautiful_result)
            return beautiful_result
        return result
    return wrapper

@beautify_result
def get_grade_message(student, grade):
    if grade >= 10:
        return f"{student} отримав відмінну оцінку: {grade}!"
    elif grade >= 7:
        return f"{student} отримав хорошу оцінку: {grade}"
    else:
        return f"{student} отримав оцінку: {grade} (треба підтягнути)"

@beautify_result
def calculate_percentage(correct, total):
    if total == 0:
        return None
    percentage = (correct / total) * 100
    return f"Правильних відповідей: {percentage:.1f}%"

print("Тестування форматування:")
get_grade_message("Анна", 11)
get_grade_message("Богдан", 8)
get_grade_message("Віка", 5)
calculate_percentage(8, 10)
calculate_percentage(15, 20)