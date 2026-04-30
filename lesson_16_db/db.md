# 🧠 Тема: Підключення до PostgreSQL з Python (psycopg2)

## 🎯 Мета

Навчитися:

* підключатися до PostgreSQL з Python
* виконувати SQL-запити
* створювати таблиці (CREATE TABLE)
* додавати дані (INSERT INTO)

---

## 📚 Теорія: psycopg2

psycopg2 — бібліотека для роботи з PostgreSQL у Python.

### Встановлення

`pip install psycopg2-binary`

### Підключення

`connection = psycopg2.connect(host="localhost", database="your_database", user="your_user", password="your_password", sslmode="require")`

### Cursor

`cursor = connection.cursor()`

### Виконання запитів

`cursor.execute("SQL QUERY")`

### Збереження змін

`connection.commit()`

### Закриття

`cursor.close()`
`connection.close()`

---

## 📌 Умова завдання

1. Підключіться до PostgreSQL
2. Створіть таблицю teachers:

   * id (PRIMARY KEY)
   * name (VARCHAR)
   * subject (VARCHAR)
3. Додайте записи:

   * Іван — Математика
   * Марія — Інформатика
   * Олег — Фізика
4. Виведіть: Дані успішно додані!

---

## ⚙️ Вимоги

* psycopg2
* cursor
* commit()
* закриття з'єднання

---

