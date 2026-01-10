# Приклад 1: Основи декораторів

print("=== Що таке декоратор? ===")
print("Декоратор - це функція, яка 'обгортає' іншу функцію")
print("і додає їй нову функціональність\n")

# Найпростіший декоратор
def simple_decorator(func):
    """Найпростіший декоратор"""
    def wrapper():
        print("Щось робимо ДО виклику функції")
        func()  # Викликаємо оригінальну функцію
        print("Щось робимо ПІСЛЯ виклику функції")
    return wrapper

# Функція без декоратора
def say_hello():
    print("Привіт!")

print("Функція без декоратора:")
say_hello()

print("\nТа ж функція з декоратором:")
decorated_hello = simple_decorator(say_hello)
decorated_hello()

print("\n=== Використання @ синтаксису ===")

# Той самий декоратор, але з @ синтаксисом
@simple_decorator
def say_goodbye():
    print("До побачення!")

say_goodbye()

print("\n=== Декоратор з аргументами ===")

def log_function(func):
    """Декоратор, який показує ім'я функції"""
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функція {func.__name__} завершена")
        return result
    return wrapper

@log_function
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

@log_function
def greet_student(name):
    message = f"Привіт, {name}!"
    print(message)
    return message

print("Тестування функцій з логуванням:")
add_numbers(3, 5)
print()
greet_student("Марія")

print("\n=== Простий декоратор підрахунку ===")

def count_calls(func):
    """Декоратор, який рахує виклики функції"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функція {func.__name__} викликана {wrapper.count} раз(ів)")
        return func(*args, **kwargs)
    
    wrapper.count = 0  # Початкове значення лічильника
    return wrapper

@count_calls
def say_hi():
    print("Привіт!")

print("Тестування підрахунку викликів:")
say_hi()
say_hi()
say_hi()

print("\n=== Декоратор з перевіркою ===")

def check_positive_numbers(func):
    """Декоратор, який перевіряє чи всі числа позитивні"""
    def wrapper(*args, **kwargs):
        # Перевіряємо всі аргументи
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                print("❌ Помилка: всі числа повинні бути позитивними!")
                return None
        
        # Якщо все ОК, викликаємо функцію
        return func(*args, **kwargs)
    return wrapper

@check_positive_numbers
def multiply(a, b):
    result = a * b
    print(f"{a} × {b} = {result}")
    return result

print("Тестування перевірки позитивних чисел:")
multiply(4, 5)  # Працює
multiply(-2, 3)  # Помилка