import psycopg2


# ---------------- MODEL ----------------

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"{self.name} — {self.subject}"

    @staticmethod
    def from_row(row):
        name, subject = row
        return Teacher(name, subject)


# ---------------- DB ----------------

def connect():
    return psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_user",
        password="your_password"
    )


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS teachers (id SERIAL PRIMARY KEY, name VARCHAR(50), subject VARCHAR(50))"
    )

    conn.commit()
    cur.close()
    conn.close()


def load_teachers():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT name, subject FROM teachers")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return list(map(Teacher.from_row, rows))


def save_teacher(teacher):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO teachers (name, subject) VALUES (%s, %s)",
        (teacher.name, teacher.subject)
    )

    conn.commit()
    cur.close()
    conn.close()


def clear_teachers():
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM teachers")

    conn.commit()
    cur.close()
    conn.close()

    print("🗑 Таблицю очищено!")


# ---------------- ДІЇ ----------------

def add_teacher():
    name = input("Ім'я: ")
    subject = input("Предмет: ")

    teacher = Teacher(name, subject)
    save_teacher(teacher)

    print("✅ Додано в БД!")


def show_teachers(data=None):
    if data is None:
        data = load_teachers()

    if not data:
        print("❌ Таблиця порожня")
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
    letter = input("Починається з букви: ")
    teachers = load_teachers()

    filtered = list(filter(lambda t: t.name.lower().startswith(letter.lower()), teachers))

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


def exit_program():
    print("👋 До побачення!")
    exit()


# ---------------- МЕНЮ ----------------

def menu():
    create_table()

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
        print("\n===== DATABASE STORAGE =====")
        print("1. Додати вчителя")
        print("2. Показати всіх")
        print("3. Фільтр по предмету")
        print("4. Фільтр по першій букві")
        print("5. Показати тільки імена (map)")
        print("6. Uppercase (map)")
        print("7. Очистити таблицю")
        print("8. Вийти")

        choice = input(">> ")

        action = actions.get(choice)

        if action:
            action()
        else:
            print("❌ Невірний вибір")


menu()