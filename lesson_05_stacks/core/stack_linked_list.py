# stack_linked_list.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            print("Стек порожній!")
            return None

        removed_value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return removed_value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        current = self.top
        print("Top -> ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# 🔎 Тестування
if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    s.display()

    print("Peek:", s.peek())
    print("Pop:", s.pop())

    s.display()
    print("Size:", s.size())