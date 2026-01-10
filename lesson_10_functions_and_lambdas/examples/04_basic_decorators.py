# Приклад 4: Прості приклади з лямбда

print("=== Лямбда для простих обчислень ===")

# Список чисел для роботи
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Числа: {numbers}")

# Знайти всі парні числа та їх квадрати
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
even_squares = list(map(lambda x: x ** 2, even_numbers))

print(f"Парні числа: {even_numbers}")
print(f"Квадрати парних: {even_squares}")

print("\n=== Робота з іменами ===")

names = ["іван", "марія", "петро", "анна", "олег"]
print(f"Імена: {names}")

# Перетворити в заголовний регістр
title_names = list(map(lambda name: name.title(), names))
print(f"Заголовний регістр: {title_names}")

# Знайти довгі імена (більше 4 символів)
long_names = list(filter(lambda name: len(name) > 4, names))
print(f"Довгі імена: {long_names}")

# Створити привітання для довгих імен
greetings = list(map(lambda name: f"Привіт, {name.title()}!", long_names))
print(f"Привітання: {greetings}")

print("\n=== Робота з оцінками ===")

grades = [85, 92, 78, 96, 88, 73, 91, 67, 94, 82]
print(f"Оцінки: {grades}")

# Знайти відмінні оцінки (90+)
excellent = list(filter(lambda grade: grade >= 90, grades))
print(f"Відмінні оцінки: {excellent}")

# Додати бонус +5 до всіх оцінок
bonus_grades = list(map(lambda grade: min(100, grade + 5), grades))
print(f"З бонусом +5: {bonus_grades}")

# Категорії оцінок
categories = list(map(
    lambda grade: "Відмінно" if grade >= 90 else "Добре" if grade >= 80 else "Задовільно",
    grades
))
print(f"Категорії: {categories}")

print("\n=== Комбінування операцій ===")

# Знайти квадрати непарних чисел менше 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Числа: {numbers}")

# Спочатку фільтруємо, потім перетворюємо
odd_small = list(filter(lambda x: x % 2 == 1 and x < 8, numbers))
odd_small_squares = list(map(lambda x: x ** 2, odd_small))

print(f"Непарні < 8: {odd_small}")
print(f"Їх квадрати: {odd_small_squares}")

print("\n=== Сортування з лямбда ===")

# Список слів
words = ["кіт", "собака", "миша", "слон", "жираф", "їжак"]
print(f"Слова: {words}")

# Сортування за довжиною
by_length = sorted(words, key=lambda word: len(word))
print(f"За довжиною: {by_length}")

# Сортування за останньою літерою
by_last_letter = sorted(words, key=lambda word: word[-1])
print(f"За останньою літерою: {by_last_letter}")

print("\n=== Практичний приклад: список покупок ===")

# Товари з цінами
items = [("хліб", 25), ("молоко", 30), ("яйця", 45), ("масло", 60), ("сир", 80)]
print("Товари та ціни:")
for item, price in items:
    print(f"  {item}: {price} грн")

# Знайти дешеві товари (до 40 грн)
cheap_items = list(filter(lambda item: item[1] <= 40, items))
print(f"\nДешеві товари: {[item[0] for item in cheap_items]}")

# Додати знижку 10% до всіх товарів
discounted = list(map(lambda item: (item[0], round(item[1] * 0.9)), items))
print("\nЗі знижкою 10%:")
for item, price in discounted:
    print(f"  {item}: {price} грн")

# Сортування за ціною
by_price = sorted(items, key=lambda item: item[1])
print(f"\nЗа ціною: {[f'{item[0]} ({item[1]} грн)' for item in by_price]}")