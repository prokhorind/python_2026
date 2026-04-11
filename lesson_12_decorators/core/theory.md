# 🧠 Декоратори в Python

## 📌 Що таке декоратор?

Декоратор — це функція, яка "обгортає" іншу функцію і змінює або розширює її поведінку **без зміни її коду**.

👉 Простими словами:
декоратор = функція, яка додає нову поведінку іншій функції

# 🔧 Простий декоратор без використання @

## 📌 Ідея

Функція обгортає іншу функцію і додає логіку до та після її виконання.

---

## 🧪 Приклад

```python
def decorator(func):
    def wrapper():
        print("Початок роботи")

        func()

        print("Кінець роботи")
    return wrapper


def say_hello():
    print("Hello!")


# обгортаємо функцію вручну
say_hello = decorator(say_hello)

say_hello()
```

---

## 📤 Результат

```
Початок роботи
Hello!
Кінець роботи
```

---

## 🔍 Що відбулося

```python
say_hello = decorator(say_hello)
```

* ми передали функцію `say_hello` в іншу функцію
* отримали нову функцію (`wrapper`)
* замінили стару функцію новою

---

## 🧠 Висновок

* декоратор — це просто функція, яка повертає іншу функцію
* `@decorator` — це лише скорочений запис
* головна ідея: **обгортка функції через іншу функцію**


---

## ⚙️ Синтаксис

```python
def my_decorator(func):
    def wrapper():
        print("До виклику функції")
        func()
        print("Після виклику функції")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 🔍 Як це працює

```python
@my_decorator
def say_hello():
    pass
```

еквівалентно:

```python
def say_hello():
    pass

say_hello = my_decorator(say_hello)
```

---

## 🧱 Важливий момент

Декоратор:

* приймає функцію
* повертає нову функцію (wrapper)

---

## 🧩 GOF Pattern: Decorator

### 📌 Ідея патерну

Динамічно додаємо нову поведінку об'єкту, не змінюючи його код.

---

## 🏗️ Приклад (GOF Decorator на Python)

```python
class Coffee:
    def cost(self):
        return 50


class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20


class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10


coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())  # 80
```

---

## 🔁 Порівняння

| Python Decorator | GOF Decorator   |
| ---------------- | --------------- |
| функція          | клас            |
| обгортає функцію | обгортає об'єкт |
| простіший        | гнучкіший       |

---

## 🧠 Висновок

Декоратори дозволяють:

* не змінювати існуючий код
* додавати логування, перевірки, кешування
* писати чистіший код
