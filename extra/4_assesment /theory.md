# 📘 Теорія для проєкту "Трекер витрат"

---

## 📂 1. Робота з файлами

Відкрити файл:
    file = open("expenses.txt", "a")

Режими:
- r — читання  
- w — перезапис  
- a — додавання  

---

Запис у файл:
    file.write("кава,50\n")
    file.close()

---

Читання файлу:
    file = open("expenses.txt", "r")
    lines = file.readlines()
    file.close()

---

## 🔁 2. Цикли

Нескінченний цикл:
    while True:
        print("Меню")

---

Перебір списку:
    for line in lines:
        print(line)

---

## 📋 3. Списки

    expenses = []

Додавання:
    expenses.append("кава,50")

---

## 🔀 4. Умови

    if choice == "1":
        print("Додавання")
    elif choice == "2":
        print("Показ")

---

## 🔢 5. Перетворення типів

    num = int("50")

---

## ✂️ 6. Робота з рядками

Розділення:
    name, amount = line.split(",")

Видалення переносу:
    line = line.strip()

---

## 🖼️ 7. Основи Tkinter

Імпорт:
    from tkinter import *

Створення вікна:
    root = Tk()
    root.title("Трекер витрат")
    root.geometry("300x400")

---

Поле вводу:
    entry = Entry(root)
    entry.pack()

Отримання тексту:
    text = entry.get()

---

Кнопка:
    def add_expense():
        print("Додано")

    btn = Button(root, text="Додати", command=add_expense)
    btn.pack()

---

Список (Listbox):
    listbox = Listbox(root)
    listbox.pack()

Додати елемент:
    listbox.insert(END, "кава - 50 грн")

Очистити список:
    listbox.delete(0, END)

---

Запуск програми:
    root.mainloop()