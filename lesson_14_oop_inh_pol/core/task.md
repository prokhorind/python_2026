# 🎯 Практичне завдання: Система повідомлень

## 🔹 Умова

Ти створюєш систему відправки повідомлень.

Є базовий клас Notification:

* message
* send()

Створи класи-нащадки:

* EmailNotification
* SMSNotification
* PushNotification

---

## 🔹 Завдання

1. Перевизнач метод send() у кожному класі
2. Реалізуй різну поведінку:

Email → Sending EMAIL: <message>
SMS → Sending SMS: <message>
Push → Sending PUSH: <message>

3. Використай self.message

---

## 🔹 Важливо

❌ Не використовувати if
✅ Використовувати поліморфізм

---

## 🔹 Очікуваний результат

Sending EMAIL: Hello via Email
Sending SMS: Hello via SMS
Sending PUSH: Hello via Push

---

## 🔹 Додаткове завдання

Додай клас:

* TelegramNotification

👉 Не змінюючи основний цикл

---

## 🔹 Підказка

for n in notifications:
n.send()
