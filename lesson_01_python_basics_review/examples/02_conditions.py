# Приклад 2: Умовні конструкції (середній)

def check_grade(grade):
    """Перевіряє оцінку та повертає результат"""
    if grade >= 10:
        return "Відмінно! 🌟"
    elif grade >= 7:
        return "Добре! 👍"
    elif grade >= 4:
        return "Задовільно 📚"
    else:
        return "Потрібно підтягнути 📖"

# Тестування різних оцінок
grades = [12, 8.5, 5, 2, 10]

for grade in grades:
    result = check_grade(grade)
    print(f"Оцінка {grade}: {result}")

# Складніша умова
def can_go_to_party(age, has_permission, finished_homework):
    """Перевіряє чи може йти на вечірку"""
    if age >= 16 and has_permission and finished_homework:
        return "Можеш йти! 🎉"
    elif not finished_homework:
        return "Спочатку зроби домашнє завдання! 📝"
    elif not has_permission:
        return "Потрібен дозвіл батьків! 👨‍👩‍👧‍👦"
    else:
        return "Ще замалий для вечірок! 🚫"

print(f"\nПеревірка дозволу на вечірку:")
print(can_go_to_party(17, True, True))
print(can_go_to_party(15, True, False))