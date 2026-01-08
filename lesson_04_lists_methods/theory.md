# Урок 4: Списки - методи та операції

## Мета уроку
Детально вивчити роботу зі списками: методи додавання, видалення, сортування та пошуку елементів.

## Теоретичний матеріал

### 1. Створення та базові операції зі списками

```python
# Різні способи створення списків
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = ["текст", 42, True, 3.14]
repeated = [0] * 5  # [0, 0, 0, 0, 0]

# Доступ до елементів
print(numbers[0])    # Перший елемент: 1
print(numbers[-1])   # Останній елемент: 5
print(numbers[1:4])  # Зріз: [2, 3, 4]

# Зміна елементів
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
```

### 2. Методи додавання елементів

```python
fruits = ["яблуко", "банан"]

# append() - додає елемент в кінець
fruits.append("апельсин")
print(fruits)  # ["яблуко", "банан", "апельсин"]

# insert() - вставляє елемент на певну позицію
fruits.insert(1, "груша")
print(fruits)  # ["яблуко", "груша", "банан", "апельсин"]

# extend() - додає всі елементи з іншого списку
more_fruits = ["ківі", "манго"]
fruits.extend(more_fruits)
print(fruits)  # ["яблуко", "груша", "банан", "апельсин", "ківі", "манго"]

# Оператор + для об'єднання
berries = ["полуниця", "малина"]
all_fruits = fruits + berries
print(all_fruits)
```

### 3. Методи видалення елементів

```python
grades = [10, 8, 9, 7, 10, 6, 9]

# remove() - видаляє перше входження елемента
grades.remove(10)  # Видалить перший 10
print(grades)  # [8, 9, 7, 10, 6, 9]

# pop() - видаляє та повертає елемент за індексом
last_grade = grades.pop()  # Видалить останній
print(f"Видалена оцінка: {last_grade}")  # 9
print(grades)  # [8, 9, 7, 10, 6]

specific_grade = grades.pop(2)  # Видалить елемент з індексом 2
print(f"Видалена оцінка: {specific_grade}")  # 7

# del - видаляє елемент за індексом
del grades[0]  # Видалить перший елемент
print(grades)  # [9, 10, 6]

# clear() - очищає весь список
# grades.clear()  # grades стане []
```

### 4. Пошук та перевірка

```python
subjects = ["математика", "фізика", "хімія", "біологія", "англійська"]

# in/not in - перевірка наявності
if "математика" in subjects:
    print("Математика є в списку")

if "географія" not in subjects:
    print("Географії немає в списку")

# index() - знаходить індекс елемента
math_index = subjects.index("математика")
print(f"Математика на позиції: {math_index}")

# count() - підраховує кількість входжень
numbers = [1, 2, 3, 2, 4, 2, 5]
count_2 = numbers.count(2)
print(f"Число 2 зустрічається {count_2} разів")
```

### 5. Сортування та зміна порядку

```python
scores = [85, 92, 78, 96, 88, 91]

# sort() - сортує список на місці
scores.sort()
print(f"За зростанням: {scores}")

scores.sort(reverse=True)
print(f"За спаданням: {scores}")

# sorted() - повертає новий відсортований список
original = [3, 1, 4, 1, 5, 9]
sorted_copy = sorted(original)
print(f"Оригінал: {original}")
print(f"Відсортована копія: {sorted_copy}")

# reverse() - змінює порядок на протилежний
names = ["Анна", "Борис", "Віра", "Григорій"]
names.reverse()
print(f"У зворотному порядку: {names}")

# Сортування рядків
names.sort()  # За алфавітом
print(f"За алфавітом: {names}")
```

### 6. Корисні функції для роботи зі списками

```python
test_scores = [85, 92, 78, 96, 88]

# len() - довжина списку
print(f"Кількість оцінок: {len(test_scores)}")

# sum() - сума всіх елементів
total = sum(test_scores)
print(f"Сума оцінок: {total}")

# min() та max() - мінімальне та максимальне значення
print(f"Найнижча оцінка: {min(test_scores)}")
print(f"Найвища оцінка: {max(test_scores)}")

# Середнє арифметичне
average = sum(test_scores) / len(test_scores)
print(f"Середня оцінка: {round(average, 2)}")

# enumerate() - отримання індексу та значення
print("Оцінки з номерами:")
for i, score in enumerate(test_scores, 1):
    print(f"{i}. {score} балів")
```

### 7. Списки та цикли

```python
# Створення списку через цикл
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Квадрати: {squares}")

# List comprehension (спрощений запис)
squares_short = [i ** 2 for i in range(1, 6)]
print(f"Квадрати (коротко): {squares_short}")

# Фільтрація списку
all_grades = [10, 7, 8, 12, 6, 9, 11, 5]
good_grades = []
for grade in all_grades:
    if grade >= 9:
        good_grades.append(grade)
print(f"Хороші оцінки: {good_grades}")

# Фільтрація через list comprehension
good_grades_short = [grade for grade in all_grades if grade >= 9]
print(f"Хороші оцінки (коротко): {good_grades_short}")
```

## Ключові поняття
- **append()** - додає елемент в кінець списку
- **insert()** - вставляє елемент на певну позицію
- **remove()** - видаляє перше входження елемента
- **pop()** - видаляє та повертає елемент за індексом
- **index()** - знаходить позицію елемента
- **sort()** - сортує список на місці
- **sorted()** - повертає новий відсортований список

## Практичні поради
1. Використовуйте append() для додавання одного елемента
2. extend() для додавання кількох елементів з іншого списку
3. Перевіряйте наявність елемента перед видаленням
4. sort() змінює оригінальний список, sorted() створює новий
5. Використовуйте enumerate() для отримання індексів у циклі
6. len(), sum(), min(), max() - корисні функції для аналізу списків