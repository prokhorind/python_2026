![img.png](img.png)# 💻 Приклади

## Приклад 1: Робота зі списком

numbers = \[10, 20, 30, 40\]

print(numbers\[2\]) \# швидкий доступ

numbers.append(50) numbers.remove(20) numbers.sort()

print(numbers)

------------------------------------------------------------------------

## Приклад 2: Простий Linked List

class Node: def **init**(self, value): self.value = value self.next =
None

class LinkedList: def **init**(self): self.head = None

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
