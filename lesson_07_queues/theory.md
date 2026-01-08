# Урок 7: Черги

## Мета уроку
Вивчити концепцію черги як структури даних FIFO (First In, First Out) та її практичне застосування.

## Теоретичний матеріал

### 1. Що таке черга?

Черга - це структура даних, яка працює за принципом **FIFO** (First In, First Out) - "перший зайшов, перший вийшов".

```python
# Уявіть чергу в магазині:
# - Нові люди стають в кінець черги (enqueue)
# - Обслуговують людей з початку черги (dequeue)
# - Не можна "пролізти" в середину черги

from collections import deque

# Створюємо чергу
queue = deque()
print("Порожня черга:", list(queue))

# Додаємо людей в чергу (enqueue)
queue.append("Анна")
queue.append("Борис")
queue.append("Віра")
print("Черга після додавання:", list(queue))

# Обслуговуємо людей (dequeue)
first_person = queue.popleft()
print(f"Обслужили: {first_person}")
print("Черга після обслуговування:", list(queue))
```

### 2. Основні операції черги

```python
from collections import deque

class Queue:
    def __init__(self):
        """Створюємо порожню чергу"""
        self.items = deque()
    
    def enqueue(self, item):
        """Додаємо елемент в кінець черги"""
        self.items.append(item)
        print(f"До черги додано: {item}")
    
    def dequeue(self):
        """Забираємо елемент з початку черги"""
        if self.is_empty():
            return None
        item = self.items.popleft()
        print(f"З черги забрано: {item}")
        return item
    
    def front(self):
        """Дивимось на перший елемент, не забираючи його"""
        if self.is_empty():
            return None
        return self.items[0]
    
    def rear(self):
        """Дивимось на останній елемент"""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Перевіряємо, чи черга порожня"""
        return len(self.items) == 0
    
    def size(self):
        """Повертаємо розмір черги"""
        return len(self.items)
    
    def display(self):
        """Показуємо вміст черги"""
        if self.is_empty():
            print("Черга порожня")
        else:
            print(f"Черга: {list(self.items)} (← початок ... кінець →)")

# Приклад використання
customer_queue = Queue()
customer_queue.enqueue("Клієнт 1")
customer_queue.enqueue("Клієнт 2")
customer_queue.enqueue("Клієнт 3")
customer_queue.display()

print(f"Перший в черзі: {customer_queue.front()}")
print(f"Останній в черзі: {customer_queue.rear()}")

customer_queue.dequeue()
customer_queue.display()
```

### 3. Черга з використанням списку Python

```python
# Простий варіант черги на основі списку (менш ефективний)
def create_queue():
    """Створює порожню чергу"""
    return []

def enqueue(queue, item):
    """Додає елемент до черги"""
    queue.append(item)
    print(f"Додано до черги: {item}")

def dequeue(queue):
    """Забирає елемент з черги"""
    if is_empty(queue):
        print("Черга порожня!")
        return None
    item = queue.pop(0)  # Видаляємо перший елемент
    print(f"Забрано з черги: {item}")
    return item

def front(queue):
    """Дивиться на перший елемент"""
    if is_empty(queue):
        return None
    return queue[0]

def is_empty(queue):
    """Перевіряє, чи черга порожня"""
    return len(queue) == 0

def display_queue(queue):
    """Показує чергу"""
    if is_empty(queue):
        print("Черга: []")
    else:
        print(f"Черга: {queue} (← початок)")

# Демонстрація
print_queue = create_queue()
enqueue(print_queue, "Документ 1")
enqueue(print_queue, "Документ 2")
enqueue(print_queue, "Документ 3")
display_queue(print_queue)

print(f"Наступний для друку: {front(print_queue)}")
dequeue(print_queue)
display_queue(print_queue)
```

### 4. Практичні застосування черг

#### 4.1 Черга друку

```python
from collections import deque
import time

class PrintQueue:
    def __init__(self):
        self.queue = deque()
        self.printing = False
    
    def add_document(self, document):
        """Додає документ до черги друку"""
        self.queue.append(document)
        print(f"📄 Документ '{document}' додано до черги друку")
        print(f"Позиція в черзі: {len(self.queue)}")
    
    def print_next(self):
        """Друкує наступний документ"""
        if not self.queue:
            print("Черга друку порожня")
            return
        
        document = self.queue.popleft()
        print(f"🖨️  Друкуємо: {document}")
        
        # Імітація процесу друку
        for i in range(3):
            print("   Друкування..." + "." * (i + 1))
            time.sleep(0.5)
        
        print(f"✅ Документ '{document}' надруковано")
        
        if self.queue:
            print(f"Наступний в черзі: {self.queue[0]}")
        else:
            print("Черга друку порожня")
    
    def show_queue(self):
        """Показує поточну чергу"""
        if not self.queue:
            print("Черга друку порожня")
        else:
            print("Черга друку:")
            for i, doc in enumerate(self.queue, 1):
                print(f"  {i}. {doc}")

# Демонстрація черги друку
printer = PrintQueue()
printer.add_document("Реферат з історії")
printer.add_document("Домашнє завдання")
printer.add_document("Презентація")

printer.show_queue()
printer.print_next()
printer.show_queue()
```

#### 4.2 Обслуговування клієнтів

```python
from collections import deque
from datetime import datetime

class CustomerService:
    def __init__(self):
        self.queue = deque()
        self.served_count = 0
        self.current_number = 1
    
    def take_number(self, customer_name):
        """Клієнт бере номерок"""
        ticket = {
            'number': self.current_number,
            'name': customer_name,
            'time': datetime.now().strftime("%H:%M:%S")
        }
        
        self.queue.append(ticket)
        print(f"🎫 {customer_name}, ваш номер: {self.current_number}")
        print(f"   Час: {ticket['time']}")
        print(f"   Попереду в черзі: {len(self.queue) - 1} людей")
        
        self.current_number += 1
        return ticket['number']
    
    def serve_next(self):
        """Обслуговуємо наступного клієнта"""
        if not self.queue:
            print("Черга порожня")
            return
        
        customer = self.queue.popleft()
        self.served_count += 1
        
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"🔔 Номер {customer['number']} ({customer['name']}) - підходьте до каси!")
        print(f"   Час очікування: {customer['time']} → {current_time}")
        
        if self.queue:
            next_customer = self.queue[0]
            print(f"   Наступний: номер {next_customer['number']} ({next_customer['name']})")
    
    def show_queue(self):
        """Показує поточну чергу"""
        if not self.queue:
            print("Черга порожня")
        else:
            print(f"Черга обслуговування ({len(self.queue)} людей):")
            for ticket in self.queue:
                print(f"  №{ticket['number']} - {ticket['name']} (з {ticket['time']})")
    
    def get_statistics(self):
        """Показує статистику"""
        print(f"📊 Статистика:")
        print(f"   Обслужено: {self.served_count}")
        print(f"   В черзі: {len(self.queue)}")
        print(f"   Наступний номер: {self.current_number}")

# Демонстрація обслуговування
service = CustomerService()
service.take_number("Анна Петренко")
service.take_number("Борис Іваненко")
service.take_number("Віра Сидоренко")

service.show_queue()
service.serve_next()
service.show_queue()
service.get_statistics()
```

#### 4.3 Обхід дерева в ширину (BFS)

```python
from collections import deque

def bfs_traversal(graph, start):
    """Обхід графа в ширину за допомогою черги"""
    visited = set()
    queue = deque([start])
    result = []
    
    print(f"Починаємо обхід з вершини: {start}")
    
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            print(f"Відвідуємо: {vertex}")
            
            # Додаємо сусідів до черги
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    print(f"  Додаємо до черги: {neighbor}")
            
            print(f"  Черга зараз: {list(queue)}")
    
    return result

# Приклад графа (соціальна мережа)
social_network = {
    'Анна': ['Борис', 'Віра'],
    'Борис': ['Анна', 'Григорій', 'Дарина'],
    'Віра': ['Анна', 'Євген'],
    'Григорій': ['Борис'],
    'Дарина': ['Борис', 'Євген'],
    'Євген': ['Віра', 'Дарина']
}

print("Граф соціальної мережі:")
for person, friends in social_network.items():
    print(f"{person}: {friends}")

print("\nОбхід в ширину:")
path = bfs_traversal(social_network, 'Анна')
print(f"\nПорядок відвідування: {' → '.join(path)}")
```

### 5. Кільцева черга (Circular Queue)

```python
class CircularQueue:
    def __init__(self, max_size):
        """Створює кільцеву чергу фіксованого розміру"""
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def is_empty(self):
        """Перевіряє, чи черга порожня"""
        return self.count == 0
    
    def is_full(self):
        """Перевіряє, чи черга повна"""
        return self.count == self.max_size
    
    def enqueue(self, item):
        """Додає елемент до черги"""
        if self.is_full():
            print(f"Черга повна! Не можу додати {item}")
            return False
        
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.count += 1
        print(f"Додано: {item}")
        return True
    
    def dequeue(self):
        """Забирає елемент з черги"""
        if self.is_empty():
            print("Черга порожня!")
            return None
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        print(f"Забрано: {item}")
        return item
    
    def peek(self):
        """Дивиться на перший елемент"""
        if self.is_empty():
            return None
        return self.queue[self.front]
    
    def display(self):
        """Показує чергу"""
        if self.is_empty():
            print("Черга порожня")
        else:
            items = []
            index = self.front
            for _ in range(self.count):
                items.append(self.queue[index])
                index = (index + 1) % self.max_size
            
            print(f"Черга: {items}")
            print(f"Розмір: {self.count}/{self.max_size}")

# Демонстрація кільцевої черги
print("=== КІЛЬЦЕВА ЧЕРГА ===")
circular_q = CircularQueue(3)

# Заповнюємо чергу
circular_q.enqueue("A")
circular_q.enqueue("B")
circular_q.enqueue("C")
circular_q.display()

# Спроба додати до повної черги
circular_q.enqueue("D")

# Забираємо елемент та додаємо новий
circular_q.dequeue()
circular_q.enqueue("D")
circular_q.display()
```

### 6. Пріоритетна черга

```python
import heapq

class PriorityQueue:
    def __init__(self):
        """Створює пріоритетну чергу"""
        self.heap = []
        self.index = 0
    
    def enqueue(self, item, priority):
        """Додає елемент з пріоритетом (менше число = вищий пріоритет)"""
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1
        print(f"Додано: {item} (пріоритет: {priority})")
    
    def dequeue(self):
        """Забирає елемент з найвищим пріоритетом"""
        if not self.heap:
            print("Черга порожня!")
            return None
        
        priority, _, item = heapq.heappop(self.heap)
        print(f"Забрано: {item} (пріоритет: {priority})")
        return item
    
    def peek(self):
        """Дивиться на елемент з найвищим пріоритетом"""
        if not self.heap:
            return None
        return self.heap[0][2]
    
    def is_empty(self):
        """Перевіряє, чи черга порожня"""
        return len(self.heap) == 0
    
    def display(self):
        """Показує чергу за пріоритетами"""
        if not self.heap:
            print("Пріоритетна черга порожня")
        else:
            sorted_items = sorted(self.heap)
            print("Пріоритетна черга:")
            for priority, _, item in sorted_items:
                print(f"  {item} (пріоритет: {priority})")

# Демонстрація пріоритетної черги
print("=== ПРІОРИТЕТНА ЧЕРГА ===")
pq = PriorityQueue()

# Додаємо завдання з різними пріоритетами
pq.enqueue("Зробити домашнє завдання", 2)
pq.enqueue("ТЕРМІНОВО: Підготуватись до контрольної", 1)
pq.enqueue("Прочитати книгу", 3)
pq.enqueue("КРИТИЧНО: Здати проект", 0)

pq.display()

print("\nОбробляємо завдання за пріоритетом:")
while not pq.is_empty():
    pq.dequeue()
```

## Ключові поняття
- **FIFO** - First In, First Out (перший зайшов, перший вийшов)
- **Enqueue** - додавання елемента в кінець черги
- **Dequeue** - забирання елемента з початку черги
- **Front** - перший елемент черги
- **Rear** - останній елемент черги
- **Кільцева черга** - черга фіксованого розміру з циклічним використанням
- **Пріоритетна черга** - черга, де елементи обслуговуються за пріоритетом

## Практичні поради
1. Використовуйте `collections.deque` для ефективної реалізації черги
2. Черги ідеальні для обробки завдань у порядку надходження
3. Кільцеві черги економлять пам'ять при фіксованому розмірі
4. Пріоритетні черги корисні для планування завдань
5. BFS використовує чергу для обходу графів по рівнях
6. Завжди перевіряйте, чи черга не порожня перед dequeue()