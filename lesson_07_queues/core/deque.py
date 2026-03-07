from collections import deque

queue = deque()

queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print(queue)

# dequeue
first = queue.popleft()

print("Removed:", first)
print(queue)

# додавання зліва
queue.appendleft("Admin")

print(queue)

# видалення справа
queue.pop()

print(queue)