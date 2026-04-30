teachers = []

def add_teacher():
    name = input("Ім'я: ")
    subject = input("Предмет: ")
    teachers.append({"name": name, "subject": subject})
    print("✅ Додано!")

def show_teachers():
    if not teachers:
        print("❌ Список порожній")
        return

    for i, t in enumerate(teachers, start=1):
        print(f"{i}. {t['name']} — {t['subject']}")

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