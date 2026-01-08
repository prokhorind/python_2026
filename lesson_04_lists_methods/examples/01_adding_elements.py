# Приклад 1: Додавання елементів до списку

print("=== ДОДАВАННЯ ЕЛЕМЕНТІВ ===")

# Початковий список покупок
shopping_list = ["хліб", "молоко"]
print(f"Початковий список: {shopping_list}")

# append() - додаємо один елемент в кінець
shopping_list.append("яйця")
print(f"Після append('яйця'): {shopping_list}")

shopping_list.append("масло")
print(f"Після append('масло'): {shopping_list}")

# insert() - вставляємо елемент на певну позицію
shopping_list.insert(1, "кефір")  # На позицію 1 (після хліба)
print(f"Після insert(1, 'кефір'): {shopping_list}")

shopping_list.insert(0, "вода")  # На початок списку
print(f"Після insert(0, 'вода'): {shopping_list}")

# extend() - додаємо кілька елементів з іншого списку
fruits = ["яблука", "банани", "апельсини"]
shopping_list.extend(fruits)
print(f"Після extend(fruits): {shopping_list}")

# Альтернатива - оператор +=
vegetables = ["морква", "картопля"]
shopping_list += vegetables
print(f"Після += vegetables: {shopping_list}")

# Оператор + створює новий список (не змінює оригінальний)
dairy = ["сир", "йогурт"]
full_list = shopping_list + dairy
print(f"Новий список (shopping_list + dairy): {full_list}")
print(f"Оригінальний список не змінився: {shopping_list}")

# Додавання елементів у циклі
print(f"\n=== ДОДАВАННЯ У ЦИКЛІ ===")
numbers = []
print("Додаємо квадрати чисел від 1 до 5:")

for i in range(1, 6):
    square = i ** 2
    numbers.append(square)
    print(f"Додано {i}² = {square}, список: {numbers}")

# Додавання з перевіркою
print(f"\n=== ДОДАВАННЯ З ПЕРЕВІРКОЮ ===")
unique_colors = ["червоний", "синій"]
new_colors = ["зелений", "червоний", "жовтий", "синій", "фіолетовий"]

print(f"Початкові кольори: {unique_colors}")
print(f"Кольори для додавання: {new_colors}")

for color in new_colors:
    if color not in unique_colors:
        unique_colors.append(color)
        print(f"Додано новий колір: {color}")
    else:
        print(f"Колір {color} вже є в списку")

print(f"Фінальний список унікальних кольорів: {unique_colors}")

# Статистика
print(f"\n=== СТАТИСТИКА ===")
print(f"Всього товарів у списку покупок: {len(shopping_list)}")
print(f"Всього унікальних кольорів: {len(unique_colors)}")
print(f"Всього квадратів: {len(numbers)}")
print(f"Сума квадратів: {sum(numbers)}")