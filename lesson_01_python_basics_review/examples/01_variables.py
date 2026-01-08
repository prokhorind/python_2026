# Приклад 1: Робота зі змінними (легкий)

# Створення змінних різних типів
student_name = "Іван"
student_age = 15
student_grade = 9.5
is_present = True

print(f"Студент: {student_name}")
print(f"Вік: {student_age}")
print(f"Оцінка: {student_grade}")
print(f"Присутній: {is_present}")

# Зміна значень змінних
student_age += 1
student_grade = round(student_grade + 0.3, 1)

print(f"\nПісля оновлення:")
print(f"Вік: {student_age}")
print(f"Оцінка: {student_grade}")