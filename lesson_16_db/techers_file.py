FILE_NAME = "teachers.txt"


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"{self.name} — {self.subject}"

    def to_line(self):
        return f"{self.name},{self.subject}\n"

    @staticmethod
    def from_line(line):
        name, subject = line.strip().split(",")
        return Teacher(name, subject)


# ---------------- STORAGE ----------------

def load_teachers():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return list(map(Teacher.from_line, f.readlines()))
    except FileNotFoundError:
        return []


def save_teacher(teacher):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(teacher.to_line())


def overwrite_teachers(teachers):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.writelines(map(lambda t: t.to_line(), teachers))


# ---------------- ДІЇ ----------------

def add_teacher():
    name = input("Ім'я: ")
    subject = input("Предмет: ")

    teacher = Teacher(name, subject)
    save_teacher(teacher)

    print("✅ Додано у файл!")


def show_teachers(data=None):
    if data is None:
        data = load_teachers()

    if not data:
        print("❌ Список порожній")
        return

    for i, t in enumerate(data, start=1):
        print(f"{i}. {t}")


def filter_by_subject():
    subject = input("Введіть предмет: ")
    teachers = load_teachers()

    filtered = list(filter(lambda t: t.subject.lower() == subject.lower(), teachers))

    print(f"\n🔍 Результат ({subject}):")
    show_teachers(filtered)


def filter_by_name():
    letter = input("Починається з букви: ").lower()
    teachers = load_teachers()

    filtered = list(filter(lambda t: t.name.lower().startswith(letter), teachers))

    print(f"\n🔍 Імена на '{letter}':")
    show_teachers(filtered)


def map_to_names():
    teachers = load_teachers()
    names = list(map(lambda t: t.name, teachers))

    print("\n🧾 Імена:")
    for n in names:
        print(n)


def map_uppercase():
    teachers = load_teachers()

    upper = list(map(lambda t: Teacher(t.name.upper(), t.subject.upper()), teachers))

    print("\n🔠 Uppercase:")
    show_teachers(upper)


def clear_teachers():
    overwrite_teachers([])
    print("🗑 Файл очищено!")


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
        print("\n===== FILE STORAGE =====")
        print("1. Додати вчителя")
        print("2. Показати всіх")
        print("3. Фільтр по предмету")
        print("4. Фільтр по першій букві")
        print("5. Показати тільки імена (map)")
        print("6. Uppercase (map)")
        print("7. Очистити файл")
        print("8. Вийти")

        choice = input(">> ")

        action = actions.get(choice)

        if action:
            action()
        else:
            print("❌ Невірний вибір")


menu()