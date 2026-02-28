# Створення словника
student = {
    "name": "Anna",
    "age": 16,
    "grade": 10
}

# Доступ до значення
print("Ім'я:", student["name"])

# Додавання нового елемента
student["city"] = "Kyiv"

# Зміна значення
student["age"] = 17

# Перевірка наявності ключа
if "grade" in student:
    print("Клас:", student["grade"])

# Метод get (безпечний доступ)
print("Телефон:", student.get("phone", "Немає даних"))

# Видалення елемента
student.pop("city")

# Перебір словника
for key, value in student.items():
    print(key, "->", value)

# Отримання списку ключів
print("Ключі:", student.keys())

# Отримання списку значень
print("Значення:", student.values())

# Довжина словника
print("Кількість елементів:", len(student))