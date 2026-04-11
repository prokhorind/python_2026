# 🔷 ООП у Python: Інкапсуляція та Абстракція

## 🔹 Що таке ООП?

Об’єктно-орієнтоване програмування (ООП) — це підхід, де програма будується навколо об’єктів.

Кожен об’єкт має:

* дані (властивості / поля)
* поведінку (методи)

---

## 🔹 Основні принципи ООП

1. Інкапсуляція
2. Абстракція
3. Наслідування
4. Поліморфізм

👉 У цьому занятті:
Інкапсуляція + Абстракція

---

# 🔒 Інкапсуляція

## 🔹 Ідея

Інкапсуляція — це приховування внутрішніх даних об’єкта та доступ до них тільки через методи.

👉 Забороняємо пряму зміну змінних

---

## 🔹 Приклад класу

```
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

## 🔹 Створення об’єкта

```
account = BankAccount("Denys", 1000)
```

---

## 🔹 Використання

```
account.deposit(500)
print(account.get_balance())   # 1500
```

---

## ❌ Неправильне використання

```
account.__balance = 999999   # так робити не можна
```

---

## 🔹 Чому це важливо?

* захист даних
* контроль логіки
* менше помилок

---

# 🎭 Абстракція

## 🔹 Ідея

Абстракція — це приховування складної логіки та надання простого інтерфейсу.

👉 користувач бачить "що робити", а не "як працює"

---

## 🔹 Приклад класу

```
class CoffeeMachine:
    def make_coffee(self):
        self.__heat_water()
        self.__add_coffee()
        print("Кава готова!")

    def __heat_water(self):
        print("Нагріваємо воду...")

    def __add_coffee(self):
        print("Додаємо каву...")
```

---

## 🔹 Використання

```
machine = CoffeeMachine()
machine.make_coffee()
```

---

# 🔄 Процедурний підхід

```
balance = 1000

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount

def get_balance():
    return balance

deposit(500)
print(get_balance())
```

---

## ❌ Проблеми

* глобальні змінні
* немає захисту
* складно масштабувати

---

# 🔁 Closure підхід

```
def create_account(owner, balance):

    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount

    def get_balance():
        return balance

    return deposit, get_balance


deposit, get_balance = create_account("Denys", 1000)

deposit(500)
print(get_balance())
```

---

## ✔ Плюси / Мінуси

✔ приховує дані
❌ складніше читати
❌ немає структури

---

# 🧠 Висновок

Процедурний підхід — простий, але небезпечний
Closures — вже краще, але складно
ООП — структурований і контрольований

👉 Використовуємо ООП у реальних проєктах
