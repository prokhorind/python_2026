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

    file.write("кава,50\n") #Запис у файл:
    file.close()

---

    file = open("expenses.txt", "r") #Читання файлу:
    lines = file.readlines()
    file.close()

---

## 🔁 2. Цикли :

    while True: #Нескінченний цикл
        print("Меню")

---

    for line in lines: #Перебір списку:
        print(line)

---

## 📋 3. Списки

    expenses = []
    expenses.append("кава,50") #Додавання:

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

    name, amount = line.split(",") #Розділення:
    line = line.strip() #Видалення переносу:

---

## 🖼️ 7. Основи Tkinter

    from tkinter import * #Імпорт:

    root = Tk() 
    root.title("Трекер витрат")
    root.geometry("300x400") 
    #Створення вікна:

---

    entry = Entry(root) #Поле вводу:
    entry.pack()

    text = entry.get() #Отримання тексту:

---

    def add_expense(): #Кнопка:
        print("Додано")

    btn = Button(root, text="Додати", command=add_expense)
    btn.pack()

---

    listbox = Listbox(root) #Список (Listbox):
    listbox.pack()

    listbox.insert(END, "кава - 50 грн") #Додати елемент:


    listbox.delete(0, END) #Очистити список:

---

    root.mainloop() #Запуск програми: