# Queue на базі dynamic array (Python list)

queue = []

# enqueue
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print("Queue:", queue)

# dequeue
first = queue.pop(0)

print("Removed:", first)
print("Queue:", queue)

# peek
print("Next:", queue[0])

# перевірка
if not queue:
    print("Queue empty")