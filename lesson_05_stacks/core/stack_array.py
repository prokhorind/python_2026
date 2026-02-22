class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Стек порожній!")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Тестування
s = Stack()

s.push(5)
s.push(15)
s.push(25)

print("Верхній:", s.peek())
print("Розмір:", s.size())

print("Видалено:", s.pop())
print("Розмір після pop:", s.size())