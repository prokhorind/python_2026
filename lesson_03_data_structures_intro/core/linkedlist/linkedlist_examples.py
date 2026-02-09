# Linked List examples in Python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

# ===== Examples =====

ll = LinkedList()

# Prepend elements (O(1))
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
ll.display()

# Append elements (O(n))
ll.append(5)
ll.append(1)
ll.display()

# Find elements
print("Find 20:", ll.find(20))
print("Find 100:", ll.find(100))
