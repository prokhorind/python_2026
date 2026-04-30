FILE_NAME = "teachers.txt"

def add_teacher():
    name = input("Ім'я: ")
    subject = input("Предмет: ")

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{name},{subject}\n")

    print("✅ Додано у файл!")

def show_teachers():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("❌ Файл не знайдено")
        return

    if not lines:
        print("❌ Файл порожній")
        return

    for i, line in enumerate(lines, start=1):
        name, subject = line.strip().split(",")
        print(f"{i}. {name} — {subject}")

def menu():
    while True:
        print("\n1. Додати вчителя")
        print("2. Показати всіх")
        print("3. Вийти")

        choice = input(">> ")

        if choice == "1":
            add_teacher()
        elif choice == "2":
            show_teachers()
        elif choice == "3":
            break
        else:
            print("❌ Невірний вибір")

menu()