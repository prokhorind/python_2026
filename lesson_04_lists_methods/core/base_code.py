# 🧩 Базовий код для учнів

## Частина 1 --- list

scores = [75, 90, 82, 60, 95]


## Частина 2 --- Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

players = LinkedList()
players.append("Alice")
players.append("Bob")

players.print_list()

# Додайте код для виконання завдання
