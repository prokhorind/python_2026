class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


q = Queue()

q.enqueue("Task1")
q.enqueue("Task2")
q.enqueue("Task3")

print(q.dequeue())
print(q.peek())
print(q.size())