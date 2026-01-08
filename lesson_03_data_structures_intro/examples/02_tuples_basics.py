# Приклад 2: Основи роботи з кортежами

# Створення кортежів для різних даних
student_info = ("Максим", "Іваненко", 16, "10-А")
coordinates = (50.4501, 30.5234)  # Київ
rgb_red = (255, 0, 0)
date_birth = (15, 8, 2007)  # день, місяць, рік

print("=== РОБОТА З КОРТЕЖАМИ ===")

# Розпакування кортежу студента
first_name, last_name, age, class_name = student_info
print(f"Студент: {first_name} {last_name}")
print(f"Вік: {age} років, клас: {class_name}")

# Робота з координатами
latitude, longitude = coordinates
print(f"\nКоординати Києва:")
print(f"Широта: {latitude}")
print(f"Довгота: {longitude}")

# Робота з кольором
red, green, blue = rgb_red
print(f"\nКолір червоний в RGB:")
print(f"R: {red}, G: {green}, B: {blue}")
print(f"Hex: #{red:02x}{green:02x}{blue:02x}")

# Робота з датою
day, month, year = date_birth
months = ("", "січень", "лютий", "березень", "квітень", "травень", "червень",
          "липень", "серпень", "вересень", "жовтень", "листопад", "грудень")

print(f"\nДата народження: {day} {months[month]} {year} року")

# Доступ до елементів за індексом
print(f"\nДоступ за індексом:")
print(f"Перший елемент student_info: {student_info[0]}")
print(f"Останній елемент student_info: {student_info[-1]}")

# Довжина кортежу
print(f"Кількість елементів у student_info: {len(student_info)}")

# Перевірка наявності елемента
if 16 in student_info:
    print("Вік 16 знайдено в інформації про студента")

# Кортежі незмінні - це викличе помилку:
# student_info[0] = "Андрій"  # TypeError!

# Але можна створити новий кортеж
updated_info = ("Андрій", last_name, age + 1, class_name)
print(f"\nОновлена інформація: {updated_info}")

# Об'єднання кортежів
full_info = student_info + coordinates
print(f"Повна інформація: {full_info}")