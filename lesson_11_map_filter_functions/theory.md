# Урок 11: Функції та декоратори. map, filter та інші

## Мета уроку
Поглибити знання про вбудовані функції Python: map(), filter(), sorted(), zip() та інші корисні функції для роботи з даними.

## Теоретичний матеріал

### 1. Функція map() - перетворення даних

`map()` застосовує функцію до кожного елемента послідовності.

```python
# Основний синтаксис
map(функція, послідовність)

# Приклад: піднести числа до квадрата
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# З звичайною функцією
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

### 2. Функція filter() - фільтрація даних

`filter()` залишає тільки ті елементи, які відповідають умові.

```python
# Основний синтаксис
filter(функція_умова, послідовність)

# Приклад: тільки парні числа
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# Фільтрація рядків за довжиною
words = ["кіт", "собака", "миша", "слон"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)  # ['собака', 'слон']
```

### 3. Функція sorted() - сортування

`sorted()` сортує послідовність за заданим критерієм.

```python
# Основний синтаксис
sorted(послідовність, key=функція_ключа, reverse=False)

# Приклад: сортування чисел
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Сортування рядків за довжиною
words = ["кіт", "собака", "миша", "слон"]
by_length = sorted(words, key=lambda word: len(word))
print(by_length)  # ['кіт', 'слон', 'миша', 'собака']

# Сортування у зворотному порядку
reverse_sorted = sorted(numbers, reverse=True)
print(reverse_sorted)  # [9, 6, 5, 4, 3, 2, 1, 1]
```

### 4. Функція zip() - об'єднання послідовностей

`zip()` об'єднує кілька послідовностей в одну.

```python
# Основний синтаксис
zip(послідовність1, послідовність2, ...)

# Приклад: об'єднання імен та віку
names = ["Іван", "Марія", "Петро"]
ages = [16, 17, 15]
combined = list(zip(names, ages))
print(combined)  # [('Іван', 16), ('Марія', 17), ('Петро', 15)]

# Створення словника
student_dict = dict(zip(names, ages))
print(student_dict)  # {'Іван': 16, 'Марія': 17, 'Петро': 15}
```

### 5. Функція enumerate() - нумерація елементів

`enumerate()` додає індекси до елементів послідовності.

```python
# Основний синтаксис
enumerate(послідовність, start=0)

# Приклад: нумерація студентів
students = ["Іван", "Марія", "Петро"]
numbered = list(enumerate(students))
print(numbered)  # [(0, 'Іван'), (1, 'Марія'), (2, 'Петро')]

# Починаючи з 1
numbered_from_1 = list(enumerate(students, start=1))
print(numbered_from_1)  # [(1, 'Іван'), (2, 'Марія'), (3, 'Петро')]
```

### 6. Функції any() та all()

`any()` повертає True, якщо хоча б один елемент True.
`all()` повертає True, якщо всі елементи True.

```python
# Приклад з any()
numbers = [0, 0, 1, 0]
print(any(numbers))  # True (є хоча б одна 1)

# Приклад з all()
positive_numbers = [1, 2, 3, 4]
print(all(positive_numbers))  # True (всі числа > 0)

negative_numbers = [1, 2, 0, 4]
print(all(negative_numbers))  # False (є 0)

# З умовами
grades = [85, 92, 78, 96, 88]
print(any(grade > 90 for grade in grades))  # True
print(all(grade >= 70 for grade in grades))  # True
```

### 7. Комбінування функцій

```python
# Приклад: знайти квадрати парних чисел > 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(
    lambda x: x ** 2,                    # піднести до квадрата
    filter(lambda x: x % 2 == 0,         # тільки парні
           filter(lambda x: x > 5,       # тільки > 5
                  numbers))
))
print(result)  # [36, 64, 100]

# Те саме, але читабельніше
big_numbers = filter(lambda x: x > 5, numbers)
even_big_numbers = filter(lambda x: x % 2 == 0, big_numbers)
squares = map(lambda x: x ** 2, even_big_numbers)
result = list(squares)
print(result)  # [36, 64, 100]
```

## Ключові поняття
- **map()** - застосовує функцію до кожного елемента
- **filter()** - залишає елементи, що відповідають умові
- **sorted()** - сортує послідовність
- **zip()** - об'єднує кілька послідовностей
- **enumerate()** - додає індекси до елементів
- **any()/all()** - перевіряють умови для всіх елементів

## Практичні поради
1. Завжди використовуйте `list()` для перетворення результатів map() та filter()
2. Комбінуйте функції для складних операцій
3. Використовуйте зрозумілі імена змінних
4. Для складної логіки краще створити окрему функцію замість довгої лямбда
5. sorted() не змінює оригінальний список, а створює новий

## Коли використовувати:
- **map()**: коли потрібно перетворити кожен елемент
- **filter()**: коли потрібно відібрати елементи за умовою
- **sorted()**: коли потрібно відсортувати дані
- **zip()**: коли потрібно об'єднати кілька списків
- **enumerate()**: коли потрібні індекси елементів