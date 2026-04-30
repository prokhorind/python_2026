import psycopg2

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

def add_teacher():
    name = input("Ім'я: ")
    subject = input("Предмет: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO teachers (name, subject) VALUES (%s, %s)",
        (name, subject)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Додано в БД!")

def show_teachers():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT name, subject FROM teachers")
    rows = cur.fetchall()

    if not rows:
        print("❌ Таблиця порожня")
    else:
        for i, (name, subject) in enumerate(rows, start=1):
            print(f"{i}. {name} — {subject}")

    cur.close()
    conn.close()

def menu():
    #create_table()

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