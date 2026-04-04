# 🔹 Лямбда функції, map, filter, reduce у Python

---

## 🔸 1. Що таке lambda

Lambda — це анонімна функція:
- без імені
- в один рядок
- автоматично повертає результат

Синтаксис:
lambda аргументи: вираз

Приклад:
square = lambda x: x * x  
print(square(5))  # 25

---

## 🔸 2. map()

map застосовує функцію до кожного елемента списку.

Приклад:
nums = [1, 2, 3, 4]  
result = list(map(lambda x: x * 2, nums))  
print(result)  # [2, 4, 6, 8]

---

### 🔹 Реалізація через for

nums = [1, 2, 3, 4]  
result = []

for x in nums:
    result.append(x * 2)

print(result)

👉 map = цикл + застосування функції

---

## 🔸 3. filter()

filter залишає тільки ті елементи, для яких функція повертає True.

Приклад:
nums = [1, 2, 3, 4, 5]  
result = list(filter(lambda x: x % 2 == 0, nums))  
print(result)  # [2, 4]

---

### 🔹 Реалізація через for

nums = [1, 2, 3, 4, 5]  
result = []

for x in nums:
    if x % 2 == 0:
        result.append(x)

print(result)

👉 filter = цикл + if

---

## 🔸 4. reduce()

reduce згортає список в одне значення.

Імпорт:
from functools import reduce

Приклад:
nums = [1, 2, 3, 4]  
result = reduce(lambda a, b: a + b, nums)  
print(result)  # 10

---

### 🔹 Реалізація через for

nums = [1, 2, 3, 4]  

result = nums[0]

for i in range(1, len(nums)):
    result = result + nums[i]

print(result)

👉 reduce = накопичення результату

---

## 🔸 5. Як це працює під капотом

### map:
def custom_map(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

---

### filter:
def custom_filter(func, data):
    result = []
    for item in data:
        if func(item):
            result.append(item)
    return result

---

### reduce:
def custom_reduce(func, data):
    result = data[0]
    for i in range(1, len(data)):
        result = func(result, data[i])
    return result

---

## 🔸 6. Коли використовувати

map → змінити всі елементи  
filter → відібрати елементи  
reduce → отримати одне значення  

---

## 🔸 7. Важливо

- lambda — для коротких дій
- не використовувати для складної логіки
- часто використовується разом з map/filter/reduce