"""
Приклад: як переписати if/elif на dictionary.

Ідея:
Замість великої конструкції if/elif
можна використати словник,
де ключ — команда,
а значення — функція.
"""


# ==============================
# ВАРІАНТ 1 — через if / elif
# ==============================

def menu_if():
    print("\n=== Меню (if/elif версія) ===")
    print("1 - Привітання")
    print("2 - Додати числа")
    print("3 - Помножити числа")
    print("4 - Вийти")

    while True:
        choice = input("\nОберіть дію: ")

        if choice == "1":
            print("Привіт!")

        elif choice == "2":
            a = int(input("Введіть перше число: "))
            b = int(input("Введіть друге число: "))
            print("Сума:", a + b)

        elif choice == "3":
            a = int(input("Введіть перше число: "))
            b = int(input("Введіть друге число: "))
            print("Добуток:", a * b)

        elif choice == "4":
            print("Вихід...")
            break

        else:
            print("Невідома команда")


# =====================================
# ВАРІАНТ 2 — через dictionary (краще)
# =====================================

def greet():
    print("Привіт!")


def add():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print("Сума:", a + b)


def multiply():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print("Добуток:", a * b)


def exit_program():
    print("Вихід...")
    return False  # сигнал для завершення циклу


def menu_dict():
    print("\n=== Меню (dictionary версія) ===")
    print("1 - Привітання")
    print("2 - Додати числа")
    print("3 - Помножити числа")
    print("4 - Вийти")

    actions = {
        "1": greet,
        "2": add,
        "3": multiply,
        "4": exit_program
    }

    while True:
        choice = input("\nОберіть дію: ")

        action = actions.get(choice)

        if action:
            result = action()

            # якщо функція повернула False — виходимо
            if result is False:
                break
        else:
            print("Невідома команда")


# ============================
# Запуск обох варіантів
# ============================

print("1 - Запустити версію з if/elif")
print("2 - Запустити версію з dictionary")

mode = input("Оберіть режим: ")

if mode == "1":
    menu_if()
elif mode == "2":
    menu_dict()
else:
    print("Невірний вибір")