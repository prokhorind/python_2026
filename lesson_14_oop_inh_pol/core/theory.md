# 🧠 ООП у Python: Спадкування та Поліморфізм

## 🔹 Що таке ООП?

Об'єктно-орієнтоване програмування (ООП) — це підхід, у якому програма будується навколо об'єктів.

Об'єкт = дані (поля) + поведінка (методи)

---

## 🔹 Основні принципи ООП

* Інкапсуляція
* Абстракція
* Спадкування
* Поліморфізм

У цьому матеріалі:
👉 Спадкування
👉 Поліморфізм

---

# 🔹 Спадкування (Inheritance)

Спадкування дозволяє створювати нові класи на основі існуючих.

## 📌 Приклад

class Animal:
def speak(self):
print("Some sound")

class Dog(Animal):
def speak(self):
print("Woof")

class Cat(Animal):
def speak(self):
print("Meow")

👉 Dog і Cat наслідують Animal

---

# 🔹 Поліморфізм (Polymorphism)

👉 Один інтерфейс — різна поведінка

## 📌 Приклад

animals = [Dog(), Cat()]

for animal in animals:
animal.speak()

---

# 🔹 Як це працює

Python визначає метод під час виконання (dynamic dispatch)

---

# 🔹 Процедурний підхід

def dog_speak():
print("Woof")

def cat_speak():
print("Meow")

animals = ["dog", "cat"]

for animal in animals:
if animal == "dog":
dog_speak()
elif animal == "cat":
cat_speak()

❌ Мінуси:

* багато if
* складно масштабувати
---

# 🔹 Висновок

Спадкування + Поліморфізм = гнучкий код
