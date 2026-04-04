# =========================================
# 🔹 ПРИКЛАДИ + ТИПОВІ ПОМИЛКИ
# Lambda, map, filter, reduce
# =========================================

from functools import reduce

# =========================================
# 🔸 1. БАЗОВІ ПРИКЛАДИ
# =========================================

print("=== BASIC LAMBDA ===")

square = lambda x: x * x
print(square(4))  # 16

add = lambda a, b: a + b
print(add(2, 3))  # 5


# =========================================
# 🔸 2. MAP
# =========================================

print("\n=== MAP ===")

nums = [1, 2, 3, 4]

# ✔ правильно
result = list(map(lambda x: x * 2, nums))
print(result)  # [2, 4, 6, 8]


# ❌ ПОМИЛКА 1: забули list()
result = map(lambda x: x * 2, nums)
print(result)
# <map object ...> ← учні часто не розуміють що це


# ✔ правильно
result = list(map(lambda x: x * 2, nums))


# =========================================
# 🔸 3. FILTER
# =========================================

print("\n=== FILTER ===")

nums = [1, 2, 3, 4, 5]

# ✔ правильно
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]


# ❌ ПОМИЛКА 2: повертають не True/False
wrong = list(filter(lambda x: x % 2, nums))
print(wrong)
# працює, але логіка неочевидна (1 = True, 0 = False)


# ✔ краще так
correct = list(filter(lambda x: x % 2 == 0, nums))


# =========================================
# 🔸 4. REDUCE
# =========================================

print("\n=== REDUCE ===")

nums = [1, 2, 3, 4]

# ✔ правильно
total = reduce(lambda a, b: a + b, nums)
print(total)  # 10


# ❌ ПОМИЛКА 3: забули імпорт
# reduce(...)  → NameError


# ❌ ПОМИЛКА 4: пустий список
# reduce(lambda a, b: a + b, [])  → помилка


# ✔ безпечний варіант
nums = []
if nums:
    total = reduce(lambda a, b: a + b, nums)
else:
    total = 0


# =========================================
# 🔸 5. КОМБІНАЦІЯ (pipeline)
# =========================================

print("\n=== PIPELINE ===")

nums = [10, 15, 20, 25, 30]

result = reduce(
    lambda a, b: a + b,
    map(
        lambda x: x * 2,
        filter(lambda x: x > 15, nums)
    )
)

print(result)
# filter → [20, 25, 30]
# map → [40, 50, 60]
# reduce → 150


# =========================================
# 🔸 6. ТИПОВІ ПОМИЛКИ З ЛЯМБДА
# =========================================

print("\n=== COMMON MISTAKES ===")

# ❌ ПОМИЛКА 5: складна логіка в lambda
# lambda x: if x > 5: return x  ← так не можна


# ✔ правильно
def func(x):
    if x > 5:
        return x
    return 0


# ❌ ПОМИЛКА 6: lambda без використання
lambda x: x * 2  # нічого не відбувається


# ✔ потрібно або зберегти або використати
f = lambda x: x * 2
print(f(3))


# ❌ ПОМИЛКА 7: змінюють зовнішні змінні
x = 10
f = lambda y: x + y
x = 100

print(f(5))
# результат = 105 (а не 15) ← часто дивує учнів


# =========================================
# 🔸 7. ВИСНОВОК
# =========================================

print("\n=== SUMMARY ===")
print("map → змінює кожен елемент")
print("filter → відбирає")
print("reduce → згортає в одне значення")