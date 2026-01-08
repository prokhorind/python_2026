# Приклад 4: Розширені типи черг

print("=== РОЗШИРЕНІ ТИПИ ЧЕРГ ===")

from collections import deque
import heapq
from datetime import datetime, timedelta
import random

# ============================================================================
# 1. КІЛЬЦЕВА ЧЕРГА (CIRCULAR QUEUE)
# ============================================================================

class CircularQueue:
    """Кільцева черга фіксованого розміру"""
    
    def __init__(self, max_size):
        """Ініціалізує кільцеву чергу"""
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0  # Індекс першого елемента
        self.rear = 0   # Індекс для наступного елемента
        self.count = 0  # Кількість елементів
    
    def is_empty(self):
        """Перевіряє, чи черга порожня"""
        return self.count == 0
    
    def is_full(self):
        """Перевіряє, чи черга повна"""
        return self.count == self.max_size
    
    def enqueue(self, item):
        """Додає елемент до черги"""
        if self.is_full():
            print(f"❌ Черга повна! Не можу додати '{item}'")
            return False
        
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size  # Кільцевий перехід
        self.count += 1
        print(f"➕ Додано: {item} (позиція {self.rear - 1})")
        return True
    
    def dequeue(self):
        """Забирає елемент з черги"""
        if self.is_empty():
            print("❌ Черга порожня!")
            return None
        
        item = self.queue[self.front]
        self.queue[self.front] = None  # Очищуємо позицію
        self.front = (self.front + 1) % self.max_size  # Кільцевий перехід
        self.count -= 1
        print(f"➖ Забрано: {item}")
        return item
    
    def peek(self):
        """Дивиться на перший елемент"""
        if self.is_empty():
            return None
        return self.queue[self.front]
    
    def display(self):
        """Показує стан черги"""
        print(f"🔄 Кільцева черга (розмір: {self.count}/{self.max_size}):")
        
        if self.is_empty():
            print("   Черга порожня")
        else:
            # Показуємо елементи в порядку черги
            items = []
            index = self.front
            for _ in range(self.count):
                items.append(str(self.queue[index]))
                index = (index + 1) % self.max_size
            
            print(f"   Елементи: {' → '.join(items)}")
            print(f"   Front: {self.front}, Rear: {self.rear}")
        
        # Показуємо весь масив для розуміння
        array_view = []
        for i in range(self.max_size):
            if self.queue[i] is None:
                array_view.append("_")
            else:
                array_view.append(str(self.queue[i]))
        
        print(f"   Масив: [{', '.join(array_view)}]")

print("1. КІЛЬЦЕВА ЧЕРГА")
print("-" * 30)

# Демонстрація кільцевої черги
circular_q = CircularQueue(4)  # Черга на 4 елементи

print("Заповнюємо чергу:")
circular_q.enqueue("A")
circular_q.display()
print()

circular_q.enqueue("B")
circular_q.enqueue("C")
circular_q.enqueue("D")
circular_q.display()
print()

# Спроба додати до повної черги
circular_q.enqueue("E")
print()

# Забираємо елементи та додаємо нові (демонстрація кільцевості)
print("Демонстрація кільцевого використання:")
circular_q.dequeue()
circular_q.enqueue("E")
circular_q.display()
print()

circular_q.dequeue()
circular_q.enqueue("F")
circular_q.display()

# ============================================================================
# 2. ПРІОРИТЕТНА ЧЕРГА (PRIORITY QUEUE)
# ============================================================================

class PriorityQueue:
    """Пріоритетна черга з використанням heap"""
    
    def __init__(self):
        """Ініціалізує пріоритетну чергу"""
        self.heap = []
        self.index = 0  # Для збереження порядку при однакових пріоритетах
    
    def enqueue(self, item, priority):
        """Додає елемент з пріоритетом (менше число = вищий пріоритет)"""
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1
        print(f"📥 Додано: '{item}' (пріоритет: {priority})")
    
    def dequeue(self):
        """Забирає елемент з найвищим пріоритетом"""
        if not self.heap:
            print("❌ Пріоритетна черга порожня!")
            return None
        
        priority, _, item = heapq.heappop(self.heap)
        print(f"📤 Забрано: '{item}' (пріоритет: {priority})")
        return item
    
    def peek(self):
        """Дивиться на елемент з найвищим пріоритетом"""
        if not self.heap:
            return None
        return self.heap[0][2]  # Повертаємо item
    
    def is_empty(self):
        """Перевіряє, чи черга порожня"""
        return len(self.heap) == 0
    
    def display(self):
        """Показує чергу за пріоритетами"""
        if not self.heap:
            print("📭 Пріоритетна черга порожня")
        else:
            print(f"⭐ Пріоритетна черга ({len(self.heap)} елементів):")
            
            # Сортуємо для показу (не змінюючи heap)
            sorted_items = sorted(self.heap)
            for priority, _, item in sorted_items:
                print(f"   Пріоритет {priority}: '{item}'")

print("\n" + "=" * 50)
print("2. ПРІОРИТЕТНА ЧЕРГА")
print("-" * 30)

# Демонстрація пріоритетної черги
pq = PriorityQueue()

print("Додаємо завдання з різними пріоритетами:")
pq.enqueue("Зробити домашнє завдання", 3)
pq.enqueue("ТЕРМІНОВО: Підготуватись до контрольної", 1)
pq.enqueue("Прочитати книгу", 5)
pq.enqueue("КРИТИЧНО: Здати проект", 0)
pq.enqueue("Прибрати кімнату", 4)
pq.enqueue("ВАЖЛИВО: Дзвонити батькам", 2)

print()
pq.display()

print("\nОбробляємо завдання за пріоритетом:")
while not pq.is_empty():
    pq.dequeue()

# ============================================================================
# 3. ДВОСТОРОННЯ ЧЕРГА (DEQUE)
# ============================================================================

def demonstrate_deque():
    """Демонстрація можливостей deque"""
    print("\n" + "=" * 50)
    print("3. ДВОСТОРОННЯ ЧЕРГА (DEQUE)")
    print("-" * 30)
    
    # Створюємо deque
    dq = deque()
    
    print("Deque дозволяє додавати та забирати з обох кінців:")
    
    # Додавання з різних кінців
    dq.append("Середина")
    print(f"Додали в кінець: {list(dq)}")
    
    dq.appendleft("Початок")
    print(f"Додали на початок: {list(dq)}")
    
    dq.append("Кінець")
    print(f"Додали в кінець: {list(dq)}")
    
    dq.appendleft("Самий початок")
    print(f"Додали на початок: {list(dq)}")
    
    print(f"\nФінальна deque: {list(dq)}")
    
    # Забирання з різних кінців
    print("\nЗабираємо елементи:")
    
    right = dq.pop()  # З правого кінця
    print(f"Забрали справа: '{right}', залишилось: {list(dq)}")
    
    left = dq.popleft()  # З лівого кінця
    print(f"Забрали зліва: '{left}', залишилось: {list(dq)}")
    
    # Практичний приклад: палиндром
    print("\n--- Перевірка паліндрому за допомогою deque ---")
    
    def is_palindrome(text):
        """Перевіряє, чи є текст паліндромом"""
        # Очищуємо текст та переводимо в нижній регістр
        clean_text = ''.join(char.lower() for char in text if char.isalnum())
        
        # Створюємо deque з символів
        char_deque = deque(clean_text)
        
        print(f"Перевіряємо: '{text}'")
        print(f"Очищений текст: '{clean_text}'")
        
        # Порівнюємо символи з обох кінців
        while len(char_deque) > 1:
            left_char = char_deque.popleft()
            right_char = char_deque.pop()
            
            print(f"Порівнюємо: '{left_char}' та '{right_char}'")
            
            if left_char != right_char:
                return False
        
        return True
    
    # Тестуємо паліндроми
    test_words = ["radar", "hello", "А роза упала на лапу Азора", "Python", "level"]
    
    for word in test_words:
        result = is_palindrome(word)
        print(f"'{word}' - {'✅ паліндром' if result else '❌ не паліндром'}")
        print()

demonstrate_deque()

# ============================================================================
# 4. ЧЕРГА З ОБМЕЖЕННЯМ ЧАСУ (TIME-LIMITED QUEUE)
# ============================================================================

class TimeLimitedQueue:
    """Черга з автоматичним видаленням старих елементів"""
    
    def __init__(self, time_limit_seconds=10):
        """Ініціалізує чергу з обмеженням часу"""
        self.queue = deque()
        self.time_limit = timedelta(seconds=time_limit_seconds)
        self.time_limit_seconds = time_limit_seconds
    
    def enqueue(self, item):
        """Додає елемент з поточним часом"""
        timestamp = datetime.now()
        self.queue.append({
            'item': item,
            'timestamp': timestamp,
            'time_str': timestamp.strftime("%H:%M:%S")
        })
        print(f"⏰ Додано: '{item}' о {timestamp.strftime('%H:%M:%S')}")
        
        # Очищуємо старі елементи
        self._cleanup_old_items()
    
    def dequeue(self):
        """Забирає найстарший актуальний елемент"""
        self._cleanup_old_items()
        
        if not self.queue:
            print("❌ Черга порожня або всі елементи застарілі!")
            return None
        
        item_data = self.queue.popleft()
        age = datetime.now() - item_data['timestamp']
        age_seconds = age.total_seconds()
        
        print(f"📤 Забрано: '{item_data['item']}' (вік: {age_seconds:.1f} сек)")
        return item_data['item']
    
    def _cleanup_old_items(self):
        """Видаляє застарілі елементи"""
        current_time = datetime.now()
        removed_count = 0
        
        while self.queue:
            oldest = self.queue[0]
            age = current_time - oldest['timestamp']
            
            if age > self.time_limit:
                expired_item = self.queue.popleft()
                removed_count += 1
                print(f"🗑️  Видалено застарілий: '{expired_item['item']}' (вік: {age.total_seconds():.1f} сек)")
            else:
                break
        
        if removed_count > 0:
            print(f"   Видалено {removed_count} застарілих елементів")
    
    def display(self):
        """Показує поточну чергу з віком елементів"""
        self._cleanup_old_items()
        
        if not self.queue:
            print("📭 Черга порожня")
        else:
            current_time = datetime.now()
            print(f"⏰ Черга з обмеженням {self.time_limit_seconds} сек ({len(self.queue)} елементів):")
            
            for i, item_data in enumerate(self.queue, 1):
                age = current_time - item_data['timestamp']
                age_seconds = age.total_seconds()
                remaining = self.time_limit_seconds - age_seconds
                
                print(f"   {i}. '{item_data['item']}' - додано {item_data['time_str']}")
                print(f"      Вік: {age_seconds:.1f} сек, залишилось: {remaining:.1f} сек")

print("=" * 50)
print("4. ЧЕРГА З ОБМЕЖЕННЯМ ЧАСУ")
print("-" * 30)

# Демонстрація черги з обмеженням часу
import time

timed_queue = TimeLimitedQueue(time_limit_seconds=5)  # 5 секунд

print("Додаємо елементи з інтервалами:")
timed_queue.enqueue("Повідомлення 1")
time.sleep(1)

timed_queue.enqueue("Повідомлення 2")
time.sleep(1)

timed_queue.enqueue("Повідомлення 3")
print()

timed_queue.display()
print()

print("Чекаємо 3 секунди...")
time.sleep(3)

timed_queue.enqueue("Повідомлення 4")
print()

timed_queue.display()
print()

print("Чекаємо ще 3 секунди...")
time.sleep(3)

print("Спроба забрати елемент:")
timed_queue.dequeue()
print()

timed_queue.display()

# ============================================================================
# 5. БАГАТОПОТОЧНА ЧЕРГА (THREAD-SAFE QUEUE)
# ============================================================================

import threading
import queue
import time

def demonstrate_thread_safe_queue():
    """Демонстрація багатопоточної черги"""
    print("\n" + "=" * 50)
    print("5. БАГАТОПОТОЧНА ЧЕРГА")
    print("-" * 30)
    
    # Створюємо thread-safe чергу
    task_queue = queue.Queue(maxsize=5)
    results = []
    
    def producer(name, count):
        """Функція-виробник завдань"""
        for i in range(count):
            task = f"Завдання-{name}-{i+1}"
            task_queue.put(task)
            print(f"🏭 {name} створив: {task}")
            time.sleep(0.1)
        
        print(f"✅ {name} завершив роботу")
    
    def consumer(name):
        """Функція-споживач завдань"""
        while True:
            try:
                # Чекаємо завдання максимум 2 секунди
                task = task_queue.get(timeout=2)
                print(f"⚙️  {name} обробляє: {task}")
                
                # Імітація обробки
                time.sleep(0.2)
                
                results.append(f"{task} -> оброблено {name}")
                task_queue.task_done()
                
            except queue.Empty:
                print(f"⏰ {name} не отримав завдань, завершує роботу")
                break
    
    print("Запускаємо виробників та споживачів:")
    
    # Створюємо потоки
    threads = []
    
    # Виробники
    producer1 = threading.Thread(target=producer, args=("Виробник-А", 3))
    producer2 = threading.Thread(target=producer, args=("Виробник-Б", 2))
    
    # Споживачі
    consumer1 = threading.Thread(target=consumer, args=("Споживач-1",))
    consumer2 = threading.Thread(target=consumer, args=("Споживач-2",))
    
    threads.extend([producer1, producer2, consumer1, consumer2])
    
    # Запускаємо всі потоки
    for thread in threads:
        thread.start()
    
    # Чекаємо завершення виробників
    producer1.join()
    producer2.join()
    
    # Чекаємо обробки всіх завдань
    task_queue.join()
    
    # Чекаємо завершення споживачів
    consumer1.join()
    consumer2.join()
    
    print(f"\n📊 Результати обробки ({len(results)} завдань):")
    for result in results:
        print(f"   {result}")

# Запускаємо демонстрацію багатопоточності
demonstrate_thread_safe_queue()

print("\n" + "=" * 50)
print("🎓 ВИСНОВКИ ПРО РОЗШИРЕНІ ЧЕРГИ:")
print("• Кільцеві черги економлять пам'ять при фіксованому розмірі")
print("• Пріоритетні черги обслуговують важливі елементи першими")
print("• Deque дозволяє ефективно працювати з обома кінцями")
print("• Черги з обмеженням часу автоматично очищають застарілі дані")
print("• Thread-safe черги безпечні для багатопоточних програм")
print("• Кожен тип черги має свої переваги для конкретних задач")