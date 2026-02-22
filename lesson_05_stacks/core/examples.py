# Реалізація стеку за допомогою list

stack = []

# push
stack.append(10)
stack.append(20)
stack.append(30)

print("Стек після додавання:", stack)

# peek
print("Верхній елемент:", stack[-1])

# pop
removed = stack.pop()
print("Видалений елемент:", removed)

print("Стек зараз:", stack)

# перевірка на порожність
if not stack:
    print("Стек порожній")
else:
    print("Стек не порожній")