# Реалізація стеку за допомогою list

numbers = []

# push
numbers.append(10)
numbers.append(20)
numbers.append(30)

print("Стек після додавання:", numbers)

# peek
print("Верхній елемент:", numbers[-1])

# pop
removed = numbers.pop(0)
print("Видалений елемент:", removed)

print("Стек зараз:", numbers)

# перевірка на порожність
if not numbers:
    print("Стек порожній")
else:
    print("Стек не порожній")