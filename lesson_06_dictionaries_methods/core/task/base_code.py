library = {}

while True:
    print("\n1 - Додати книгу")
    print("2 - Показати всі книги")
    print("3 - Знайти книгу")
    print("4 - Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        book = input("Назва книги: ")
        # TODO: реалізувати додавання

    elif choice == "2":
        # TODO: вивести всі книги
        pass

    elif choice == "3":
        book = input("Назва книги: ")
        # TODO: вивести кількість
        pass

    elif choice == "4":
        break