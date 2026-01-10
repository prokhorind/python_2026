# Приклад 4: Практичні приклади з map, filter, sorted, zip

print("=== Обробка списку студентів ===")

# Прості дані про студентів
names = ["Іван", "Марія", "Петро", "Анна", "Олег"]
grades = [85, 92, 78, 96, 81]

print(f"Імена: {names}")
print(f"Оцінки: {grades}")

# Об'єднуємо імена та оцінки
students = list(zip(names, grades))
print(f"Студенти: {students}")

# Знаходимо відмінників (оцінка >= 90)
excellent_students = list(filter(lambda student: student[1] >= 90, students))
print(f"Відмінники: {excellent_students}")

# Створюємо рейтинг (сортування за оцінкою)
ranking = sorted(students, key=lambda student: student[1], reverse=True)
print("Рейтинг студентів:")
for i, (name, grade) in enumerate(ranking, 1):
    print(f"  {i}. {name}: {grade}")

print("\n=== Робота з температурами ===")

# Температури в різних містах (Цельсій)
cities = ["Київ", "Львів", "Одеса", "Харків", "Дніпро"]
celsius_temps = [22, 18, 25, 20, 23]

print(f"Міста: {cities}")
print(f"Температура (°C): {celsius_temps}")

# Перетворюємо в Фаренгейт
fahrenheit_temps = list(map(lambda c: round(c * 9/5 + 32, 1), celsius_temps))
print(f"Температура (°F): {fahrenheit_temps}")

# Об'єднуємо міста з температурами
weather_data = list(zip(cities, celsius_temps, fahrenheit_temps))
print("Погода:")
for city, c, f in weather_data:
    print(f"  {city}: {c}°C ({f}°F)")

# Знаходимо найтепліші міста (>20°C)
warm_cities = list(filter(lambda data: data[1] > 20, weather_data))
print(f"Теплі міста: {[city[0] for city in warm_cities]}")

print("\n=== Обробка списку покупок ===")

# Товари та ціни
shopping_list = [
    ("хліб", 25),
    ("молоко", 30),
    ("яйця", 45),
    ("масло", 60),
    ("сир", 80),
    ("м'ясо", 120)
]

print("Список покупок:")
for item, price in shopping_list:
    print(f"  {item}: {price} грн")

# Знаходимо дешеві товари (до 50 грн)
cheap_items = list(filter(lambda item: item[1] <= 50, shopping_list))
print(f"\nДешеві товари: {[item[0] for item in cheap_items]}")

# Додаємо податок 20% до всіх цін
with_tax = list(map(lambda item: (item[0], round(item[1] * 1.2)), shopping_list))
print("\nЗ податком 20%:")
for item, price in with_tax:
    print(f"  {item}: {price} грн")

# Сортуємо за ціною
by_price = sorted(shopping_list, key=lambda item: item[1])
print("\nЗа ціною (від дешевих):")
for item, price in by_price:
    print(f"  {item}: {price} грн")

# Загальна вартість
total_cost = sum(map(lambda item: item[1], shopping_list))
print(f"\nЗагальна вартість: {total_cost} грн")

print("\n=== Робота зі словами ===")

# Список слів
words = ["програмування", "python", "код", "функція", "змінна", "цикл"]
print(f"Слова: {words}")

# Знаходимо довгі слова (більше 5 символів)
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"Довгі слова: {long_words}")

# Перетворюємо в верхній регістр
upper_words = list(map(lambda word: word.upper(), words))
print(f"Верхній регістр: {upper_words}")

# Сортуємо за довжиною
by_length = sorted(words, key=lambda word: len(word))
print(f"За довжиною: {by_length}")

# Створюємо нумерований список
numbered_words = list(zip(range(1, len(words) + 1), words))
print("Нумерований список:")
for num, word in numbered_words:
    print(f"  {num}. {word}")

print("\n=== Комбінований приклад ===")

# Оцінки з різних предметів
subjects = ["Математика", "Фізика", "Хімія", "Біологія", "Історія"]
scores = [88, 92, 76, 85, 90]

# Об'єднуємо предмети та оцінки
subject_scores = list(zip(subjects, scores))
print("Оцінки з предметів:")
for subject, score in subject_scores:
    print(f"  {subject}: {score}")

# Знаходимо предмети з високими оцінками (85+)
high_scores = list(filter(lambda item: item[1] >= 85, subject_scores))
print(f"\nВисокі оцінки: {[item[0] for item in high_scores]}")

# Додаємо бонус +5 до всіх оцінок
bonus_scores = list(map(lambda item: (item[0], min(100, item[1] + 5)), subject_scores))
print("\nЗ бонусом +5:")
for subject, score in bonus_scores:
    print(f"  {subject}: {score}")

# Середня оцінка
average = sum(scores) / len(scores)
print(f"\nСередня оцінка: {average:.1f}")