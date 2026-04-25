# TASK.md
## 🧠 Практичне завдання: DTO для замовлень

### 📌 Умова

Створи систему для роботи із замовленнями.

У вас є DTO клас:

* OrderDTO

Він повинен містити:

* id
* product_name
* quantity
* price

### 🔹 Завдання

1. Створіть клас `OrderDTO`
2. Створіть клас `OrderService`
3. Реалізуйте методи:

   * print_order(order)
   * calculate_total(order)

### 🔹 Очікувана логіка

* print_order → виводить інформацію
* calculate_total → quantity * price

### 🔹 Обмеження

❗ DTO НЕ повинен містити логіку

# STARTER.py

class OrderDTO:
# TODO: реалізувати DTO
pass

class OrderService:

```
def print_order(self, order):
    # TODO
    pass

def calculate_total(self, order):
    # TODO
    pass
```

# --- test ---

order = OrderDTO(1, "Laptop", 2, 500)
service = OrderService()

service.print_order(order)
print("Total:", service.calculate_total(order))
