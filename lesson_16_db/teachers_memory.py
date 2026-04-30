class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"{self.name} — {self.subject}"


teachers = []


# ---------------- ДІЇ ----------------

def add_teacher():
    name = input("Ім'я: ")
    subject = input("Предмет: ")

    teacher = Teacher(name, subject)
    teachers.append(teacher)

    print("✅ Додано!")


def show_teachers(data=None):
    if data is None:
        data = teachers

    if not data:
        print("❌ Список порожній")
        return

    for i, t in enumerate(data, start=1):
        print(f"{i}. {t}")


def filter_by_subject():
    subject = input("Введіть предмет: ")

    filtered = list(filter(lambda t: t.subject.lower() == subject.lower(), teachers))

    print(f"\n🔍 Результат фільтрації ({subject}):")
    show_teachers(filtered)


def filter_by_name():
    letter = input("Починається з букви: ").lower()

    filtered = list(filter(lambda t: t.name.lower().startswith(letter), teachers))

    print(f"\n🔍 Імена на '{letter}':")
    show_teachers(filtered)


def map_to_names():
    names = list(map(lambda t: t.name, teachers))

    print("\n🧾 Список імен:")
    for n in names:
        print(n)


def map_uppercase():
    upper_teachers = list(
        map(lambda t: Teacher(t.name.upper(), t.subject.upper()), teachers)
    )

    print("\n🔠 У верхньому регістрі:")
    show_teachers(upper_teachers)


def clear_teachers():
    teachers.clear()
    print("🗑 Очищено!")


def exit_program():
    print("👋 До побачення!")
    exit()


# ---------------- МЕНЮ ----------------

def menu():
    actions = {
        "1": add_teacher,
        "2": show_teachers,
        "3": filter_by_subject,
        "4": filter_by_name,
        "5": map_to_names,
        "6": map_uppercase,
        "7": clear_teachers,
        "8": exit_program
    }

    while True:
        print("\n===== МЕНЮ =====")
        print("1. Додати вчителя")
        print("2. Показати всіх")
        print("3. Фільтр по предмету")
        print("4. Фільтр по першій букві імені")
        print("5. Показати тільки імена (map)")
        print("6. Показати у ВЕРХНЬОМУ регістрі (map)")
        print("7. Очистити список")
        print("8. Вийти")

        choice = input(">> ")

        action = actions.get(choice)

        if action:
            action()
        else:
            print("❌ Невірний вибір")


menu()