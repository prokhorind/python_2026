# Приклад 1: Сума та середнє арифметичне

# Введення 5 оцінок від користувача
print("Введи 5 своїх оцінок:")

total_sum = 0
grade_count = 5

for i in range(grade_count):
    grade = int(input(f"Оцінка {i+1}: "))
    total_sum += grade

print(f"\nСума оцінок: {total_sum}")

# Обчислення середнього
average = total_sum / grade_count
print(f"Середня оцінка: {round(average, 2)}")

# Визначення рівня успішності
if average >= 9:
    level = "Відмінник"
elif average >= 7:
    level = "Хорошист"
else:
    level = "Потрібно підтягнути"

print(f"Рівень: {level}")

# Додаткова статистика
print(f"До відмінника не вистачає: {round(9 - average, 2)} балів" if average < 9 else "Ти вже відмінник!")