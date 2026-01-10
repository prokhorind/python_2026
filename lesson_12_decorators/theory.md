# Урок 12: Функції та декоратори. Декоратори

## Мета уроку
Вивчити декоратори в Python - потужний інструмент для модифікації поведінки функцій без зміни їх коду.

## Теоретичний матеріал

### 1. Що таке декоратор?

Декоратор - це функція, яка приймає іншу функцію і розширює її поведінку, не змінюючи її код.

```python
# Простий приклад
def my_decorator(func):
    def wrapper():
        print("Щось відбувається перед функцією")
        func()
        print("Щось відбувається після функції")
    return wrapper

@my_decorator
def say_hello():
    print("Привіт!")

say_hello()
# Виведе:
# Щось відбувається перед функцією
# Привіт!
# Щось відбувається після функції
```

### 2. Як працюють декоратори

```python
# Без декоратора (довгий спосіб)
def greet():
    print("Привіт!")

greet = my_decorator(greet)  # Обгортаємо функцію
greet()

# З декоратором (короткий спосіб)
@my_decorator
def greet():
    print("Привіт!")

greet()  # Результат той самий
```

### 3. Декоратор з параметрами функції

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        print(f"Аргументи: {args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

@log_decorator
def greet_person(name, age=18):
    return f"Привіт, {name}! Тобі {age} років."

# Тестування
result1 = add_numbers(5, 3)
result2 = greet_person("Марія", age=16)
```

### 4. Практичні декоратори

#### Декоратор для вимірювання часу

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функція {func.__name__} виконалась за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)  # Імітація повільної роботи
    return "Готово!"

result = slow_function()
```

#### Декоратор для підрахунку викликів

```python
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функція {func.__name__} викликана {wrapper.call_count} раз(ів)")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def say_hello():
    print("Привіт!")

say_hello()  # Функція say_hello викликана 1 раз(ів)
say_hello()  # Функція say_hello викликана 2 раз(ів)
say_hello()  # Функція say_hello викликана 3 раз(ів)
```

#### Декоратор для перевірки типів

```python
def type_check(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Очікувався {expected_type.__name__}, отримано {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int)
def multiply_numbers(a, b):
    return a * b

# Працює
result = multiply_numbers(5, 3)  # 15

# Викине помилку
# result = multiply_numbers(5, "3")  # TypeError
```

### 5. Декоратор класу

```python
def add_method(cls):
    def new_method(self):
        return f"Новий метод для {self.__class__.__name__}"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass("Тест")
print(obj.new_method())  # Новий метод для MyClass
```

### 6. Множинні декоратори

```python
def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

@bold
@italic
def get_text():
    return "Важливий текст"

print(get_text())  # ***Важливий текст***
```

### 7. Декоратор з параметрами

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Привіт!")

say_hello()
# Виведе "Привіт!" 3 рази
```

### 8. Збереження метаданих функції

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Зберігає ім'я та документацію оригінальної функції
    def wrapper(*args, **kwargs):
        print(f"Викликається {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """Це важлива функція"""
    return "Результат"

print(important_function.__name__)  # important_function (не wrapper)
print(important_function.__doc__)   # Це важлива функція
```

## Ключові поняття
- **Декоратор** - функція, яка модифікує поведінку іншої функції
- **@синтаксис** - спеціальний синтаксис для застосування декораторів
- **wrapper** - внутрішня функція декоратора, яка обгортає оригінальну функцію
- **\*args, \*\*kwargs** - дозволяє декоратору працювати з будь-якими аргументами
- **functools.wraps** - зберігає метадані оригінальної функції

## Практичні поради
1. Використовуйте декоратори для логування, вимірювання часу, кешування
2. Завжди використовуйте `*args, **kwargs` для універсальності
3. Використовуйте `functools.wraps` для збереження метаданих
4. Декоратори можна комбінувати
5. Для складної логіки краще створити клас-декоратор

## Коли використовувати декоратори:
- ✅ Логування викликів функцій
- ✅ Вимірювання часу виконання
- ✅ Перевірка прав доступу
- ✅ Кешування результатів
- ✅ Валідація вхідних даних
- ❌ Складна бізнес-логіка (краще винести в окрему функцію)