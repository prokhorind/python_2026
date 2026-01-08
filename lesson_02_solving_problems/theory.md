# Урок 2: Розв'язання задач з циклів та функцій

## Мета уроку
Закріпити навички роботи з циклами та функціями через практичне розв'язання задач.

## Теоретичний матеріал

### 1. Цикли для обробки чисел

```python
# Обчислення суми чисел від 1 до 10
total = 0
for i in range(1, 11):
    total += i
print(f"Сума чисел від 1 до 10: {total}")

# Знаходження найбільшого з введених чисел
max_num = int(input("Введи перше число: "))
for i in range(4):  # Ще 4 числа
    num = int(input(f"Введи число {i+2}: "))
    if num > max_num:
        max_num = num
print(f"Найбільше число: {max_num}")
```

### 2. Функції з параметрами

```python
def calculate_grade(points, max_points):
    """Обчислює оцінку у відсотках"""
    percentage = (points / max_points) * 100
    return round(percentage, 1)

def get_letter_grade(percentage):
    """Повертає літерну оцінку"""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    else:
        return "F"

# Використання функцій
student_points = 85
max_points = 100
percentage = calculate_grade(student_points, max_points)
letter = get_letter_grade(percentage)
print(f"Результат: {percentage}% ({letter})")
```

### 3. Цикли з умовами

```python
# Підрахунок парних чисел від 1 до 20
even_count = 0
for i in range(1, 21):
    if i % 2 == 0:
        even_count += 1

print(f"Парних чисел від 1 до 20: {even_count}")

# Знаходження всіх дільників числа
number = 12
print(f"Дільники числа {number}:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print()  # Новий рядок
```

### 4. Функції з циклами

```python
def sum_range(start, end):
    """Обчислює суму чисел у діапазоні"""
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

def count_digits(number):
    """Підраховує кількість цифр у числі"""
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

def is_prime(n):
    """Перевіряє, чи є число простим"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Приклади використання
print(f"Сума від 1 до 100: {sum_range(1, 100)}")
print(f"Кількість цифр у числі 12345: {count_digits(12345)}")
print(f"Чи є 17 простим числом? {is_prime(17)}")
```

## Ключові поняття
- **Ітерація** - проходження через елементи послідовності
- **Акумулятор** - змінна для накопичення результату
- **Фільтрація** - відбір елементів за певною умовою
- **Параметри функції** - вхідні дані для функції
- **Повернення значення** - результат роботи функції

## Практичні поради
1. Використовуйте змістовні імена змінних у циклах
2. Ініціалізуйте акумулятори перед циклом
3. Розбивайте складні задачі на прості функції
4. Тестуйте функції з різними вхідними даними
5. Використовуйте коментарі для пояснення логіки