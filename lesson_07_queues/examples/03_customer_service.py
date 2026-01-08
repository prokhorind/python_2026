# Приклад 3: Система обслуговування клієнтів

print("=== СИСТЕМА ОБСЛУГОВУВАННЯ КЛІЄНТІВ ===")

from collections import deque
from datetime import datetime, timedelta
import random

class CustomerServiceSystem:
    def __init__(self, service_name="Банк"):
        """Ініціалізує систему обслуговування"""
        self.service_name = service_name
        self.queue = deque()
        self.current_ticket_number = 1
        self.served_customers = 0
        self.total_wait_time = 0
        self.service_windows = {
            1: {"status": "free", "customer": None},
            2: {"status": "free", "customer": None},
            3: {"status": "free", "customer": None}
        }
    
    def take_ticket(self, customer_name, service_type="загальне"):
        """Клієнт бере номерок"""
        current_time = datetime.now()
        
        ticket = {
            "number": self.current_ticket_number,
            "customer_name": customer_name,
            "service_type": service_type,
            "arrival_time": current_time,
            "estimated_service_time": random.randint(3, 8)  # 3-8 хвилин
        }
        
        self.queue.append(ticket)
        
        print(f"🎫 Номерок видано:")
        print(f"   Номер: {self.current_ticket_number}")
        print(f"   Клієнт: {customer_name}")
        print(f"   Послуга: {service_type}")
        print(f"   Час: {current_time.strftime('%H:%M:%S')}")
        print(f"   Попереду в черзі: {len(self.queue) - 1} людей")
        
        # Оцінка часу очікування
        estimated_wait = (len(self.queue) - 1) * 5  # 5 хвилин на клієнта
        if estimated_wait > 0:
            estimated_time = current_time + timedelta(minutes=estimated_wait)
            print(f"   Орієнтовний час обслуговування: {estimated_time.strftime('%H:%M')}")
        else:
            print(f"   Можете підходити до вільного вікна!")
        
        self.current_ticket_number += 1
        return ticket["number"]
    
    def call_next_customer(self, window_number=1):
        """Викликає наступного клієнта до вікна"""
        if not self.queue:
            print(f"📢 Вікно {window_number}: Черга порожня")
            return None
        
        if self.service_windows[window_number]["status"] == "busy":
            print(f"⏳ Вікно {window_number} зайняте")
            return None
        
        # Забираємо наступного клієнта з черги
        customer = self.queue.popleft()
        current_time = datetime.now()
        
        # Обчислюємо час очікування
        wait_time = current_time - customer["arrival_time"]
        wait_minutes = wait_time.total_seconds() / 60
        
        # Оновлюємо статус вікна
        self.service_windows[window_number] = {
            "status": "busy",
            "customer": customer,
            "service_start": current_time
        }
        
        print(f"🔔 УВАГА! Номер {customer['number']} ({customer['customer_name']})")
        print(f"   Підходьте до вікна {window_number}")
        print(f"   Послуга: {customer['service_type']}")
        print(f"   Час очікування: {wait_minutes:.1f} хвилин")
        
        # Показуємо наступного в черзі
        if self.queue:
            next_customer = self.queue[0]
            print(f"   Наступний: №{next_customer['number']} ({next_customer['customer_name']})")
        
        return customer
    
    def finish_service(self, window_number):
        """Завершує обслуговування клієнта"""
        if self.service_windows[window_number]["status"] == "free":
            print(f"❌ Вікно {window_number} вільне")
            return False
        
        customer = self.service_windows[window_number]["customer"]
        service_start = self.service_windows[window_number]["service_start"]
        current_time = datetime.now()
        
        # Обчислюємо час обслуговування
        service_time = current_time - service_start
        service_minutes = service_time.total_seconds() / 60
        
        # Обчислюємо загальний час від приходу до завершення
        total_time = current_time - customer["arrival_time"]
        total_minutes = total_time.total_seconds() / 60
        
        print(f"✅ Обслуговування завершено:")
        print(f"   Клієнт: {customer['customer_name']} (№{customer['number']})")
        print(f"   Вікно: {window_number}")
        print(f"   Час обслуговування: {service_minutes:.1f} хвилин")
        print(f"   Загальний час: {total_minutes:.1f} хвилин")
        
        # Оновлюємо статистику
        self.served_customers += 1
        self.total_wait_time += total_minutes
        
        # Звільняємо вікно
        self.service_windows[window_number] = {
            "status": "free",
            "customer": None
        }
        
        return True
    
    def show_queue_status(self):
        """Показує поточний стан черги та вікон"""
        current_time = datetime.now()
        
        print(f"\n📊 Стан системи {self.service_name} ({current_time.strftime('%H:%M:%S')}):")
        
        # Стан вікон
        print("🏢 Вікна обслуговування:")
        for window_num, window_info in self.service_windows.items():
            if window_info["status"] == "free":
                print(f"   Вікно {window_num}: 🟢 Вільне")
            else:
                customer = window_info["customer"]
                service_start = window_info["service_start"]
                elapsed = current_time - service_start
                elapsed_minutes = elapsed.total_seconds() / 60
                
                print(f"   Вікно {window_num}: 🔴 Зайняте")
                print(f"      Клієнт: {customer['customer_name']} (№{customer['number']})")
                print(f"      Послуга: {customer['service_type']}")
                print(f"      Обслуговується: {elapsed_minutes:.1f} хв")
        
        # Черга
        print(f"\n👥 Черга ({len(self.queue)} людей):")
        if not self.queue:
            print("   Черга порожня")
        else:
            for i, customer in enumerate(self.queue, 1):
                wait_time = current_time - customer["arrival_time"]
                wait_minutes = wait_time.total_seconds() / 60
                
                print(f"   {i}. №{customer['number']} - {customer['customer_name']}")
                print(f"      Послуга: {customer['service_type']}")
                print(f"      Чекає: {wait_minutes:.1f} хв")
    
    def get_statistics(self):
        """Показує статистику роботи"""
        print(f"\n📈 Статистика {self.service_name}:")
        print(f"   Обслужено клієнтів: {self.served_customers}")
        print(f"   В черзі зараз: {len(self.queue)}")
        print(f"   Наступний номер: {self.current_ticket_number}")
        
        if self.served_customers > 0:
            avg_wait_time = self.total_wait_time / self.served_customers
            print(f"   Середній час обслуговування: {avg_wait_time:.1f} хвилин")
        
        # Завантаженість вікон
        busy_windows = sum(1 for w in self.service_windows.values() if w["status"] == "busy")
        total_windows = len(self.service_windows)
        utilization = (busy_windows / total_windows) * 100
        print(f"   Завантаженість вікон: {busy_windows}/{total_windows} ({utilization:.1f}%)")

# Демонстрація роботи системи
print("Відкриваємо банківське відділення")
bank = CustomerServiceSystem("ПриватБанк")

# Клієнти приходять та беруть номерки
print("\n=== РАНКОВА ЧЕРГА ===")
bank.take_ticket("Анна Петренко", "відкриття рахунку")
bank.take_ticket("Борис Іваненко", "кредит")
bank.take_ticket("Віра Сидоренко", "переказ коштів")
bank.take_ticket("Григорій Коваленко", "обмін валют")
bank.take_ticket("Дарина Мельник", "консультація")

# Показуємо стан системи
bank.show_queue_status()

# Починаємо обслуговування
print("\n=== ПОЧАТОК РОБОТИ ===")
bank.call_next_customer(1)  # Вікно 1
bank.call_next_customer(2)  # Вікно 2

# Показуємо оновлений стан
bank.show_queue_status()

# Завершуємо обслуговування та викликаємо нових клієнтів
print("\n=== ПРОЦЕС ОБСЛУГОВУВАННЯ ===")
bank.finish_service(1)
bank.call_next_customer(1)

bank.finish_service(2)
bank.call_next_customer(2)
bank.call_next_customer(3)  # Відкриваємо третє вікно

# Показуємо стан після активної роботи
bank.show_queue_status()

# Додаємо ще клієнтів
print("\n=== ДЕННИЙ ПОТІК КЛІЄНТІВ ===")
bank.take_ticket("Євген Шевченко", "депозит")
bank.take_ticket("Жанна Бондаренко", "страхування")

# Завершуємо обслуговування решти клієнтів
print("\n=== ЗАВЕРШЕННЯ РОБОЧОГО ДНЯ ===")
while bank.queue or any(w["status"] == "busy" for w in bank.service_windows.values()):
    # Завершуємо обслуговування у зайнятих вікнах
    for window_num in [1, 2, 3]:
        if bank.service_windows[window_num]["status"] == "busy":
            bank.finish_service(window_num)
    
    # Викликаємо нових клієнтів
    for window_num in [1, 2, 3]:
        if bank.queue and bank.service_windows[window_num]["status"] == "free":
            bank.call_next_customer(window_num)
    
    print()

# Фінальна статистика
bank.get_statistics()

# Демонстрація різних типів черг
print("\n" + "="*60)
print("=== РІЗНІ ТИПИ СИСТЕМ ОБСЛУГОВУВАННЯ ===")

# Швидке обслуговування (кафе)
class FastServiceQueue:
    def __init__(self):
        self.queue = deque()
        self.order_number = 1
    
    def place_order(self, customer, item):
        """Розміщення замовлення"""
        order = {
            "number": self.order_number,
            "customer": customer,
            "item": item,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        self.queue.append(order)
        
        print(f"🍔 Замовлення #{self.order_number}: {customer} - {item}")
        print(f"   Позиція в черзі: {len(self.queue)}")
        
        self.order_number += 1
    
    def serve_order(self):
        """Видача замовлення"""
        if not self.queue:
            print("📭 Замовлень немає")
            return
        
        order = self.queue.popleft()
        print(f"🔔 Замовлення #{order['number']} готове!")
        print(f"   {order['customer']}, ваш {order['item']} готовий")

# Тестуємо швидке обслуговування
print("\nКафе 'Швидка їжа':")
cafe = FastServiceQueue()

cafe.place_order("Студент Олексій", "Бургер")
cafe.place_order("Школярка Марія", "Піца")
cafe.place_order("Офісний працівник", "Салат")

print("\nВидача замовлень:")
cafe.serve_order()
cafe.serve_order()
cafe.serve_order()

print("\n=== ВИСНОВКИ ===")
print("Системи обслуговування клієнтів демонструють:")
print("• FIFO принцип - справедливість обслуговування")
print("• Управління чергами - оптимізація часу очікування")
print("• Багатовіконне обслуговування - паралельна робота")
print("• Статистика та аналіз - покращення якості сервісу")
print("• Різні типи послуг - адаптація під потреби бізнесу")